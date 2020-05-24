---
title: PHP-phpexcel[导入][导出]实现方法总结
categories: PHP
---
![image](https://upload-images.jianshu.io/upload_images/15325592-c145cd899ba65b9e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# phpexcel导出方法实现过程
```
/** 
 * 数据导出 
 * @param array $title   标题行名称 
 * @param array $data   导出数据 
 * @param string $filename 文件名 
 * @param string $savepath 保存路径 
 * @param $type   是否下载  false--保存   true--下载 
 * @return string   返回文件全路径 
 * @throws phpexcel_exception 
 * @throws phpexcel_reader_exception 
 */  
function exportexcel($title=array(), $data=array(), $filename='', $savepath='./', $isdown=false){  
    include('phpexcel.php');  
    $obj = new phpexcel();  
  
    //横向单元格标识  
    $cellname = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az');  
      
    $obj->getactivesheet(0)->settitle('sheet名称');   //设置sheet名称  
    $_row = 1;   //设置纵向单元格标识  
    if($title){  
        $_cnt = count($title);  
        $obj->getactivesheet(0)->mergecells('a'.$_row.':'.$cellname[$_cnt-1].$_row);   //合并单元格  
        $obj->setactivesheetindex(0)->setcellvalue('a'.$_row, '数据导出：'.date('y-m-d h:i:s'));  //设置合并后的单元格内容  
        $_row++;  
        $i = 0;  
        foreach($title as $v){   //设置列标题  
            $obj->setactivesheetindex(0)->setcellvalue($cellname[$i].$_row, $v);  
            $i++;  
        }  
        $_row++;  
    }  
  
    //填写数据  
    if($data){  
        $i = 0;  
        foreach($data as $_v){  
            $j = 0;  
            foreach($_v as $_cell){  
                $obj->getactivesheet(0)->setcellvalue($cellname[$j] . ($i+$_row), $_cell);  
                $j++;  
            }  
            $i++;  
        }  
    }  
      
    //文件名处理  
    if(!$filename){  
        $filename = uniqid(time(),true);  
    }  
  
    $objwrite = phpexcel_iofactory::createwriter($obj, 'excel2007');  
  
    if($isdown){   //网页下载  
        header('pragma:public');  
        header("content-disposition:attachment;filename=$filename.xls");  
        $objwrite->save('php://output');exit;  
    }  
  
    $_filename = iconv("utf-8", "gb2312", $filename);   //转码  
    $_savepath = $savepath.$_filename.'.xlsx';  
     $objwrite->save($_savepath);  
  
     return $savepath.$filename.'.xlsx';  
}  
  
//exportexcel(array('姓名','年龄'), array(array('a',21),array('b',23)), '档案', './', true);   
```
# phpexcel导入方法实现过程
```
/** 
*  数据导入 
* @param string $file excel文件 
* @param string $sheet 
 * @return string   返回解析数据 
 * @throws phpexcel_exception 
 * @throws phpexcel_reader_exception 
*/  
function importexecl($file='', $sheet=0){  
    $file = iconv("utf-8", "gb2312", $file);   //转码  
    if(empty($file) or !file_exists($file)) {  
        die('file not exists!');  
    }  
    include('phpexcel.php');  //引入php excel类  
    $objread = new phpexcel_reader_excel2007();   //建立reader对象  
    if(!$objread->canread($file)){  
        $objread = new phpexcel_reader_excel5();  
        if(!$objread->canread($file)){  
            die('no excel!');  
        }  
    }  
  
    $cellname = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az');  
  
    $obj = $objread->load($file);  //建立excel对象  
    $currsheet = $obj->getsheet($sheet);   //获取指定的sheet表  
    $columnh = $currsheet->gethighestcolumn();   //取得最大的列号  
    $columncnt = array_search($columnh, $cellname);  
    $rowcnt = $currsheet->gethighestrow();   //获取总行数  
  
    $data = array();  
    for($_row=1; $_row<=$rowcnt; $_row++){  //读取内容  
        for($_column=0; $_column<=$columncnt; $_column++){  
            $cellid = $cellname[$_column].$_row;  
            $cellvalue = $currsheet->getcell($cellid)->getvalue();  
             //$cellvalue = $currsheet->getcell($cellid)->getcalculatedvalue();  # 获取公式计算的值  
            if($cellvalue instanceof phpexcel_richtext){   //富文本转换字符串  
                $cellvalue = $cellvalue->__tostring();  
            }  
  
            $data[$_row][$cellname[$_column]] = $cellvalue;  
        }  
    }  
  
    return $data;  
}  
```
