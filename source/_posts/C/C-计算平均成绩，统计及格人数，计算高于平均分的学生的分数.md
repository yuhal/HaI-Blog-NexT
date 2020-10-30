---
title: C-计算平均成绩，统计及格人数，计算高于平均分的学生的分数
categories: C
---
![image.png](https://upload-images.jianshu.io/upload_images/15325592-c779aee843ab6273.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

从键盘输入10个学生的成绩，计算平均成绩，统计及格人数，计算高于平均分的学生的分数
# 实例
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
```
# 运行
```
[root@izbp1ipfxx237fclphlj7wz c]#  gcc test.c
[root@izbp1ipfxx237fclphlj7wz c]#  ./a.out
```
# 输入
```
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
```
# 输出
```
平均成绩avg=: 54
及格人数passnum=: 5
高于平均分的分数passtotalgrade=: 400
```
