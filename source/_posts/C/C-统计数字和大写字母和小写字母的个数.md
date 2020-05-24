---
title: C-统计数字和大写字母和小写字母的个数
categories: C
---

![image](https://upload-images.jianshu.io/upload_images/15325592-d6cffd43e00f9001?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

从键盘输入一行字符，分别统计其中大写字母和小写字母的个数
# 实例
```
# include <stdio.h>

int main(void)
{
	char str;
	int digit,upper,lower;

	digit,upper,lower = 0;//初始化为0
	while((str = getchar()) != '\n'){
		if('0'<=str && str<='9'){
			digit+=1;
		}else if('a'<=str && str<='z'){
			lower+=1;
		}else if('A'<=str && str<='Z'){
			upper+=1;
		}
	}

	printf("数字类型的个数%d\n", digit);
	printf("小写字母的个数%d\n", lower);
	printf("大写字母的个数%d\n", upper);

	return 0;
}
```
# 运行
```
[root@izbp1ipfxx237fclphlj7wz c]#  gcc test.c
[root@izbp1ipfxx237fclphlj7wz c]#  ./a.out
```
# 输入
```
Hello World 666
```
# 输出
```
数字类型的个数3
小写字母的个数8
大写字母的个数2
```
