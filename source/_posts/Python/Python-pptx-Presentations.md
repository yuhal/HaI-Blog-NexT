---
title: Python-pptx-Presentations
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-baa931ed93e718a2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
使用Presentation()函数打开一个演示文稿，该函数直接由pptx包提供：
```
from pptx import Presentation
```
该函数返回一个Presentation对象，该对象是包含构成表示的组件的图形的根，
例如 幻灯片，形状等。通过遍历图形来引用所有现有的表示组件，
并通过在对象的容器上调用方法来将新对象添加到图形中。
因此，通常不会直接构造python-pptx对象。
例：
```
#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  第一张幻灯片中的第一个形状
sp = prs.slides[0].shapes[0]

#  向第一张幻灯片中添加图片形状
pic = prs.slides[0].shapes.add_picture('image/bg2.jpg', 100, 100, 100, 100)
```

#  Presentation功能
此功能是使用演示文件必须导入的唯一参考。典型用法与许多其他类进行交互，
但是由于使用其包含对象的属性或方法访问它们时，无需构造它们。
**class pptx.Presentation**(pptx = None )
返回Presentation从pptx加载的对象，其中pptx可以是.pptx文件(字符串)的路径，
也可以是类似文件的对象。如果 缺少pptx或None，则将加载内置的默认演示文稿“模板”。

#  Presentation对象
**class pptx.presentation.Presentation**
PresentationML(PML)演示文稿。不打算直接构造。
使用pptx.Presentation()打开或创建演示文稿。

- core_properties
> 拥有此演示文稿的读取/写入Dublin Core文档属性的CoreProperty实例。

- notes_master
> 此演示文稿的NotesMaster实例。如果演示文稿没有便笺母版，
则从默认模板创建一个便笺本并将其返回。每次调用都返回相同的单个实例。

- save(file )
> 将此演示文稿保存到file，其中file可以是文件的路径(字符串)或类似文件的对象。

- slide_height
> 本演示文稿中的幻灯片高度，以英制公制(EMU)为单位。
如果未定义幻灯片宽度，则返回None。读/写。

- slide_layouts
> 属于此演示文稿的第一个SlideMaster的SlideLayout实例的序列。 
一个演示文稿可以有多个幻灯片母版，每个母版都有自己的一组布局。 
对于演示文稿只有一个幻灯片母版的常见情况，此属性很方便。

- slide_master
> 属于此演示文稿的第一个SlideMaster对象。 
通常，演示文稿只有一个幻灯片母版。 
在这种常见情况下，此属性提供了更简单的访问。

- slide_masters
> 属于此演示文稿的SlideMaster对象的序列

- slide_width
> 本演示文稿中的幻灯片宽度，以英语公制单位(EMU)为单位。
如果未定义幻灯片宽度，则返回None。读/写。

- slides
> slides对象，其中包含此演示文稿中的幻灯片

#  CoreProperties对象
每个Presentation对象都有一个CoreProperties通过其core_properties属性访问的对象，
该属性提供对文档的所谓核心属性的读/写访问。
核心属性是作者，类别，评论，content_status，已创建，标识符，关键字，语言，
last_modified_by，last_printed，modified，修订，主题，标题和版本。

每个属性是str，datetime.datetime或int这三种类型之一。 
字符串属性的长度限制为255个字符，如果未设置，则返回一个空字符串(‘’)。 
日期属性被分配并作为没有时区的datetime.datetime对象返回，即在UTC中。 
任何时区转换均由客户负责。 如果未设置，日期属性将返回无。

python-pptx不会自动设置任何文档核心属性，
除非将核心属性部分添加到不包含该属性的演示文稿中(非常少见)。
如果python-pptx添加了核心属性部分，则它包含标题，last_modified_by，
修订版和修改后属性的默认值。如果需要该行为，
客户端代码应显式更改诸如revend和last_modified_by之类的属性。

**class pptx.opc.coreprops.CoreProperties**
- author
> string –主要负责制作资源内容的实体。

- category
> string –此软件包内容的分类。值示例包括：简历，信函，财务预测，提案或技术演示。

- comments
> string –资源内容的帐户。

- content_status
> string –文档的完成状态，例如“草稿”

- created
> datetime –最初创建文档的时间

