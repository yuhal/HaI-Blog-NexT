---
title: 程序设计基础C-作业及复习考题汇总
categories: 程序设计基础C
---
![image](https://upload-images.jianshu.io/upload_images/15325592-7f8b181301b274dd?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 第一次作业
![218.1.73.51_82_mod_quiz_review.php_attempt=1182165.png](https://upload-images.jianshu.io/upload_images/15325592-7ad11b6493a0152d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
--------------------------------------------------------------------------------
# 第二次作业
## 1、阅读下面的程序，并写出程序的运行结果
```
# include <stdio.h>
 
int x=10;
int i=1;
int j=2;
int main(void)
{
	printf("%d,%o,%x\n",x,x,x);
	printf("i=%d\n",++i);
	printf("%c\n",i==j ? 'E' : 'F');//输出 E
	return 0;
}
/*
输出结果
10,12,a
i=2
E
*/
```
## 2、程序填空
### 计算正整数n各位数字之和
```
# include <stdio.h>
  
int main(void)
{
	int n=0;
	int sum=0;

	scanf ("%d",&n);

	while( n!=0 )
	{
	  sum=sum+n%10;

	  n= n/10;
	}

	printf("sum=%d",sum);

   return 0;
}
/*
计算正整数n各位数字之和
1234567890
输出结果
sum=45
*/
```
## 3、编程题
### 从键盘输入10个学生的成绩，计算平均成绩，统计及格人数，计算高于平均分的学生的分数
```
# include <stdio.h>

int main()
{

    int passgrade = 60;//设及格分为60
    int avg;	//平均成绩
    int passnum;	//及格人数
    int totalgrade;	//总分数
    float total[10];	//总分数集合
    int passtotalgrade;	//及格总分数
    int i,x;
	
	printf("请输入10位学生的分数\n");
	printf("********************************\n");
	for(i=0;i<=9;i++)
	{
		printf("请输入一位学生的分数：");
		scanf("%f",&total[i]);
	}

	avg=passnum=totalgrade=passtotalgrade=0; //初始化为0
	for(i=1;i<=9;i++)
	{
		if(total[i]>=60)
		{
			passnum++;
			passtotalgrade+=total[i];
		}
		totalgrade+=total[i];
	}
	avg=totalgrade/10;

    printf("平均成绩avg=: %d\n",avg);
    printf("及格人数passnum=: %d\n",passnum);
    printf("高于平均分的分数passtotalgrade=: %d\n",passtotalgrade);

    return 0;
}
/*
从键盘输入10个学生的成绩，计算平均成绩，统计及格人数，计算高于平均分的学生的分数
请输入10位学生的分数
********************************
请输入一位学生的分数：10
请输入一位学生的分数：20
请输入一位学生的分数：30
请输入一位学生的分数：40
请输入一位学生的分数：50
请输入一位学生的分数：60
请输入一位学生的分数：70
请输入一位学生的分数：80
请输入一位学生的分数：90
请输入一位学生的分数：100
输出结果
平均成绩avg=: 54
及格人数passnum=: 5
高于平均分的分数passtotalgrade=: 400
*/
```
### 从键盘输入一行字符，分别统计其中大写字母和小写字母的个数
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
/*
从键盘输入一行字符，分别统计其中大写字母和小写字母的个数
Hello World 666
输出结果
数字类型的个数3
小写字母的个数8
大写字母的个数2
*/
```
--------------------------------------------------------------------------------
# 复习样卷题
## 一、填空题
1、如果在定义局部变量时省略了存储类型，则默认的类型是(int);
2、语句for(i=1;i==1;i++);的循环次数是(1次);
3、在C语言中，优先级最低的运算符是(逗号表达式);
4、设int a[10]={1,2,3};则*(a+3)的值是(0);
5、在do-while语言的循环体内使用break语言的作用是(跳出循环体)
6、设变量定义int a =2;计算表达式a+=a/=a-=a*a后，变量a的值是(2);
7、在C语言中，注释可以在程序的任何地方，其开始和结束标记是(/**/); 
## 二、程序阅读题(写出程序的运行结果) 
```
# include <stdio.h>

int x=30,y=50;

int sub(int x,int y)
{
	y=x>y?x:y;
	return y;
}

int main()
{
	int x =100;
	printf("%d\n",sub(x,y));
	printf("%d,%d",x,y);
}
/*输出结果
100
100,50
*/
```
```
# include <stdio.h>

int main()
{
	int r=1,n=203,k=0;
	do
	{
		k+=n%10*r;
		n/=10;
		r++;
	}
	while(n);
	printf("%d\n",k);
	return 0;
}
/*输出结果
9
*/
```
```
# include <stdio.h>

int main()
{
	char str[]={'S','H','\0','W','H','Y','\0'};
	int i=0;
	while(i<6)
	printf("%c\n",str[i++]);
	return 0;
}
/*输出结果
S
H

W
H
Y
*/
```
## 三、程序填空题
### 从键盘上输入2个整型数据，并按照从小到大的顺序输出这2个数
```
# include <stdio.h>

int main()
{
	int x,y,t;
	scanf("%d%d",&x,&y);
	if(x>y)
	{
		t=x;x=y;y=t;
	}
	printf("x=%d,y=%d\n",x,y);

}
/*
从键盘上输入2个整型数据，并按照从小到大的顺序输出这2个数
1 2
输出结果
x=1,y=2
*/
```
## 四、编程题
### 从键盘输入一行字符，分别统计其中字母字符和数字字符的个数
```
# include <stdio.h>
# define N 100
# include <string.h>

int main()
{
int len,i,len_char=0,len_num=0;
char s[N];

gets(s);
len=strlen(s);

for(i=0;i<len;i++)
{
	if( ((s[i] <= 'z') && (s[i] >='a')) || ((s[i] <= 'Z') && (s[i] >= 'A')) )
		len_char++;
	if((s[i]<='9') && (s[i]>='0'))
		len_num++;
}

printf("len_char=%d,len_num=%d\n",len_char,len_num);
return 0;

}
/*
从键盘输入一行字符，分别统计其中字母字符和数字字符的个数
123456qwer
输出结果
len_char=4,len_num=6
*/
```
### 从键盘输入十个整型数据，要求输出其中最小的数据
```
# include <stdio.h>
int main()
{
int a[10],i,min;

for(i=0;i<10;i++)
scanf("%d",&a[i]);

min=a[0];

for(i=0;i<10;i++)
{
	if(a[i]<min)
	min = a[i];
}
printf("min=%d\n",min);
return 0;
}
/*
从键盘输入十个整型数据，要求输出其中最小的数据
1 2 3 4 5 6 7 8 9 0
输出结果
0
*/
```
### 从键盘上输入10个字符，然后按相反次序输出
```
# include <stdio.h>
int main()
{
char s[10];
int i;
gets(s);

for(i=9;i>=0;i--)
printf("%c",s[i]);
printf("\n");
return 0;
}
/*
从键盘上输入10个字符，然后按相反次序输出
qwertyuiop
输出结果
poiuytrewq
*/
```
### 从键盘输入10个整数，求他们的平均值以及正数的个数，并加以输出
```
# include <stdio.h>
int main()
{
int a[10],i,avg=0,num=0;
for(i=0;i<10;i++)
scanf("%d",&a[i]);
for(i=0;i<10;i++)
{
avg+=a[i];
if(a[i]>0)
num++;
}
avg/=10;

printf("avg=%d,num=%d\n",avg,num);
return 0;
}
/*
从键盘输入10个整数，求他们的平均值以及正数的个数，并加以输出
1 2 3 4 5 6 7 8 9 0
输出结果
avg=4,num=9
*/
```
