---
title: PHP-递归实现无限极分类
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-a96e71fc0b1a0291?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
/*
    无限级分类 返回多维数组
 */
function cat_tree($list,$parent_id=0){
    $temp=array();
    foreach($list as $k=>$v){
        if($v['parent_id']==$parent_id){
            $temp[$k]=$v;
            $temp[$k]['son']=cat_tree($list,$v['cat_id']);
              
        }
    }
   return $temp;
}

/*
    无限分类  返回二维数组
 */
function cat_arr($list,$parent_id,$level){
    static $temp=array();
    foreach($list as $v){
        if($parent_id==$v['parent_id']){
            $v['level']=$level;
            $temp[]=$v;
            cat_arr($list,$v['cat_id'],$level+1);
        }
    }
    return $temp;
}
```