- identifier
> string –在给定上下文(例如ISBN)中对资源的明确引用。

- keywords
> string –描述性词或短短语可能会用作本文档的搜索词

- language
> string -文档所用的语言

- last_modified_by
> string –上次修改文档的人的姓名或其他标识符(例如电子邮件地址)

- last_printed
> datetime –文档上次打印的时间

- modified
> datetime –文档上次修改的时间

- revision
> int –此修订版的编号，每次保存文档时，PowerPoint®客户端将其递增一次。
但是请注意，版本号不会由python-pptx自动增加。

- subject
> string –资源内容的主题。

- title
> string –给资源的名称。

- version
> string –自由格式的字符串

#  Note
```
#  !/usr/bin/python
#  coding:utf-8
from pptx import Presentation
import sys
#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  在第一张幻灯片中获得对第一个形状的引用
sp = prs.slides[0].shapes[0]

#  向第一张幻灯片中添加图片形状
pic = prs.slides[0].shapes.add_picture('image/bg2.jpg', 100, 100, 100, 100)

#  此演示文稿的NotesMaster实例。如果演示文稿没有便笺母版，
则从默认模板创建一个便笺本并将其返回。每次调用都返回相同的单个实例。
note = prs.notes_master

#  本演示文稿中的幻灯片高度，以英制公制(EMU)为单位。
None如果未定义幻灯片宽度，则返回。读/写。
height = prs.slide_height

#  属于此演示文稿的第一个SlideMaster的SlideLayout实例的序列。 
一个演示文稿可以有多个幻灯片母版，每个母版都有自己的一组布局。 
对于演示文稿只有一个幻灯片母版的常见情况，此属性很方便。
layouts = prs.slide_layouts

#  属于此演示文稿的第一个SlideMaster对象。 
通常，演示文稿只有一个幻灯片母版。 
在这种常见情况下，此属性提供了更简单的访问。
master = prs.slide_master

#  属于此演示文稿的SlideMaster对象的序列
masters = prs.slide_masters

#  本演示文稿中的幻灯片宽度，以英语公制单位(EMU)为单位。
如果未定义幻灯片宽度，则返回None。读/写。
width = prs.slide_width

#  slides对象，其中包含此演示文稿中的幻灯片
slides = prs.slides

#  每个Presentation对象都有一个CoreProperties通过其core_properties属性访问的对象，
该属性提供对文档的所谓核心属性的读/写访问
core_properties = prs.core_properties

core_properties.author = 'HaI'
core_properties.category = 'python-pptx'
core_properties.comments = 'HaI\'s comments'
core_properties.content_status = "draft"
core_properties.identifier = 'HaI\'s identifier'
core_properties.keywords = 'HaI\'s keywords'
core_properties.language = 'utf-8'
core_properties.last_modified_by = 'HaI\'s last_modified_by'
core_properties.subject = 'HaI\'s subject'
core_properties.title = 'HaI\'s title'
core_properties.version = 'v1.0.0'

#  string –主要负责制作资源内容的作者。
author = core_properties.author
#  string –此软件包内容的分类。值示例包括：简历，信函，财务预测，提案或技术演示。
category = core_properties.category
#  string –资源内容的帐户。
comments = core_properties.comments
#  string –文档的完成状态，例如“草稿”
content_status = core_properties.content_status
#  datetime –最初创建文档的时间
created = core_properties.created
#  string –在给定上下文(例如ISBN)中对资源的明确引用。
identifier = core_properties.identifier
#  string –描述性词或短短语可能会用作本文档的搜索词
keywords = core_properties.keywords
#  string -文档所用的语言
language = core_properties.language
#  string –上次修改文档的人的姓名或其他标识符(例如电子邮件地址)
last_modified_by = core_properties.last_modified_by
#  datetime –文档上次打印的时间
last_printed = core_properties.last_printed
#  datetime –文档上次修改的时间
modified = core_properties.modified
#  int –此修订版的编号，每次保存文档时，PowerPoint®客户端将其递增一次。
#  但是请注意，版本号不会由python-pptx自动增加。
revision = core_properties.revision
#  string –资源内容的主题。
subject = core_properties.subject
#  string –给资源的名称。
title = core_properties.title
#  string –自由格式的字符串
version = core_properties.version

prs.save('pptx/zf-01.pptx')
```
