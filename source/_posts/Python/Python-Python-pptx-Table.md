---
title: Python-Python-pptx-Table
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-e480df7803bd1f18.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# Table对象
使用SlideShapes上的add_table()方法将Table对象添加到幻灯片。

**class pptx.table.Table**
一个DrawingML表对象。不能直接构造，
请使用Slide.shapes.add_table()将表添加到幻灯片。

- cell(row_idx, col_idx)
> 返回位于row_idx，col_idx的单元格。
返回值是_Cell的实例。
row_idx和col_idx是从零开始的，
例如 cell(0，0)是表格中左上方的单元格。

- columns
> 表示表列的_Column对象集合的只读引用。
_Column对象使用列表表示法访问，
例如 col = tbl.columns [0]。

- first_col
> 读/写布尔属性，当为true时，
指示第一列的格式应与表格最左侧的侧栏相同。

- first_row
> 读/写布尔属性，当为true时，
指示第一行应采用不同的格式，例如 用于列标题。

- horz_banding
> 读/写布尔值属性，当为true时，指示表的行应以交替的阴影显示。

- iter_cells()
> 为该表中的每个单元格生成_Cell对象。
每个网格单元都是按从左到右，从上到下的顺序生成的。

- last_col
> 读/写布尔属性，当为true时，
指示最后一列的格式应不同，例如表最右边的总计行。

- last_row
> 读/写布尔属性，当为true时，
指示最后一行的格式应不同，例如表底部的总计行。

- rows
> 表示表行的_Row对象集合的只读引用。
_Row对象使用列表表示法访问，例如 row = tbl.rows [0]。

- vert_banding
> 读/写布尔属性，当为true时，指示表的列应以交替的阴影显示。

# _Column对象
**class pptx.table._Column**
表格列

- width
> 列的宽度，以英制公制单位(EMU)

# _Row对象
**class pptx.table._Row**
表格行

- cells
> 表示表行的_Row对象集合的只读引用。
_Row对象使用列表表示法访问，例如 row = tbl.rows [0]。

- height
> 行的高度，以英制公制单位(EMU)

# _Cell对象
_Cell对象表示表中特定行/列位置的单个表单元格。
_Cell对象不是直接构造的。
使用Table.cell()方法可以获得对_Cell对象的引用，
并指定单元格的行/列位置。
也可以使用_Row.cells集合获得单元对象。

**class pptx.table._Cell(tc, parent)**
表格单元格

- fill
> 此单元格的FillFormat实例，提供对填充属性(例如前景色)的访问。

- is_merge_origin
> 如果此单元格是合并单元格的左上角网格单元格，则为true。

- is_spanned
> 如果此单元格由合并源单元格跨越，则为true。
合并源单元在其合并范围内“跨越”其他网格单元，
从而消耗其面积并“遮蔽”跨过的网格单元。
请注意，对于合并源单元格，此值为False。
合并源单元格跨其他网格单元，但本身不是跨度单元。

- margin_left
> 读/写单元格左边界的整数值作为长度值对象。
如果指定为None，则使用默认值，左右边距为0.1英寸，顶部和底部为0.05英寸。

- margin_right
> 单元格的右边距。

- margin_top
> 单元格的上边距。

- margin_bottom
> 单元格的底边距。

- merge(other_cell)
> 创建从此单元格到other_cell的合并单元格。
此单元格和other_cell指定合并的单元格范围的相对角。
可以以任意顺序指定单元区域的任一对角线，
例如 self =右下角，other_cell =左上角，依此类推。
如果指定范围在其范围内的任何位置已经包含合并的单元格，
或者other_cell与self不在同一表中，则引发ValueError。

- span_height
> 此单元格跨越的int行数。
此属性的值在.is_merge_origin不是True的单元格上可能会引起误解(通常为1)，
> 因为只有合并起源的单元格包含完整的跨度信息。
此属性仅适用于通过测试.is_merge_origin已知为合并起点的单元格。

