---
title: Python-Python-pptx-ChartData
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-20e54f2556127ca7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# ChartData 对象
ChartData对象用于指定图表中描述的数据。
在创建新图表和替换现有图表的数据时使用它。
大多数图表是使用CategoryChartData对象创建的，
但是XY和气泡图表类型的数据差异很大，
以至于每个图表都需要一个单独的图表数据对象。

**class pptx.chart.data.ChartData(number_format=u'General')**
ChartData只是CategoryChartData的别名，将来的版本中可能会删除它。
所有新开发都应使用CategoryChartData来创建或替换XY和Bubble以外的图表类型的数据。

**class pptx.chart.data.CategoryChartData(number_format=u'General')**
累积指定图表类别和系列值的数据，并充当将要写入Excel工作表的图表数据表的代理。
作为一个参数shapes.add_chart()和 Chart.replace_data()。

该对象适用于类别表，即所有具有离散标签值(类别)集作为其自变量(X轴)值范围的表。
与支持连续范围的自变量值(例如XyChartData)的图表的ChartData类型不同，
CategoryChartData具有类别(X)值的单个集合，并且其系列中的每个数据点仅指定Y值。
根据其在序列中的位置推断相应的X值。

- add_category(label)
> 返回带有标签的新创建的Category对象，该对象附加到此图表的category集合的末尾。
label可以是字符串，数字，datetime.date或datetime.datetime对象。
图表中的所有类别标签必须为同一类型。图表中具有多级类别的所有类别标签都必须是字符串。

- add_series(name, values=(), number_format=None)
> 向此数据集添加一系列名称为name的数据，并使用值(可迭代的数值)指定数据点。
number_format指定如何显示系列值，并且可以是字符串，例如 对应于Excel数字格式的“＃，##  0”。

- categories
> 类别对象，用于访问此图表数据的类别对象的层次结构。
分配一个可迭代的类别标签(字符串，数字或日期)，
将Categories对象替换为一个新对象，该对象包含序列中每个标签的类别。
> 从具有日期类别的图表数据创建图表将导致该图表的类别轴具有DateAxis。

- values_ref(series)
> Excel工作表对系列值的引用(不包括列标题)。

- number_format
> 格式模板字符串，例如 “＃，##  0.0”，
用于确定此图表和Excel电子表格中X和Y值的格式。
在系列上指定的数字格式将覆盖该系列的该值。
同样，可以为系列中的特定数据点指定不同的数字格式。

**class pptx.chart.data.Categories**
一个类别对象序列，也有一定的层次图行为来支持多层次(嵌套)的类别。

- add_category(label)
> 返回带有标签的新创建的Category对象，该对象附加到此图表的category集合的末尾。
label可以是字符串，数字，datetime.date或datetime.datetime对象。
图表中的所有类别标签必须为同一类型。图表中具有多级类别的所有类别标签都必须是字符串。

> 从具有日期类别的图表数据创建图表将导致该图表的类别轴具有DateAxis。

- are_dates
> 如果此集合中的第一个类别具有日期标签(而不是str或数字)，则返回True。
日期标签是datetime.date或datetime.datetime类型之一。
否则返回False，包括当此类别集合为空时。
当此类别集合是分层类别时，它也返回False，因为分层类别只能写为字符串标签。

- are_numeric
> 如果此集合中的第一个类别具有数字标签(而不是字符串标签)，
包括该值是datetime.date或datetime.datetime对象(将那些转换为整数以存储在Excel中)，
则返回True。否则返回False，包括当此类别集合为空时。
当此类别集合是分层类别时，它也返回False，因为分层类别只能写为字符串标签。

- depth
> 此类别图中的层次结构级别数。如果不包含类别，则返回0。

- index(category)
> 类别在页类别的总体序列中的偏移量。
非页类别获得其第一个子类别的索引。

- leaf_count
> 此层次结构中叶级类别的数量。
仅当层次结构为单级时，返回值才与len()相同。

- levels
> (idx，label)序列的生成器从下至上表示类别层次结构。
第一个级别包含所有页类别，每个后续级别都是下一个级别。

