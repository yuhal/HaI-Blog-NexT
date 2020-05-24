---
title: PHP-实现字符串的所有排列
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-f667c2eded2615ac?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
class Test{

	/**
	 * arr 元素数组，
	 * m 从arr 中选择的元素个数
	 * isRepeat arr中的元素是否可以重复
         * isSortRepeat arr中的元素排序后是否可以重复
	 * b 中间变量
	 * M 等于第一次调用时的 m
	 * res 存放结果
	 */
	public static function combine($arr, $m, $isRepeat = 0, $isSortRepeat = 0, $b = [], $n = 0, $res = []) {
		!$n && $n = $m;
		
		if($m == 1) {
			foreach($arr as $item)
				$res[] = array_merge($b, [$item]);
		} else {
			foreach($arr as $key => $item) {
				$b[$n - $m] = $item;
				
				$tmp = $arr;
				if(!$isRepeat) unset($tmp[$key]);
				
				$res = self::combine($tmp, $m-1, $isRepeat, $b, $n, $res); 
			}
        }
        
        if($isSortRepeat){
            foreach ($res as $key => $value) {
                asort($value);
                $res[$key] = $value;
            }
            $unique_arr = [];
            foreach ($res as $key => $value) {
                $unique_arr[] = implode(',',$value);
            }
            $unique_arr = array_unique($unique_arr);
            $unique_key = array_keys($unique_arr);
            foreach ($res as $key => $value) {
                if(!in_array($key,$unique_key)){
                    unset($res[$key]);    
                }
            }
        }
		
		return $res;
	
}

print_r(Test::combine(['a','b', 'c'], 3));
```
