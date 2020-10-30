---
title: TP3-一对多关联查询
categories: TP3
---

![661594626942_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-26398e9b98300685.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  场景 

> 一个班级拥有多个学生，一个学生只能够属于某个班级，查询某个班级的信息及该班级的学生姓名列表。

#  数据模型

- think_student 学生表

|id|student_name|class_id|
|------|------|------|
|1	|柯南	|2|
|2	|元太	|2|
|3	|步美	|2|
|4	|小哀	|2|
|5	|光彦	|2|

- think_class 班级表

|id|class_name|
|------|------|
|1	|一年级A班	|
|2	|一年级B班	|
|3	|一年级C班	|

#  代码

- 创建 ClassModel.class.php 内容如下：

```
<?php
namespace Home\Model;
use Think\Model\RelationModel;
class ClassModel extends RelationModel {
    protected $_link = array(
        'Student'=>array(
            'mapping_type'      => self::HAS_MANY,
            'mapping_fields'    => 'student_name',
        )
    );
}
```

- 创建 StudentModel.class.php 内容如下：

```
<?php
namespace Home\Model;
use Think\Model\RelationModel;
class StudentModel extends RelationModel {
    protected $_link = array(
        'Class'=>array(
            'mapping_type'      => self::BELONGS_TO,
        ),
    );
}
```

- 创建 TestController.class.php 内容如下：

```
<?php
namespace Home\Controller;
use Think\Controller;
class TestController extends Controller {
    public function oneToMany(){
        $class = D('Class');
        $record = $class->relation('Student')->find(2);
        echo json_encode($record);
    }
}
```

#  查询

```
{
    "id": "2",
    "class_name": "一年级B班",
    "Student": [
        {
            "student_name": "柯南"
        },
        {
            "student_name": "元太"
        },
        {
            "student_name": "步美"
        },
        {
            "student_name": "小哀"
        },
        {
            "student_name": "光彦"
        }
    ]
}
```
