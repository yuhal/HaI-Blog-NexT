---
title: PHP-二维数组的排序
categories: PHP
---
 ![image](https://upload-images.jianshu.io/upload_images/15325592-a2116e572245c9cf?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
function my_sort($arrays,$sort_key,$sort_order=sort_asc,$sort_type=sort_numeric ){  
    if(is_array($arrays)){  
        foreach ($arrays as $array){  
            if(is_array($array)){  
                $key_arrays[] = $array[$sort_key];  
            }else{  
                return false;  
            }  
        }  
    }else{  
        return false;  
    } 
    array_multisort($key_arrays,$sort_order,$sort_type,$arrays);  
    return $arrays;  
}
```
