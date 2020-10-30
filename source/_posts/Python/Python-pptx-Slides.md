---
title: Python-pptx-Slides
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-df3a1a4a459be399.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# Slides对象
使用Presentation的slides属性可以访问Slides对象。 它不打算直接构造。
**class pptx.slide.Slides**
属于Presentation实例的幻灯片序列，具有访问单个幻灯片的列表语义。 
支持索引访问，len()和迭代。

- add_slide(slide_layout )
> 返回一个新添加的幻灯片，该幻灯片继承了slide_layout的布局。

- get(slide_id，default = None )
> 返回此演示文稿中由整数slide_id标识的幻灯片，如果找不到，则返回默认值。

- index(幻灯片)[来源]
> 将幻灯片映射到表示此幻灯片集合中从零开始的位置的整数。 
在幻灯片上不存在时引发ValueError。

# Slide对象
Slide通过索引从Slides或作为的返回值访问单个对象add_slide()。
**class pptx.slide.Slide**
滑动对象。提供对形状和幻灯片级属性的访问。

- background
> _Background对象提供幻灯片背景属性。
无论幻灯片是否覆盖默认背景或继承默认背景，此属性都将返回_Background对象。 
确定这些条件中的哪一个适用于此幻灯片是使用follow_master_background属性完成的。
每次调用同一幻灯片对象都返回相同的_Background对象。

- element
> 该对象代理的lxml元素。

- follow_master_background
> 如果此幻灯片继承了幻灯片母版背景，则为true。
分配False会导致从主控的后台继承被中断； 
如果此幻灯片没有自定义背景，则会添加默认背景。 
如果此幻灯片已存在自定义背景，则将False赋值无效。
分配为True会导致删除此幻灯片的所有自定义背景，并恢复从母版继承的内容。

- has_notes_slide
> 如果此幻灯片具有注释幻灯片，则返回True，否则返回False。 
注释幻灯片由notes_slide创建(如果不存在)； 
使用此属性可以测试笔记幻灯片，而不会产生创建笔记幻灯片的副作用。

- name
> 表示此幻灯片的内部名称的字符串。 如果未分配名称，
则返回一个空字符串(‘’)。为该属性分配空字符串或无将导致删除任何名称。

- notes_slide
> 返回此幻灯片的NotesSlide实例。 如果幻灯片没有便笺幻灯片，则会创建一个。 
每次调用都返回相同的单个实例。

- placeholders
> 此幻灯片中包含占位符形状序列的SlidePlaceholders实例。

- shapes
> 包含形状对象序列的SlideShapes实例出现在此幻灯片上。

- slide_id
> 在此演示文稿中唯一标识此幻灯片的整数值。 如果通过添加，
重新排列或删除幻灯片来更改幻灯片序列中幻灯片的位置，则幻灯片ID不会更改。

- slide_layout
> 此幻灯片继承其外观的SlideLayout对象。

# SlideLayouts对象
SlideLayouts对象是使用SlideMaster的slide_layouts属性访问的，通常是:
```
from pptx import Presentation
prs = Presentation()
slide_layouts = prs.slide_master.slide_layouts
```
为方便起见，由于大多数演示文稿只有一个幻灯片母版，
因此SlideLayouts可以直接从Presentation对象访问第一个母版的集合 ：
```
slide_layouts = prs.slide_layouts
```
此类不能直接构造。

**class pptx.slide.SlideLayouts**
属于幻灯片母版的幻灯片布局顺序。
支持索引访问，len()，迭代，index()和remove()。

- get_by_name(name，default = None )
> 返回具有名称或没有找到的默认值的SlideLayout对象。

- index(slide_layout )
> 在此集合中返回slide_layout的从零开始的索引。
如果此集合中不存在slide_layout，则引发ValueError。

- part
> 包含此对象的包装部件

- remove(slide_layout )
> 从集合中删除slide_layout。
使用slide_layout时引发ValueError； 
不能删除作为一张或多张幻灯片的基础的幻灯片布局。

# SlideLayout对象
**class pptx.slide.SlideLayout**(element，part )
幻灯片布局对象。提供对占位符，常规形状和幻灯片布局级别属性的访问。

- placeholders
> 在此幻灯片布局中包含占位符形状序列的LayoutPlaceholders实例，按idx顺序排序。