- number_format
> 读/写。返回一个字符串，该字符串表示Excel中用于格式化这些类别值的数字格式，
例如 “ 0.0”或“ mm / dd / yyyy”。该字符串仅在类别为数字或日期类型时才有意义，
尽管在类别为字符串标签时它返回“常规”而不会出错。
根据类别标签的类型，将“无”分配为默认数字格式。

**class pptx.chart.data.Category(label, parent)**
图表类别，主要具有要在类别轴上显示的标签，
但也可以按层次结构进行配置以支持多级类别图表。

- add_sub_category(label)
> 返回带有标签的新创建的Category对象，该对象附加到该类别的子类别序列的末尾。

- label
> 在此类别的轴上显示的值。
标签可以是字符串，数字或datetime.date或datetime.datetime对象。

- numeric_str_val(date_1904=False)
> 此类别的数字(或日期)标签的字符串表示形式，适用于此类别的XML c：pt元素。
可选的date_1904参数指定用于计算Excel日期数字的时期。

- sub_categories
> 此类别的子类别的顺序。

**class pptx.chart.data.XyChartData(number_format=u'General')**
适用于XY(又称散点图)图表的特殊ChartData对象。
与ChartData不同，它没有类别序列。而是，每个系列的每个数据点都指定X和Y值。

- add_series(name, number_format=None)
> 返回在此序列末尾新创建并添加的XySeriesData对象，
该对象由使用number_format格式化的名称和值标识。

- number_format
> 格式模板字符串，例如 “＃，##  0.0”，
用于确定此图表和Excel电子表格中X和Y值的格式。
在系列上指定的数字格式将覆盖该系列的该值。
同样，可以为系列中的特定数据点指定不同的数字格式。

**class pptx.chart.data.BubbleChartData(number_format=u'General')**
适用于气泡图的特殊ChartData对象。
气泡图本质上是XY图，其中标记按比例缩放以为展览提供第三定量维度。

- add_series(name, number_format=None)
> 返回在此序列末尾新创建并添加的BubbleSeriesData对象，
该对象的序列名为name，值使用number_format格式化。

- number_format
> 格式模板字符串，例如 “＃，##  0.0”，
用于确定此图表和Excel电子表格中X和Y值的格式。
在系列上指定的数字格式将覆盖该系列的该值。
同样，可以为系列中的特定数据点指定不同的数字格式。

**class pptx.chart.data.XySeriesData(chart_data, name, number_format)**
特定于XY图表系列的数据。它提供对系列标签，
系列数据点以及可选数字格式的访问，
该可选数字格式将应用于没有指定数字格式的每个数据点。

XY系列中的数据点顺序很重要；
即使点导致线段“向后移动”(暗示多值函数)，
也会按照点的顺序绘制线。
数据点不会自动按X值升序排序。

- add_data_point(x, y, number_format=None)
> 返回一个新创建的XyDataPoint对象，
该对象的值分别为x和y，并附加到此序列中。

- index
> 从零开始的整数，指示此系列在其图表中的序列位置。
例如，三个系列中的第二个将返回1。
如果序列不在图表数据对象中，则引发ValueError。

- name
> 该系列的名称，例如 “系列1”。
此名称用作该系列的y值的列标题，
并且也可能会出现在图表图例和其他图表位置中。

- number_format
> 格式模板字符串，用于确定图表和Excel电子表格中该系列数字的格式。
例如“＃，##  0.0”。如果未为该系列指定，它将从父图表数据对象继承。

- x_values
> 包含此系列中每个数据点的X值的序列(按数据点顺序)。

- y_values
> 包含此系列中每个数据点的Y值的序列(按数据点顺序)。

**class pptx.chart.data.BubbleSeriesData(chart_data, name, number_format)**
特定气泡图系列的特定数据。它提供对系列标签，
系列数据点以及可选数字格式的访问，

该可选数字格式将应用于没有指定数字格式的每个数据点。
在气泡图系列中，数据点的顺序在整个图表构建过程中都得到维护，
因为数据点没有唯一的标识符，只能通过索引来检索。

