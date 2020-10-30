---
title: TP3-一对一关联查询
categories: TP3
---

![671594626943_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-7e2c29afecef037c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  场景

> 一个学生对应一张学生证，一张学生证对应一个学生，查询某个学生的信息及学生证编号。

#  数据模型

- think_student 学生表

|id|student_name|
|------|------|
|1	|柯南	|
|2	|元太	|
|3	|步美	|
|4	|小哀	|
|5	|光彦	|

- think_student_card 学生证表

|id|student_card_number|student_id|
|------|------|------|
|1	|80199809011901|1|
|2	|80199809011902|2|
|3	|80199809011903|3|
|4	|80199809011904|4|
|5	|80199809011905|5|

#  代码

- 创建 StudentModel.class.php 内容如下：

```
<?php
namespace Home\Model;
use Think\Model\RelationModel;
class StudentModel extends RelationModel {
    protected $_link = array(
        'StudentCard'=>array(
            'mapping_type'      => self::HAS_ONE,
            'mapping_fields'    => 'student_card_number',
        )
    );
}
```

- 创建 StudentCardModel.class.php 内容如下：

```
<?php
namespace Home\Model;
use Think\Model\RelationModel;
class StudentCardModel extends RelationModel {
    protected $_link = array(
        'Student'=>array(
            'mapping_type'      => self::BELONGS_TO,
        )
    );
}
```

- 创建 TestController.class.php 内容如下：

```
<?php
namespace Home\Controller;

use Think\Controller;

class TestController extends Controller {

    public function oneToOne(){
        $student = D('Student');
        $record = $student->field('id,student_name')->relation('StudentCard')->find(1);
        echo json_encode($record);
    }
}
```

#  查询

```
{
    "id": "1",
    "student_name": "柯南",
    "StudentCard": {
        "student_card_number": "80199809011901"
    }
}
```
