---
title: Linux-no-crontab-for-root
categories: Linux
---
![image](https://upload-images.jianshu.io/upload_images/15325592-1ad501d72324e1af.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 执行```crontab -l```
> 某次查看定时任务列表时，返回```no crontab for root```，因为这个 liunx 服务器第一次使用 crontab ，还没有生成对应的文件导致的。
- 执行```crontab -e```
```
no crontab for root - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]:3
```
> 选择一个编辑器，这里我选了```/usr/bin/vim.tiny```，回车。
```
#  Edit this file to introduce tasks to be run by cron.
# 
#  Each task to run has to be defined through a single line
#  indicating with different fields when the task will be run
#  and what command to run for the task
# 
#  To define the time you can provide concrete values for
#  minute (m), hour (h), day of month (dom), month (mon),
#  and day of week (dow) or use '*' in these fields (for 'any').# 
#  Notice that tasks will be started based on the cron's system
#  daemon's notion of time and timezones.
# 
#  Output of the crontab jobs (including errors) is sent through
#  email to the user the crontab file belongs to (unless redirected).
# 
#  For example, you can run a backup of all your user accounts
#  at 5 a.m every week with:
#  0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
#  For more information see the manual pages of crontab(5) and cron(8)
# 
#  m h  dom mon dow   command
~
~
~
~
~
~
~
~
~
~
~
~
"/tmp/crontab.iE77U6/crontab" 22L, 888C
```
> 执行了```crontab -e```后，就生成了这个文件。