- add_data_point(x, y, size, number_format=None)
> 追加一个新的BubbleDataPoint对象，其值分别为x，y和size。
可选的number_format用于格式化Y值。
如果未提供，则数字格式将从系列数据继承。

- bubble_sizes
> 一个序列，其中包含该系列中每个数据点的气泡大小(按数据点顺序)。

- data_point_offset
> 在此图表之前的所有图表系列中出现的数据点的整数计数。
如果序列不在图表数据对象中，则引发ValueError。

- index
> 从零开始的整数，指示此系列在其图表中的序列位置。
例如，三个系列中的第二个将返回1。
如果序列不在图表数据对象中，则引发ValueError。

- name
> 该系列的名称，例如 “系列1”。
此名称用作该系列的y值的列标题，
并且也可能会出现在图表图例和其他图表位置中。

- number_format
> 格式模板字符串，用于确定图表和Excel电子表格中该系列数字的格式。
例如“＃，##  0.0”。如果未为该系列指定，它将从父图表数据对象继承。

- x_values
> 包含此系列中每个数据点的X值的序列(按数据点顺序)。

- y_values
> 包含此系列中每个数据点的Y值的序列(按数据点顺序)。

# Code
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from pptx.chart.data import ChartData
from pptx.chart.data import CategoryChartData
from pptx.chart.data import Categories
from pptx.chart.data import Category
from pptx.chart.data import XyChartData
from pptx.chart.data import BubbleChartData
from pptx.chart.data import XySeriesData
from pptx.chart.data import BubbleSeriesData

#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回通过索引slides中的第四个对象
slide = slides[3]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  ChartData只是CategoryChartData的别名，将来的版本中可能会删除它。
#  所有新开发都应使用CategoryChartData来创建或替换XY和Bubble以外的图表类型的数据。
number_format = u'General'
chart_data = ChartData(
	number_format 
)

#  累积指定图表类别和系列值的数据，并充当将要写入Excel工作表的图表数据表的代理。
#  作为一个参数shapes.add_chart()和 Chart.replace_data()。
#  该对象适用于类别表，即所有具有离散标签值(类别)集作为其自变量(X轴)值范围的表。
#  与支持连续范围的自变量值(例如XyChartData)的图表的ChartData类型不同，
#  CategoryChartData具有类别(X)值的单个集合，并且其系列中的每个数据点仅指定Y值。
#  根据其在序列中的位置推断相应的X值。
number_format = u'General'
category_chart_data = CategoryChartData(
	number_format 
)

#  返回带有标签的新创建的Category对象，该对象附加到此图表的category集合的末尾。
#  label可以是字符串，数字，datetime.date或datetime.datetime对象。
#  图表中的所有类别标签必须为同一类型。图表中具有多级类别的所有类别标签都必须是字符串。
label = u'A班级得分率'
category_chart_data.add_category(
	label
)

#  向此数据集添加一系列名称为name的数据，并使用值(可迭代的数值)指定数据点。
#  number_format指定如何显示系列值，并且可以是字符串，例如 对应于Excel数字格式的“＃，##  0”。
name = u'得分率对比'
values = ('80.5')
number_format = None
category_chart_data.add_series(
	name, values, number_format
)

#  类别对象，用于访问此图表数据的类别对象的层次结构。
#  分配一个可迭代的类别标签(字符串，数字或日期)，
#  将Categories对象替换为一个新对象，该对象包含序列中每个标签的类别。
#  从具有日期类别的图表数据创建图表将导致该图表的类别轴具有DateAxis。
categories = category_chart_data.categories

#  Excel工作表对系列值的引用(不包括列标题)。
values_ref = category_chart_data.values_ref

#  格式模板字符串，例如 “＃，##  0.0”，
#  用于确定此图表和Excel电子表格中X和Y值的格式。
#  在系列上指定的数字格式将覆盖该系列的该值。
#  同样，可以为系列中的特定数据点指定不同的数字格式。
number_format = category_chart_data.number_format

#  一个类别对象序列，也有一定的层次图行为来支持多层次(嵌套)的类别。
cate_gories = Categories

