---
title: 程序设计基础C-自测题汇总
categories: 程序设计基础C
---
![image](https://upload-images.jianshu.io/upload_images/15325592-790e13eee6569835?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 自测题一 
## 判断对错
### 1、C语言中基本数据类型包括整型、实型、字符型。true
### 2、C语言程序总是从main函数第一条可执行语句开始执行，在main函数结束。false
### 3、凡是函数中未指定存储类别的局部变量其隐含的存储类别是自动(auto)变量。true
--------------------------------------------------------------------------------
# 自测题二 
## 选择题
### 1．C 语言属于(C)语言。
A、低级 B、汇编  C、高级 D、面向对象 

### 2．一个 C 语言程序总是从(A)开始执行。 
A、书写顺序的第一个函数 main( ) B、书写顺序的第一条执行语句C、主函数 D、不确定

### 3. C 语言中的标识符只能由字母、数字和下划线组成，且第一个字符(C)
 A、必须为字母 C、必须为字母或下划线 B、必须为下划线 D、可以是字母、数字或下划线中的任一种

### 4. 在 C 语言中，不正确的 int 类型的常数是（A） 
A．32768     B.0      C.037     D.0Xaf

### 5．以下选项中，不能作为合法常量的是（B） 
 A．1.2e04   B．1.2e0.4 	C．1.2e+4 	D．1.2e0

### 6．C语言中的数据的基本类型包括 (C)
A.整型、实型、字符型的逻辑型 B. 整型、实型、字符型和结构体 C. 整型、实型、字符型和枚举型D.整型、实型、字符型和指针型 

--------------------------------------------------------------------------------
# 自测题三
### 1．
```
# include<stdio.h>
# include<string.h>
main()
{
   printf("%d\n", strlen("IBM\n012\t\"\\\0"));
}
```
则程序运行后的输出结果是              。
A)  10         B) 11         C)  16      D)  12

### 2．有如下程序片段：
int i = 0;
while(i++ <= 2);
printf("%d", i);
则正确的执行结果是：
A)  2     B)  3   C)  4     D)  程序陷入死循环
 
