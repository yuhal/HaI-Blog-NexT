---
title: PHP-常用自定义函数
categories: PHP
---
![WechatIMG8.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e968ee1301c524ce.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  获取分页信息

```
/**
 * 获取分页信息
 * @param int $nowPage 当前页
 * @param int $totalRows 总条数
 * @param int $listRows 每页显示条数，默认为10
 * @return array $aPage
 */
function getPage($nowPage, $totalRows, $listRows=10){
    $totalPages = ceil($totalRows / $listRows);
    $firstRow = ($nowPage-1) * $listRows;
    $firstRow = $firstRow<0 ? 0 : $firstRow;
	// 起始条数
    $aPage['firstRow'] = $firstRow;
	// 每页显示条数
    $aPage['listRows'] = $listRows;
	// 当前页
    $aPage['nowPage'] = $nowPage;
	// 总条数
    $aPage['totalRows'] = $totalRows;
	// 总页数
    $aPage['totalPages'] = $totalPages;
    return $aPage;
}
```

#  二维数组去重

```
/**
 * 二维数组去重
 * @param array $arr 传入数组
 * @param string $key 判断的键值
 * @return array $res
 */
function array_unset_repeat($arr, $key){     
    //建立一个目标数组  
    $res = array();        
    foreach ($arr as $value) {           
        //查看有没有重复项  
        if(isset($res[$value[$key]])){  
            //有：销毁  
            unset($value[$key]);  
        }else{  
            $res[$value[$key]] = $value;  
        }    
    }  
    return array_values($res);  
}  
```

#  二维数组合并重复项

```
/**
 * 二维数组合并重复项
 * @param array $arr 传入数组
 * @param string $key 判断的键值
 * @return array $res
 */
function array_restruct($arr, $key){
    $res = array_column($arr, NULL, $key);
    foreach ($res as &$value) {
        $value = array();
    }
    foreach($arr as $v) {
        array_push($res[$v[$key]], $v);
    }
    return array_values($res);
}
```

#  二维数组排序

```
/**
 * 二维数组排序
 * @param array $arr 传入数组
 * @param string $key 需要排序的键值
 * @param int $order/$type 查看https://www.w3school.com.cn/php/func_array_multisort.asp
 * @return array 转换得到的数组
 */
function array_key_sort($arr, $key, $order=SORT_ASC, $type=SORT_NUMERIC){  
    if(is_array($arr)){  
        foreach ($arr as $array){  
            if (is_array($array)) {  
                $key_arr[] = $array[$key];  
            } else {  
                return false;  
            }  
        }  
    }else{  
        return false;  
    } 
    array_multisort($key_arr, $order, $type, $arr);  
    return $arr;  
}
```

#  二维数组字母排序

```
/**
 * 二维数组按字母A-Z排序
 * @param array $arr 传入数组
 * @param string $key 需要排序的键值
 * @param int $order/$type 查看
 */
function letterSort($arr, $key){
    foreach ($arr as $k => &$v) {
        $name = preg_replace('/^\d+/','',$v[$key]);
        $arr[$k]['letter'] = getFirstLetter( $name );
    }
    $data = array();
    foreach ($arr as $v) {
        if (empty($data[$v['letter']])) {
            $data[$v['letter']] = array();
        }
        $data[$v['letter']][]=$v;
    }
    ksort($data);
    return $data;
}
/**
 * 返回取汉字的第一个字的首字母
 * @param string $str 字符
 * @return string
 */
function getFirstLetter($str){
    if(empty($str)){return '';}
    $fchar=ord($str{0});
    if($fchar>=ord('A')&&$fchar<=ord('z')) return strtoupper($str{0});
    try{
        $s1=iconv('UTF-8','gb2312',$str);
        $s2=iconv('gb2312','UTF-8',$s1);
    }catch (\Exception $e){
        $s1=iconv('UTF-8','GBK',$str);
        $s2=iconv('GBK','UTF-8',$s1);
    }
    $s=$s2==$str?$s1:$str;
    $asc=ord($s{0})*256+ord($s{1})-65536;
    if($asc>=-20319&&$asc<=-20284) return 'A';
    if($asc>=-20283&&$asc<=-19776) return 'B';
    if($asc>=-19775&&$asc<=-19219) return 'C';
    if($asc>=-19218&&$asc<=-18711) return 'D';
    if($asc>=-18710&&$asc<=-18527) return 'E';
    if($asc>=-18526&&$asc<=-18240) return 'F';
    if($asc>=-18239&&$asc<=-17923) return 'G';
    if($asc>=-17922&&$asc<=-17418) return 'H';
    if($asc>=-17417&&$asc<=-16475) return 'J';
    if($asc>=-16474&&$asc<=-16213) return 'K';
    if($asc>=-16212&&$asc<=-15641) return 'L';
    if($asc>=-15640&&$asc<=-15166) return 'M';
    if($asc>=-15165&&$asc<=-14923) return 'N';
    if($asc>=-14922&&$asc<=-14915) return 'O';
    if($asc>=-14914&&$asc<=-14631) return 'P';
    if($asc>=-14630&&$asc<=-14150) return 'Q';
    if($asc>=-14149&&$asc<=-14091) return 'R';
    if($asc>=-14090&&$asc<=-13319) return 'S';
    if($asc>=-13318&&$asc<=-12839) return 'T';
    if($asc>=-12838&&$asc<=-12557) return 'W';
    if($asc>=-12556&&$asc<=-11848) return 'X';
    if($asc>=-11847&&$asc<=-11056) return 'Y';
    if($asc>=-11055&&$asc<=-10247) return 'Z';
    return 'Z';
}
```