#  返回带有标签的新创建的Category对象，该对象附加到此图表的category集合的末尾。
#  label可以是字符串，数字，datetime.date或datetime.datetime对象。
#  图表中的所有类别标签必须为同一类型。图表中具有多级类别的所有类别标签都必须是字符串。
#  从具有日期类别的图表数据创建图表将导致该图表的类别轴具有DateAxis。
add_category = cate_gories.add_category

#  如果此集合中的第一个类别具有日期标签(而不是str或数字)，则返回True。
#  日期标签是datetime.date或datetime.datetime类型之一。
#  否则返回False，包括当此类别集合为空时。
#  当此类别集合是分层类别时，它也返回False，因为分层类别只能写为字符串标签。
are_dates = cate_gories.are_dates

#  如果此集合中的第一个类别具有数字标签(而不是字符串标签)，
#  包括该值是datetime.date或datetime.datetime对象(将那些转换为整数以存储在Excel中)，
#  则返回True。否则返回False，包括当此类别集合为空时。
#  当此类别集合是分层类别时，它也返回False，因为分层类别只能写为字符串标签。
are_numeric = cate_gories.are_numeric

#  此类别图中的层次结构级别数。如果不包含类别，则返回0。
depth = cate_gories.depth

#  类别在页类别的总体序列中的偏移量。
#  非页类别获得其第一个子类别的索引。
index = cate_gories.index

#  此层次结构中叶级类别的数量。
#  仅当层次结构为单级时，返回值才与len()相同。
leaf_count = cate_gories.leaf_count

# (idx，label)序列的生成器从下至上表示类别层次结构。
#  第一个级别包含所有页类别，每个后续级别都是下一个级别。
levels = cate_gories.levels

#  读/写。返回一个字符串，该字符串表示Excel中用于格式化这些类别值的数字格式，
#  例如 “ 0.0”或“ mm / dd / yyyy”。该字符串仅在类别为数字或日期类型时才有意义，
#  尽管在类别为字符串标签时它返回“常规”而不会出错。
#  根据类别标签的类型，将“无”分配为默认数字格式。
cate_gories.number_format = '10/24/2019'
number_format = cate_gories.number_format

#  图表类别，主要具有要在类别轴上显示的标签，
#  但也可以按层次结构进行配置以支持多级类别图表。
label = 80
parent = None
cate_gory = Category(
	label,parent
)

#  返回带有标签的新创建的Category对象，该对象附加到该类别的子类别序列的末尾。
label = u'B班级得分率'
add_sub_category = cate_gory.add_sub_category(
	label
)

#  在此类别的轴上显示的值。
#  标签可以是字符串，数字或datetime.date或datetime.datetime对象。
label = cate_gory.label

#  此类别的数字(或日期)标签的字符串表示形式，适用于此类别的XML c：pt元素。
#  可选的date_1904参数指定用于计算Excel日期数字的时期。
date_1904 = False
numeric_str_val = cate_gory.numeric_str_val(
	date_1904
)

#  此类别的子类别的顺序。
sub_categories = cate_gory.sub_categories

#  适用于XY(又称散点图)图表的特殊ChartData对象。
#  与ChartData不同，它没有类别序列。而是，每个系列的每个数据点都指定X和Y值。
number_format = u'General'
xy_chart_data = XyChartData(
	number_format 
)

#  返回在此序列末尾新创建并添加的XySeriesData对象，
#  该对象由使用number_format格式化的名称和值标识。
name = u'C班级得分率'
number_format = None
add_series = xy_chart_data.add_series(
	name, number_format
)

#  格式模板字符串，例如 “＃，##  0.0”，
#  用于确定此图表和Excel电子表格中X和Y值的格式。
#  在系列上指定的数字格式将覆盖该系列的该值。
#  同样，可以为系列中的特定数据点指定不同的数字格式。
number_format = xy_chart_data.number_format

#  适用于气泡图的特殊ChartData对象。
#  气泡图本质上是XY图，其中标记按比例缩放以为展览提供第三定量维度。
number_format = u'General'
bubble_chart_data = BubbleChartData(
	number_format 
)