- span_width
> 此单元格跨越的int列数。
此属性的值在.is_merge_origin不是True的单元格上可能会引起误解(通常为1)，
因为只有合并起源的单元格包含完整的跨度信息。
此属性仅适用于通过测试.is_merge_origin已知为合并起点的单元格。

- split()
> 从此(合并来源)单元中删除合并。
该对象表示的合并单元将被“取消合并"，
从而为先前由该合并所跨越的每个网格单元生成一个单独的未合并单元。
当此单元格不是合并源单元格时，引发ValueError。
在调用之前使用.is_merge_origin进行测试。

- text
> 单元格内容的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并为单元格文本中的每个换行符(软回车)提供一个垂直制表符("\v")。
分配给文本将替换当前包含在单元格中的所有文本。
分配的文本中的换行符("\n")导致新段落开始。
分配的文本中的垂直制表符("\v")导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
假定采用UTF-8编码(正确解码ASCII)，则将字节值转换为unicode。

- text_frame
> 包含出现在单元格中的文本的TextFrame实例。

- vertical_anchor
> 此单元格的垂直对齐。
此值是MSO_VERTICAL_ANCHOR枚举的成员或“无"。
值None表示该单元格没有明确应用垂直锚设置，
并且其有效值是从其样式层次结构祖先继承的。
为该属性分配None将清除任何明确应用的垂直锚设置，
并恢复其有效值的继承。

# Code
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation
from pptx.util import Inches

#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回通过索引slides中的第四个对象
slide = slides[4]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  表格的行列
rows,cols = 3,5
#  预设位置及大小
left,top,width,height = Inches(0.5), Inches(1), Inches(4), Inches(3) 
#  添加一个GraphicFrame对象，
#  其中包含一个具有指定行数和cols以及指定位置和大小的表。
#  宽度均匀地分布在新表的列之间。同样地，高度均匀地分布在行之间。
#  请注意，必须使用返回的GraphicFrame形状上的.table属性来访问所包含的表对象。
shapes.add_table(
	rows,cols,left,top,width,height 
)

#  返回通过索引shapes中的第一个对象
shape = shapes[0]

#  Table此图形框中包含的对象。
#  如果此图形框架不包含表格，则引发ValueError。
table = shape.table

#  返回位于row_idx，col_idx的单元格。
#  返回值是_Cell的实例。row_idx和col_idx是从零开始的，
#  例如 cell(0，0)是表格中左上方的单元格。
row_idx = 1
col_idx = 2
cell = table.cell(
	row_idx,col_idx
)

#  表示表列的_Column对象集合的只读引用。
#  _Column对象使用列表表示法访问，例如 col = tbl.columns [0]。
columns = table.columns
column = columns[0]

#  读/写布尔属性，当为true时，
#  指示第一列的格式应与表格最左侧的侧栏相同。
table.first_col = True
first_col = table.first_col

#  读/写布尔属性，当为true时，
#  指示第一行应采用不同的格式，例如 用于列标题。
table.first_row = False
first_row = table.first_row

#  读/写布尔值属性，当为true时，指示表的行应以交替的阴影显示。
table.horz_banding = False
horz_banding = table.horz_banding

#  为该表中的每个单元格生成_Cell对象。
#  每个网格单元都是按从左到右，从上到下的顺序生成的。
iter_cells = table.iter_cells

#  读/写布尔属性，当为true时，
#  指示最后一列的格式应不同，例如表最右边的总计行。
table.last_col = True
last_col = table.last_col

#  读/写布尔属性，当为true时，
#  指示最后一行的格式应不同，例如表底部的总计行。
table.last_row = True
last_row = table.last_row

#  表示表行的_Row对象集合的只读引用。
#  _Row对象使用列表表示法访问，例如 row = tbl.rows [0]。
rows = table.rows
row = rows[0]

#  读/写布尔属性，当为true时，指示表的列应以交替的阴影显示。
table.vert_banding = True
vert_banding = table.vert_banding

#  列的宽度，以英制公制单位(EMU)
width = column.width

