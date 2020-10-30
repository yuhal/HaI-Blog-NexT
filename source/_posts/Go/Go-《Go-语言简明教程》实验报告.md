---
title: Go-《Go-语言简明教程》实验报告
categories: Go
---
![WechatIMG6.jpeg](https://upload-images.jianshu.io/upload_images/15325592-336445aa1e1c09cd.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![图片描述](https://upload-images.jianshu.io/upload_images/15325592-d253fe53844f55c5?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  整型

|类型	|说明
| ------------ | ------------ |
|byte	|等同于 uint8
|int	|依赖于不同平台下的实现，可以是 int32 或者 int64
|int8	|[-128, 127]
|int16	|[-32768, 32767]
|int32	|[-2147483648, 2147483647]
|int64	|[-9223372036854775808, 9223372036854775807]
|rune	|等同于 int32
|uint	|依赖于不同平台下的实现，可以是 uint32 或者 uint64
|uint8	|[0, 255]
|uint16	|[0, 65535]
|uint32	|[0, 4294967295]
|uint64	|[0, 18446744073709551615]
|uintptr	|一个可以恰好容纳指针值的无符号整型（对 32 位平台是 uint32, 对 64 位平台是 uint64）

#  浮点型

|类型	|说明
| ------------ | ------------ |
|float32	|±3.402 823 466 385 288 598 117 041 834 845 169 254 40x1038 计算精度大概是小数点后 7 个十进制数
|float64	|±1.797 693 134 862 315 708 145 274 237 317 043 567 981x1038 计算精度大概是小数点后 15 个十进制数
|complex32	|复数，实部和虚部都是 float32
|complex64	|复数，实部和虚部都是 float64

#  转义字符

|转义字符	|含义
| ------------ | ------------ |
|\\	|表示反斜线
|'	|单引号
|"	|双引号
|\n	|换行符
|\uhhhh	|4 个 16 进制数字给定的 Unicode 字符

#  字符串切片

|语法	|描述
| ------------ | ------------ |
|s += t	|将字符串 t 追加到 s 末尾
|s + t	|将字符串 s 和 t 级联
|s[n]	|从字符串 s 中索引位置为 n 处的原始字节
|s[n:m]	|从位置 n 到位置 m-1 处取得的字符（字节）串
|s[n:]	|从位置 n 到位置 len(s)-1 处取得的字符（字节）串
|s[:m]	|从位置 0 到位置 m-1 处取得的字符（字节）串
|len(s)	|字符串 s 中的字节数
|len([]rune(s))	|字符串 s 中字符的个数，可以使用更快的方法 utf8.RuneCountInString()
|[ ]rune(s)	|将字符串 s 转换为一个 unicode 值组成的串
|string(chars)	|chars 类型是 []rune 或者 []int32, 将之转换为字符串
|[ ]byte(s)	|无副本的将字符串 s 转换为一个原始的字节的切片数组，不保证转换的字节是合法的 UTF-8 编码字节

#  格式化字符串

|格式化指令	|含义
| ------------ | ------------ |
|%%	|% 字面量
|%b	|一个二进制整数，将一个整数格式化为二进制的表达方式
|%c	|一个 Unicode 的字符
|%d	|十进制数值
|%o	|八进制数值
|%x	|小写的十六进制数值
|%X	|大写的十六进制数值
|%U	|一个 Unicode 表示法表示的整形码值，默认是 4 个数字字符
|%s	|输出以原生的 UTF-8 字节表示的字符，如果 console 不支持 UTF-8 编码，则会输出乱码
|%t	|以 true 或者 false 的方式输出布尔值
|%v	|使用默认格式输出值，或者使用类型的 String() 方法输出的自定义值，如果该方法存在的话
|%T	|输出值的类型

#  数组

|数组创建语法|
| ------------ | 
|[length]Type
|[N]Type{value1, value2, ..., valueN}
|[...]Type{value1, value2, ..., valueN}

#  切片

|切片创建语法|
| ------------ | 
|make([ ]Type, length, capacity)
|make([ ]Type, length)
|[ ]Type{}
|[ ]Type{value1, value2, ..., valueN}