#  返回在此序列末尾新创建并添加的BubbleSeriesData对象，
#  该对象的序列名为name，值使用number_format格式化。
name = u'D班级得分率'
number_format = None
add_series = bubble_chart_data.add_series(
	name, number_format
)

#  格式模板字符串，例如 “＃，##  0.0”，
#  用于确定此图表和Excel电子表格中X和Y值的格式。
#  在系列上指定的数字格式将覆盖该系列的该值。
#  同样，可以为系列中的特定数据点指定不同的数字格式。
number_format = bubble_chart_data.number_format

#  特定于XY图表系列的数据。它提供对系列标签，
#  系列数据点以及可选数字格式的访问，
#  该可选数字格式将应用于没有指定数字格式的每个数据点。
#  XY系列中的数据点顺序很重要；
#  即使点导致线段“向后移动”(暗示多值函数)，
#  也会按照点的顺序绘制线。
#  数据点不会自动按X值升序排序。
name = u'系列1' 
number_format = None
xy_series_data = XySeriesData(
	chart_data, name, number_format
)

#  返回一个新创建的XyDataPoint对象，
#  该对象的值分别为x和y，并附加到此序列中。
x, y = Inches(0.5), Inches(1)
number_format = None
add_data_point = xy_series_data.add_data_point(
	x, y, number_format
)

#  从零开始的整数，指示此系列在其图表中的序列位置。
#  例如，三个系列中的第二个将返回1。
#  如果序列不在图表数据对象中，则引发ValueError。
#  index = xy_series_data.index

#  该系列的名称，例如 “系列1”。
#  此名称用作该系列的y值的列标题，
#  并且也可能会出现在图表图例和其他图表位置中。
name = xy_series_data.name

#  格式模板字符串，用于确定图表和Excel电子表格中该系列数字的格式。
#  例如“＃，##  0.0”。如果未为该系列指定，它将从父图表数据对象继承。
number_format = xy_series_data.number_format

#  包含此系列中每个数据点的X值的序列(按数据点顺序)。
x_values = xy_series_data.x_values

#  包含此系列中每个数据点的Y值的序列(按数据点顺序)。
y_values = xy_series_data.y_values

#  特定气泡图系列的特定数据。它提供对系列标签，
#  系列数据点以及可选数字格式的访问，
#  该可选数字格式将应用于没有指定数字格式的每个数据点。
#  在气泡图系列中，数据点的顺序在整个图表构建过程中都得到维护，
#  因为数据点没有唯一的标识符，只能通过索引来检索。
name = u'系列1' 
number_format = None
bubble_series_data = BubbleSeriesData(
	chart_data, name, number_format
)

#  追加一个新的BubbleDataPoint对象，其值分别为x，y和size。
#  可选的number_format用于格式化Y值。
#  如果未提供，则数字格式将从系列数据继承。
x, y, size = Inches(0.5), Inches(1), 20
number_format = None
add_data_point = bubble_series_data.add_data_point(
	x, y, size, number_format
)

#  一个序列，其中包含该系列中每个数据点的气泡大小(按数据点顺序)。
bubble_sizes = bubble_series_data.bubble_sizes

#  在此图表之前的所有图表系列中出现的数据点的整数计数。
#  如果序列不在图表数据对象中，则引发ValueError。
#  data_point_offset = bubble_series_data.data_point_offset

#  从零开始的整数，指示此系列在其图表中的序列位置。
#  例如，三个系列中的第二个将返回1。
#  如果序列不在图表数据对象中，则引发ValueError。
#  index = bubble_series_data.index

#  该系列的名称，例如 “系列1”。
#  此名称用作该系列的y值的列标题，
#  并且也可能会出现在图表图例和其他图表位置中。
name = bubble_series_data.name

#  格式模板字符串，用于确定图表和Excel电子表格中该系列数字的格式。
#  例如“＃，##  0.0”。如果未为该系列指定，它将从父图表数据对象继承。
number_format = xy_series_data.number_format

#  包含此系列中每个数据点的X值的序列(按数据点顺序)。
x_values = xy_series_data.x_values

#  包含此系列中每个数据点的Y值的序列(按数据点顺序)。
y_values = xy_series_data.y_values

```
