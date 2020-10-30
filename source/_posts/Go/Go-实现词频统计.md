---
title: Go-实现词频统计
categories: Go
---
![a1ec08fa513d2697d52da0805cfbb2fb4216d875.jpeg](https://upload-images.jianshu.io/upload_images/15325592-a0ccb596c478c3ec.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  功能
- 统计多个文件中英文单词出现的次数
- 按照词频从多到少排序输出
- 支持并发


#  实现
- 创建 file.txt 内容如下：

```
You were the shadow to my light，Did you feel us?
Another start，You fade away
Afraid our aim is out of sight，Wanna see us，Alive
Where are you now? Where are you now?Where are you now?
Was it all in my fantasy?Where are you now?Were you only imaginary?
Where are you now? Atlantis Under the sea Under the sea
Where are you now? Another dream，The monster's running wild inside of me
I'm faded I'm faded  So lost, I'm faded
I'm faded  So lost, I'm faded
These shallow waters never met what I needed I'm letting go a deeper dive
Eternal silence of the sea. I'm breathing alive
Where are you now? Where are you now?
Under the bright but faded lights You've set my heart on fire
Where are you now? Where are you now?
Where are you now? Atlantis
Under the sea Under the sea
Where are you now? Another dream The monster's running wild inside of me
I'm faded I'm faded So lost, I'm faded
I'm faded So lost, I'm faded
```

- 创建 wordcount.go 内容如下：

```
package main

import (
    "bufio"
    "fmt"
    "io"
    "log"
    "os"
    "sort"
    "strings"
    "unicode"
    "unicode/utf8"
    "path/filepath"
)

type Pair struct {
    Key   string
    Value int
}

// PariList实现了sort接口，可以使用sort.Sort对其排序

type PairList []Pair

func (p PairList) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p PairList) Len() int           { return len(p) }
func (p PairList) Less(i, j int) bool { return p[j].Value < p[i].Value } // 逆序

// 提取单词
func SplitOnNonLetters(s string) []string {
    notALetter := func(char rune) bool { return !unicode.IsLetter(char) }
    return strings.FieldsFunc(s, notALetter)
}

/*
   基于map实现了类型WordCount, 并对期实现了Merge(), Report(), SortReport(), UpdateFreq(),
   WordFreqCounter() 方法
*/

type WordCount map[string]int

// 用于合并两个WordCount
func (source WordCount) Merge(wordcount WordCount) WordCount {
    for k, v := range wordcount {
        source[k] += v
    }

    return source
}

// 打印词频统计情况
func (wordcount WordCount) Report() {
    words := make([]string, 0, len(wordcount))
    wordWidth, frequencyWidth := 0, 0
    for word, frequency := range wordcount {
        words = append(words, word)
        if width := utf8.RuneCountInString(word); width > wordWidth {
            wordWidth = width
        }
        if width := len(fmt.Sprint(frequency)); width > frequencyWidth {
            frequencyWidth = width
        }
    }
    sort.Strings(words)
    gap := wordWidth + frequencyWidth - len("Word") - len("Frequency")
    fmt.Printf("Word %*s%s\n", gap, " ", "Frequency")
    for _, word := range words {
        fmt.Printf("%-*s %*d\n", wordWidth, word, frequencyWidth,
            wordcount[word])
    }
}

// 从多到少打印词频
func (wordcount WordCount) SortReport() {
    p := make(PairList, len(wordcount))
    i := 0
    for k, v := range wordcount { // 将wordcount map转换成PairList
        p[i] = Pair{k, v}
        i++
    }

    sort.Sort(p) // 因为PairList实现了排序接口，所以可以使用sort.Sort()对其排序

    wordWidth, frequencyWidth := 0, 0
    for _, pair := range p {
        word, frequency := pair.Key, pair.Value
        if width := utf8.RuneCountInString(word); width > wordWidth {
            wordWidth = width
        }
        if width := len(fmt.Sprint(frequency)); width > frequencyWidth {
            frequencyWidth = width
        }
    }
    gap := wordWidth + frequencyWidth - len("Word") - len("Frequency")
    fmt.Printf("Word %*s%s\n", gap, " ", "Frequency")

    for _, pair := range p {
        fmt.Printf("%-*s %*d\n", wordWidth, pair.Key, frequencyWidth,
            pair.Value)
    }

}

// 从文件中读取单词，并更新其出现的次数
func (wordcount WordCount) UpdateFreq(filename string) {
    var file *os.File
    var err error

    if file, err = os.Open(filename); err != nil {
        log.Println("failed to open the file: ", err)
        return
    }
    defer file.Close() // 本函数退出之前时，关闭文件

    reader := bufio.NewReader(file)
    for {
        line, err := reader.ReadString('\n')
        for _, word := range SplitOnNonLetters(strings.TrimSpace(line)) {
            if len(word) > utf8.UTFMax ||
                utf8.RuneCountInString(word) > 1 {
                wordcount[strings.ToLower(word)] += 1
            }
        }
        if err != nil {
            if err != io.EOF {
                log.Println("failed to finish reading the file: ", err)
            }
            break
        }
    }
}

// 并发统计单词频次
func (wordcount WordCount) WordFreqCounter(files []string) {

    results := make(chan Pair, len(files))  // goroutine 将结果发送到该channel
    done := make(chan struct{}, len(files)) // 每个goroutine工作完成后，发送一个空结构体到该channel，表示工作完成

    for i := 0; i < len(files); { // 有多少个文件就开启多少个goroutine, 使用匿名函数的方式
        go func(done chan<- struct{}, results chan<- Pair, filename string) {
            wordcount := make(WordCount)
            wordcount.UpdateFreq(filename)
            for k, v := range wordcount {
                pair := Pair{k, v}
                results <- pair
            }
            done <- struct{}{}
        }(done, results, files[i])

        i++
    }

    for working := len(files); working > 0; { // 监听通道，直到所有的工作goroutine完成任务时才退出
        select {
        case pair := <-results: // 接收发送到通道中的统计结果
            wordcount[pair.Key] += pair.Value

        case <-done: // 判断工作goroutine是否全部完成
            working--

        }
    }

DONE: // 再次启动for循环处理通道中还未处理完的值
    for {
        select {
        case pair := <-results:
            wordcount[pair.Key] += pair.Value
        default:
            break DONE
        }
    }

    close(results)
    close(done)

}


func main() {
    if len(os.Args) == 1 || os.Args[1] == "-h" || os.Args[1] == "--help" {
        fmt.Printf("usage: %s <file1> [<file2> [... <fileN>]]\n",
            filepath.Base(os.Args[0]))
        os.Exit(1)
    }

    wordcounter := make(WordCount)

    wordcounter.WordFreqCounter(os.Args[1:])

    wordcounter.SortReport()
}
```

- 编译

```
$ go build wordcount.go
$ ls
wordcount  wordcount.go
```

> 执行`go build wordcount.go`对 wordcount.go 进行编译。执行后，查看当前目录已经有了一个可执行文件 wordcount

- 执行

```
$ ./wordcount file.txt |head -n 6
Word   Frequency
you       17
where     12
are       12
now       12
faded     11
```

> 为了方便输出，这里只打印了排名前 5 的单词

