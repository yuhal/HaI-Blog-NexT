---
title: PHP-中文数字替换阿拉伯数字
categories: PHP
---
![image](https://upload-images.jianshu.io/upload_images/15325592-baf44b5b069f9281?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
/**
* 中文数字替换阿拉伯数字
*/
function switchChnNumber($time){
    if(!empty($time)){
        $replaceValueC = [
            "一"=>1,"二"=>2,"两"=>2,"三"=>3,"四"=>4,"五"=>5,
            "六"=>6,"七"=>7,"八"=>8,"九"=>9,"十"=>'0',
            "百"=>'00',"千"=>'000',"万"=>'0000',"块"=>'元'
        ];
        //拆分含有中文的字符串
        $arrTime = preg_split('/(?<!^)(?!$)/u', $time);
        foreach ($arrTime as $key => $value){
            if(isset($replaceValueC[$value]) && $replaceValueC[$value] != ''){
                $arrTime[$key] = $replaceValueC[$value];
            }else{
                $arrTime[$key] = $value;
            }
        }
        return implode("", $arrTime);
    }else{
        return $time;
    }
}
```
