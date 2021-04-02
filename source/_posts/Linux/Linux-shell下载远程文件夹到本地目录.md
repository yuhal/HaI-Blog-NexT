---
title: Linux-shell下载远程文件夹到本地目录
categories: Linux
---
![WechatIMG508.jpeg](https://upload-images.jianshu.io/upload_images/15325592-6d0b30e4059483cc.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 最近在操作 syno，尝试通过 shell 脚本定时备份远程服务器的项目信息，在此分享下脚本文件。

- 创建 down.sh，代码如下

```
#  !/bin/bash

#  本地备份根目录
local_base_path='/volume1/Backups/test'

#  远程下载目录
remote_path='Uploads'

#  项目信息
projects=(
    '111.222.333.444' 'root' '1234' 'project'
)

#  主函数
main(){
    length=${# projects[@]}
    for((i=1;i<=${length};i++))
      do
        for project in ${projects[${i}*4-1]}
          do
            #  一台服务器的参数
            host=${projects[${i}*4-4]}
            user=${projects[${i}*4-3]}
            passwd=${projects[${i}*4-2]}

            #  项目备份路径
            project_path=${local_base_path}'/'${project}
            
            #  检查项目备份文件夹是否存在
            if [ ! -d "${project_path}" ] 
                then
                    mkdir ${project_path}
                    #  项目上传目录备份路径
                    project_upload_path=${local_base_path}'/'${project}'/'${remote_path}
                    #  检查项目上传目录备份文件夹是否存在
                    if [ ! -d "${project_upload_path}" ] 
                        then
                            mkdir ${project_upload_path}
                    fi
            fi

            #  远程下载目录(绝对路径)
            upload_path='/mnt/'${project}'/'${remote_path}
            #  本地备份目录(绝对路径)
            local_path=${local_base_path}'/'${project}'/'${remote_path}
            #  执行下载
            down ${user} ${passwd} ${host} 22 ${upload_path} ${local_path}
          done
      done
}

#  执行下载
down(){
lftp -u $1,$2 sftp://$3:$4<<EOF
mirror ${5} ${6}
EOF
}

main
```

- 执行

```
$ ./down.sh
```

- 查看

```
ls /volume1/Backups/test
Uploads
```