### 3、写出运行结果
```
# include<stdio.h>
int main()
{
	int i=16,j,x=6;
	j=i+++1;
	x*=i=j;
	printf("%d,%d\n",j,x);
	return 0;
}
/*
输出结果
17,102
*/
```
--------------------------------------------------------------------------------
# 自测题四 
### 1、 写出运行结果
```
# include<stdio.h>
int main()
{
	int a,b,c,d;
	a=c=0;
	b=1;
	d=20;
	if(a){
	   d=d-10;
	} 
	else if(!b)
	{
	   if(!c)
	   {
	   	d=25;
	   }
	   else
	   {
	   	d=15;	
	   }	
	}
	  
	printf("d=%d\n",d);
	return 0;
}
/*
输出结果
d=20
*/
```
### 2、 写出运行结果
```
# include<stdio.h>
int main()
{
int i=10;
switch(i){
          case 9: i+=1;
          case 10: i+=1;
          case 11: i+=1;
          default : i+=1;
      }
printf("%d",i);
}
/*
输出结果
13
*/
```
### 3、 编程题
计算1-1/2+1/3-1/4+…+1/99-1/100+…,直到最后一项的绝对值小于0.0001为止。
```
# include <stdio.h>
int main(void)
{
    float fm = 1,sum = 0;
    for(;fm < 10000;fm++)
    {
        if((int)fm%2)
            sum += 1/fm;
        else 
            sum -= 1/fm;
    }
    printf("The result is : %f\n",sum);       
    return 0;
}
/*
输出结果
The result is : 0.693192
*/
```
--------------------------------------------------------------------------------
# 自测题五 
### 1、 程序填空
将100至200间不能被3整除的数输出：
```
# include<stdio.h>
int main()
{
	int n;
	for(n=100;n<=200;n++)
	{
	   if(n%3==0)
	   {
	   	printf("%d\n",n);	
	   }
	}
}
/*
输出结果
102
105
108
111
114
117
120
123
126
129
132
135
138
141
144
147
150
153
156
159
162
165
168
171
174
177
180
183
186
189
192
195
198
*/
```
### 2、 程序填空
判断m是否是素数
```
# include <stdio.h>
# include <math.h>
int main(){
    int m;  // 输入的整数 
    int i;  // 循环次数
    int k;  // m 的平方根 

    printf("输入一个整数：");
    scanf("%d",&m);

    // 求平方根，注意sqrt()的参数为 double 类型，这里要强制转换m的类型 
    k=(int)sqrt( (double)m );
    for(i=2;i<=k;i++)
        if(m%i==0)
            break;

    // 如果完成所有循环，那么m为素数
    // 注意最后一次循环，会执行i++，此时 i=k+1，所以有i>k 
    if(i>k)
        printf("%d是素数。\n",m);
    else
        printf("%d不是素数。\n",m);

    return 0;
}
/*
输入一个整数：4
输出结果
4不是素数。
*/
```
--------------------------------------------------------------------------------
# 自测题六 
### 1、 编程题
任意从键盘输入10个整数，按从小到大的顺序排序，并输出结果。
```
# include <stdio.h>
int main()
{
	int a[10];
	int i,j;
	int temp;
	printf("请输入10个整数：");
	for(i=0;i<10;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<9;i++)
	{
		for(j=0;j<9-i;j++)
		{
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	printf("排列后顺序为：");
	for(i=0;i<10;i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n");
	return 0;
}
/*
请输入10个整数：1 2 3 4 5 6 7 8 9 0
排列后顺序为：0 1 2 3 4 5 6 7 8 9
*/
```
### 2、输入一行字符，分别统计求出其中英文字母、空格、数字和其他字符的个数并输出结果。
```
# include <stdio.h>
# include <string.h>
int main()
{
     char c[50];
     int i,el=0,sp=0,nu=0,other=0; 
     gets(c);//输入字符串 
      
     for(i=0; i<strlen(c); i++)//strlen返回字符串长度 
     {
             if((c[i]>='A' && c[i]<='Z')||(c[i]>='a' && c[i]<='z'))
                  el++;
             else if(c[i]>='0'&&c[i]<='9')
                 nu++;
             else if(c[i]==' ')
                 sp++;
             else 
                  other++;
     }
     printf("英文字母个数=%d\n数 字 个 数 =%d\n空 格 字 数 =%d\n其他字符个数=%d\n",el,nu,sp,other);
     return 0;
}
/*
5124u0sahfsfjlss  dfsffsf
输出结果
英文字母个数=18
数 字 个 数 =5
空 格 字 数 =2
其他字符个数=0
*/
```
### 3、 编程打印如下形式的杨辉三角形，打印的杨辉三角形的行数n（不超过10行）要求由用户从键盘输入。要求按照如下函数原型进行编程，不能使用全局变量
```
# include <stdio.h> 
int i,j,a[16][16]={0};/*定义全局变量*/
int main() 
{
	void YHTriangle(int n);/*声明函数*/ 
	void PrintYHTriangle(int n);/*声明函数*/ 
	int n=0;   
	while(n<1 || n>10)   /*不超过10行*/ 
	{ 
		printf("请输入杨辉三角形的行数:");     
		scanf("%d",&n);   
	}
 	YHTriangle(n);/*引用函数*/ 
 	PrintYHTriangle(n);/*引用函数*/
 	return 0;
}
void YHTriangle(int n)/*定义杨辉三角函数*/
{
   
  for(i=0;i<n;i++)     
   a[i][0]=1;                            
   for(i=1;i<n;i++)     
   for(j=1;j<=i;j++)       
    a[i][j]=a[i-1][j-1]+a[i-1][j];    
}
void PrintYHTriangle(int n)/*定义杨辉三角的输出函数*/
{
	YHTriangle(n);
	for(i=0;i<n;i++)                    
    { 
    	for(j=0;j<=i;j++)       
    	printf("%5d",a[i][j]);     
    	printf("\n");   
    } 
}
/*
请输入杨辉三角形的行数:10
输出结果
    1
    1    1
    1    2    1
    1    3    3    1
    1    4    6    4    1
    1    5   10   10    5    1
    1    6   15   20   15    6    1
    1    7   21   35   35   21    7    1
    1    8   28   56   70   56   28    8    1
    1    9   36   84  126  126   84   36    9    1
*/
```
--------------------------------------------------------------------------------
# 自测题七
### 1、 编程输入10个数，找出其中的最大值及其所在的数组下标位置。
```
# include <stdio.h>
int main()
{
    int a[10];
    int i,max;
    for(i = 0; i < 10; i ++)
        scanf("%d",a+i);
    for(max = 0, i=1; i<10; i++)
        if(a[max]<a[i])max = i;
    printf("%d,%d\n",a[max],max);
}
/*
1 2 3 4 5 6 7 8 9 0
输出结果
9,8
*/
```
### 2、韩信点兵。韩信有一队兵，他想知道有多少人，便让士兵排队报数：按从1至5报数，最末一个士兵报的数为1；按从1至6报数，最末一个士兵报的数为5；按从1至7报数，最末一个士兵报的数为4；最后再按从1至11报数，最末一个士兵报的数为10。你知道韩信至少有多少兵吗？
```
# include <stdio.h>
int main()
{
	int x;

	for (x=1; x++;)
	{
		if(x%5==1 && x%6==5 && x%7==4 && x%11==10)
		{
			printf("x=%d\n",x);
			break;
		}
	}
}
/*
输出结果
2111
*/
```
### 3、找出下面程序的错误
下面程序的功能是从键盘输入一行字符，统计其中有多少单词。假设单词之间以空格分开。已知：判断是否有新单词出现的方法——当前被检验字符不是空格，而前一被检验字符是空格，则表示有新单词出现。
```
# include<stdio.h>

int main(){

	int i,num,n=20;

	char str[n];	//改为char str[20]; 

	scanf("%s",str);	//改为gets(str);

	if(str[0] != ' '){

		num = 1;

	}else{

		num = 0;

	}

	for(i=1;i<20;i++){	//改为for(i=1;str[i]!='\o';i++){

		if(str[i]!= ' ' || str[i-1]== ' '){	//改为if(str[i]!= ' ' && str[i-1]== ' '){

			num++;

		}

	}

	printf("num=%d\n",num);

	return 0;

}
/*
Nice to meet you
输出结果
num=4
*/
```