- shapes
> 包含出现在此幻灯片布局上的形状序列的LayoutShapes实例。

- slide_master
> 此幻灯片版式将从其继承属性的幻灯片母版。

- used_by_slides
> 基于此幻灯片布局的幻灯片对象的元组。

- SlideMasters对象
> SlideMasters对象是通过slide_masters属性来访问的，通常是:
```
from pptx import Presentation
prs = Presentation()
slide_masters = prs.slide_masters
```
为方便起见，由于大多数演示文稿只有一个幻灯片母版，
因此可以直接从Presentation对象访问第一个母版而无需索引集合：
```
slide_master = prs.slide_master
```
此类不能直接构造。

**class pptx.slide.SlideMasters**
SlideMaster属于演示文稿的对象序列。
具有列表访问语义，支持索引访问，len()和迭代。

- part
> 包含此对象的包装部件

# SlideMaster对象
**class pptx.slide.SlideMaster**(element，part )
滑动主对象。提供对幻灯片布局的访问。从继承对占位符，
常规形状和幻灯片母版级属性的访问_BaseMaster。

- slide_layouts
> SlideLayouts对象，可以访问此幻灯片母版的布局。

# SlidePlaceholders对象
**class pptx.shapes.shapetree.SlidePlaceholders**(element，parent )
幻灯片上占位符形状的集合。支持对其包含的占位符len()的idx值进行迭代， 和字典式查找。

# NotesSlide对象
**class pptx.slide.NotesSlide**(element，part )
注释幻灯片对象。可在注释讲义页面上访问幻灯片注释占位符和其他形状。

- background
> _Background对象提供幻灯片背景属性。
无论幻灯片，母版或布局是否具有明确定义的背景，此属性都将返回_Background对象。
每次调用同一幻灯片对象都返回相同的_Background对象。

- element
> 该对象代理的lxml元素。

- name
> 表示此幻灯片的内部名称的字符串。如果未分配名称，则返回一个空字符串('')。
None为该属性分配空字符串或 将导致删除任何名称。

- notes_placeholder
> 返回此笔记幻灯片上的笔记占位符，该形状包含实际的笔记文本。
如果没有注释占位符，则返回None；否则返回false。 
尽管这可能很少见，但如果Notes主文件没有正文占位符，
或者如果Notes占位符已从Notes幻灯片中删除，则可能会发生这种情况。

- notes_text_frame
> 返回此便笺幻灯片上便笺占位符的文本框架；如果没有便笺占位符，则返回无。
这是一种快捷方式，可以适应将简单的“注释”文本添加到注释“页面”的常见情况。

- part
> 包含此对象的包装部件

- placeholders
> 在此笔记幻灯片中包含占位符形状序列的NotesSlidePlaceholders实例。

- shapes
> 一个NotesSlideShapes实例，其中包含出现在此笔记幻灯片上的形状对象序列。

# Note
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation

#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回一个新添加的幻灯片，该幻灯片继承了slide_layout的布局。
addSlide = slides.add_slide

#  循环遍历slides
for slide in slides:

	#  返回此演示文稿中由整数slide_id标识的幻灯片，如果找不到，则返回默认值。
	get_slide = slides.get(slide.slide_id)

	#  返回幻灯片映射到表示此幻灯片集合中从零开始的位置的整数
	index = slides.index(get_slide)

	pass

#  返回通过索引slides中的第一个对象
slide = slides[0]

#  返回幻灯片背景属性的对象
background = slide.background

#  返回该对象代理的lxml元素
element = slide.element

#  follow_master_background属性可以确定哪些条件适用于此幻灯片
#  True 如果此幻灯片继承了幻灯片母版背景。
#  分配False会导致从主控的后台继承中断。如果此幻灯片没有自定义背景，则会添加默认背景。
#  如果此幻灯片已存在自定义背景，则分配False无效。
#  分配True会导致删除此幻灯片的所有自定义背景，并恢复从母版的继承。
follow_master_background = slide.follow_master_background

#  如果此幻灯片具有注释幻灯片，则返回True，否则返回False。
#  一张便笺幻灯片是通过notes_slide不存在的幻灯片创建的。
#  使用此属性可以测试笔记幻灯片，而不会产生创建笔记幻灯片的副作用。
has_notes_slide = slide.has_notes_slide

