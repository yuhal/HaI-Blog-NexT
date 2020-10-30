---
title: TP3-多对多关联查询
categories: TP3
---

![651594626941_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-ab759e76dcdc3f9b.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  场景

> 一个学生可以选修多门课程，一个课程可以被多个学生选修，查询某个课程的信息及选修该课程的学生姓名列表或者查询某个学生的信息及该学生选修课程的名称列表。

#  数据模型

- think_student 学生表

|id|student_name|
|------|------|
|1	|柯南	|
|2	|元太	|
|3	|步美	|
|4	|小哀	|
|5	|光彦	|

- think_subject 课程表

|id|subject_name|
|------|------|
|1	|算数	|
|2	|图画	|
|3	|体育	|

- think_student_subject 学生课程表

|id|student_id|subject_id|
|------|------|------|
|1	|1	|1|
|2	|3	|2|
|3	|1	|3|

#  多对多关联


- 创建 SubjectModel.class.php 内容如下：

```
<?php
namespace Home\Model;
use Think\Model\RelationModel;
class SubjectModel extends RelationModel {
    protected $_link = array(
        'Student' => array(
            'mapping_type' =>  self::MANY_TO_MANY,
            'mapping_fields'    => 'student_name',
            'mapping_name'      =>  'Students',
            'foreign_key' =>  'subject_id',
            'relation_foreign_key' =>  'student_id',
            'relation_table' => 'think_student_subject',
        ),
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
        'Subject' => array(
            'mapping_type' =>  self::MANY_TO_MANY,
            'mapping_fields'    => 'subject_name',
            'mapping_name'      =>  'Subjects',
            'foreign_key' =>  'student_id',
            'relation_foreign_key' =>  'subject_id',
            'relation_table' => 'think_student_subject',
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
    public function manyToMany(){
		// 查询某个课程的信息及选修该课程的学生姓名列表
        $subject = D('Subject');
        $record = $subject->relation(Students)->find(3);
        echo json_encode($record);
		// 查询某个学生的信息及该学生选修课程的名称列表
		$student = D('Student');
        $record = $student->relation('Subjects')->find(1);
        echo json_encode($record);
    }
}
```

#  查询

```
{
    "id": "3",
    "subject_name": "体育",
    "students": [
        {
            "student_name": "光彦"
        },
        {
            "student_name": "柯南"
        }
    ]
}
```

> 查询体育课程的信息及选修该课程的学生姓名列表

```
{
    "id": "1",
    "student_name": "柯南",
    "Subjects": [
        {
            "subject_name": "算数"
        },
        {
            "subject_name": "体育"
        }
    ]
}
```
> 查询柯南学生的信息及该学生选修课程的名称列表