#  对行中单元格集合的只读引用。
#  使用列表表示法引用单个单元格，例如 单元格= row.cells [0]。
cells = row.cells
cell = cells[0]

#  行的高度，以英制公制单位(EMU)
height = row.height

#  此单元格的FillFormat实例，提供对填充属性(例如前景色)的访问。
fill = cell.fill

#  如果此单元格是合并单元格的左上角网格单元格，则为true。
is_merge_origin = cell.is_merge_origin

#  如果此单元格由合并源单元格跨越，则为true。
#  合并源单元在其合并范围内“跨越"其他网格单元，
#  从而消耗其面积并“遮蔽"跨过的网格单元。
#  请注意，对于合并源单元格，此值为False。
#  合并源单元格跨其他网格单元，但本身不是跨度单元。
is_spanned = cell.is_spanned

#  读/写单元格左边界的整数值作为长度值对象。
#  如果指定为None，则使用默认值，左右边距为0.1英寸，顶部和底部为0.05英寸。
cell.margin_left = 91430
margin_left = cell.margin_left

#  单元格的右边距。
cell.margin_right = 91430
margin_right = cell.margin_right

#  单元格的上边距。
cell.margin_top = 91430
margin_top = cell.margin_top

#  单元格的底边距。
cell.margin_bottom = 91430
margin_bottom = cell.margin_bottom

#  创建从此单元格到other_cell的合并单元格。
#  此单元格和other_cell指定合并的单元格范围的相对角。
#  可以以任意顺序指定单元区域的任一对角线，
#  例如 self =右下角，other_cell =左上角，依此类推。
#  如果指定范围在其范围内的任何位置已经包含合并的单元格，
#  或者other_cell与self不在同一表中，则引发ValueError。
other_cell = table.cell(2,2)
cell.merge(other_cell)

#  此单元格跨越的int行数。
#  此属性的值在.is_merge_origin不是True的单元格上可能会引起误解(通常为1)，
#  因为只有合并起源的单元格包含完整的跨度信息。
#  此属性仅适用于通过测试.is_merge_origin已知为合并起点的单元格。
span_height = cell.span_height

#  此单元格跨越的int列数。
#  此属性的值在.is_merge_origin不是True的单元格上可能会引起误解(通常为1)，
#  因为只有合并起源的单元格包含完整的跨度信息。
#  此属性仅适用于通过测试.is_merge_origin已知为合并起点的单元格。
span_width = cell.span_width

#  从此(合并来源)单元中删除合并。
#  该对象表示的合并单元将被“取消合并"，
#  从而为先前由该合并所跨越的每个网格单元生成一个单独的未合并单元。
#  当此单元格不是合并源单元格时，引发ValueError。
#  在调用之前使用.is_merge_origin进行测试。
cell.split()

#  单元格内容的Unicode(在Python 3中为str)表示形式。
#  返回的字符串将包含换行符("\n")，分隔每个段落，
#  并为单元格文本中的每个换行符(软回车)提供一个垂直制表符("\v")。
#  分配给文本将替换当前包含在单元格中的所有文本。
#  分配的文本中的换行符("\n")导致新段落开始。
#  分配的文本中的垂直制表符("\v")导致插入换行符(软回车)。
#  (垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
#  可以分配字节(Python 2 str)或unicode(Python 3 str)。
#  字节可以是7位ASCII或UTF-8编码的8位字节。
#  假定采用UTF-8编码(正确解码ASCII)，则将字节值转换为unicode。
cell.text = 'HaI\'s text'
text = cell.text

#  包含出现在单元格中的文本的TextFrame实例。
text_frame = cell.text_frame

#  此单元格的垂直对齐。
#  此值是MSO_VERTICAL_ANCHOR枚举的成员或“无"。
#  值None表示该单元格没有明确应用垂直锚设置，
#  并且其有效值是从其样式层次结构祖先继承的。
#  为该属性分配None将清除任何明确应用的垂直锚设置，
#  并恢复其有效值的继承。
vertical_anchor = cell.vertical_anchor
```