#  表示此幻灯片的内部名称的字符串。如果未分配名称，则返回一个空字符串('')。
slide.name = 'HaI\'s name'
name = slide.name

#  返回NotesSlide此幻灯片的实例。
#  如果幻灯片没有便笺幻灯片，则会创建一个。每次调用都返回相同的单个实例。
notes_slide = slide.notes_slide

#  _Background 提供幻灯片背景属性的对象。
#  _Background无论幻灯片，母版或布局是否具有明确定义的背景，此属性都将返回一个对象。
background = notes_slide.background

#  返回该对象代理的lxml元素。
element = notes_slide.element

#  表示此幻灯片的内部名称的字符串。如果未分配名称，则返回一个空字符串('')。
#  None为该属性分配空字符串或 将导致删除任何名称。
notes_slide.name = 'HaI\'s name'
name = notes_slide.name

#  返回此笔记幻灯片上的笔记占位符，该形状包含实际的笔记文本。
#  如果没有注释占位符，则返回None；
#  尽管这可能很少见，但如果Notes主文件没有正文占位符，或者如果Notes占位符已从Notes幻灯片中删除，则可能会发生这种情况。
notes_placeholder = notes_slide.notes_placeholder

#  返回此笔记幻灯片上笔记占位符的文本框架，或者None如果没有笔记占位符，则返回该文本框。
#  这是一种快捷方式，可以适应将简单的“注释”文本添加到注释“页面”的常见情况。
notes_text_frame = notes_slide.notes_text_frame

#  包含此对象的包装部件
part = notes_slide.part

#  notesslideplaceholder的一个实例，其中包含了本注释幻灯片中占位符形状的序列。
placeholders = notes_slide.placeholders

#  NotesSlideShapes的一个实例，其中包含出现在这张notes幻灯片上的形状对象的序列。
shapes = notes_slide.shapes

#  返回幻灯片中包含占位符形状序列的slideplaceholder实例。
placeholders = slide.placeholders

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  返回在此演示文稿中唯一标识此幻灯片的整数值。
#  如果通过添加，重新排列或删除幻灯片来更改幻灯片序列中幻灯片的位置，则幻灯片ID不会更改。
slide_id = slide.slide_id

#  返回此幻灯片继承外观的对象。
slide_layout = slide.slide_layout

#  SlideLayouts对象是使用SlideMaster的slide_layouts属性访问的
slide_layouts = prs.slide_master.slide_layouts

#  由于大多数演示文稿只有一个幻灯片母版，因此SlideLayouts可以直接从Presentation对象访问第一个母版的集合 ：
slide_layouts = prs.slide_layouts

#  循环遍历slide_layouts
for slide_layout in slide_layouts:

	#  返回具有名称或没有找到的默认值的 SlideLayout对象。
	get_by_name = slide_layouts.get_by_name(slide_layout.name)
	
	#  返回在此集合中返回slide_layout的从零开始的索引。
	#  如果此集合中不存在slide_layout，则引发ValueError 。
	index = slide_layouts.index(slide_layout)
	
	#  返回包含此对象的包装部件
	part = slide_layout.part

	#  返回包含此对象的包装部件
	#  使用slide_layout时引发ValueError;不能删除作为一张或多张幻灯片的基础的幻灯片布局。
	#  这里因引发ValueError错误，先注释
	#  remove = slide_layouts.remove(slide_layout)

	#  返回包含此幻灯片布局中占位符形状序列的layoutplaceholder实例，按idx顺序排序。
	placeholders = slide_layout.placeholders

	#  返回包含此幻灯片布局中出现的形状序列的LayoutShapes实例。
	shapes = slide_layout.shapes

	#  此幻灯片版式将从其继承属性的幻灯片母版。
	slide_master = slide_layout.slide_master

	#  基于此幻灯片布局的幻灯片对象的元组。
	used_by_slides = slide_layout.used_by_slides

	pass

#  SlideMasters对象是通过slide_masters属性来访问的
slide_masters = prs.slide_masters

#  由于大多数演示文稿只有一个幻灯片母版，因此可以直接从Presentation对象访问第一个母版而无需索引集合：
slide_master = prs.slide_master

#  返回包含此对象的包装部件
part = slide_master.part

#  SlideLayouts对象，提供对该幻灯片主布局的访问。
slide_layouts = slide_master.slide_layouts
```
