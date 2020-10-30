---
title: Python-pptx-Chart
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-461c9db840408151.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  图表
python-pptx提供了一个用于添加和操作图表的API。
图表对象（例如表格）不是形状。
而是它是包含在GraphicFrame形状中的图形对象。
图形框架形状提供形状API，例如位置，大小，形状ID和名称。
使用chart图形框架形状上的属性可以访问图表本身。

#  Chart对象
该Chart对象是组成对象的一般分层图的根，
这些图共同提供对指定和设置图表格式所需的属性和方法的访问。

***class pptx.chart.chart.Chart（chartSpace，chart_part ）***
图表对象。

- category_axis
此图表的类别轴。对于XY或气泡图，这是X轴。
ValueError如果未定义类别轴则引发（例如，饼图的情况）。

- chart_style
用于格式化此图表的图表样式的读/写整数索引。范围是1到48。
值是None如果未分配显式样式，则使用默认图表样式。
分配 None会导致删除任何显式设置。
整数索引对应于PowerPoint UI中图表样式库中样式的位置。

- chart_title
ChartTitle提供对标题属性的访问的对象。
调用此属性具有破坏性，因为如果尚不存在，
则将图表标题元素（c：title）添加到图表XML中。
使用has_title于测试图表标题非破坏性的存在。

- chart_type
只读XL_CHART_TYPE枚举值，指定此图表的类型。
如果图表有两个图，例如在条形图上叠加了一个线图，
则报告的类型适用于第一个（最后一个）图。

- font
此图表的默认字体对象控制文本格式。

- has_legend
True如果图表有图例，则读/写布尔值。
True如果没有图例，则分配 将使图例添加到图表中。
分配False会删除所有现有的图例定义以及任何现有的图例设置。

- has_title
读/写布尔值，指定此图表是否具有标题。
分配True会导致添加标题（如果尚不存在）。
分配False会删除所有现有标题及其文本和设置。

#  legend
一个Legend对象，提供对该图表的图例属性的访问。

- plots
此图中的绘图顺序。图表 在Microsoft API中称为图表组，
是在特定图表类型中描绘的一个或多个系列的不同序列。
例如，如果一个图表的序列绘制为一条线，而三个序列绘制为列，
则该图表将具有两个图。第一个对应于三列系列，第二个对应于线系列。
绘图按绘制顺序排序，即从最后到最前。支持len（），
成员资格（例如），迭代，切片和索引访问（例如）。
p in plotsplot = plots[i]

- replace_data（chart_data ）
使用ChartData对象 chart_data中的类别和系列值替换该图表的XML和Excel工作表中的类别和系列值。

- series
甲SeriesCollection包含此图表中系列对象。
当图表具有多个图时，第一个图的所有序列出现在第二个图的所有序列之前，
依此类推。绘图中的系列具有明确的顺序，并按该顺序显示。

- value_axis
ValueAxis提供访问此图表的值轴属性的对象。
ValueError如果图表没有值轴，则引发。

***class pptx.chart.chart.ChartTitle***
提供用于操纵图表标题的属性。

- format
ChartFormat 提供访问行和填充格式的对象。
返回ChartFormat提供此图表标题的形状格式设置属性的对象，例如其线条颜色和填充。

- has_text_frame
读/写布尔值，指定此标题是否具有文本框架。
返回True如果这个图表标题有一个文本框，和False 其他。
分配True会导致添加文​​本框（如果尚不存在）。
分配False会导致删除任何现有文本框架以及其文本和格式。

- text_frame
TextFrame 该图表标题的实例。
返回一个TextFrame实例，该实例允许对该图表标题的文本及其文本格式设置属性进行读/写访问。
从某种意义上说，如果不存在该属性，则访问该属性会破坏性。
使用has_text_frame测试一个文本框的存在非破坏性。

#  Legend对象
图例通过将颜色，线型或点形状映射到每个系列名称来提供将每个数据点系列与其指定含义相关联的可视键。
图例是可选的，但最多可以有一个。图例的大多数方面是自动确定的，但是可以通过API指定其位置的方面。

***class pptx.chart.chart.Legend***
在图表中表示图例。一张图表最多可以包含一个图例。

- font
Font提供对此图例的文本属性（例如，粗体，斜体等）的访问权限的对象。

- horz_offset
从图例的默认值调整图例的x位置。表示为-1.0和1.0之间的浮点数，
表示图表宽度的一部分。负值将图例向左移动，正值将其向右移动。None如果未指定设置。

- include_in_layout
True 图例是否应位于情节区域内。
读/写布尔值，指定是否应在图例区域内放置图例。在许多情况下，这将使其叠加在图表本身上。
分配None给此属性会导致删除任何 c：overlay元素，其解释与相同 True。
很少需要这种用例，建议分配一个布尔值。

- position
读/写XL_LEGEND_POSITION枚举值，指定要在其中放置图例的图表的常规区域。

#  Axis对象
图表通常具有两个轴，即类别轴和值轴。通常，其中一个是水平的，
另一个是垂直的，这取决于图表类型。
例如，类别轴在柱形图上是水平的，而在条形图上是垂直的。
自变量处于连续（数字）范围内的图表（例如XY /散点图）没有类别轴。
而是有两个值轴。
类别可能是最常见的字符串标签，例如'East'或 'Revenue'；
但是，类别也可以是数字或日期（尽管图表中的所有类别都必须是同一类型）。
当图表的类别是日期时，类别轴通常是但不一定是DateAxis对象。
图表可能有零到四个轴。例如，饼图既没有类别也没有值轴。

***class pptx.chart.axis._BaseAxis***
图表轴对象的基类。所有轴对象共享这些属性。

- axis_title
AxisTitle提供访问标题属性的对象。
调用此属性具有破坏性，因为如果尚不存在，
则将轴标题元素（c：title）添加到轴XML中。使用has_title于测试轴标题非破坏性的存在。

- format
通过该ChartFormat对象可以访问此轴的形状格式设置属性，例如其线条颜色和填充。

- has_major_gridlines
读/写布尔值，指定此轴在其主要刻度线位置处是否具有网格线。
分配True给该属性将导致显示主要网格线。分配False会使它们被删除。

- has_minor_gridlines
读/写布尔值，指定此轴在其次刻度线位置是否具有网格线。
分配True给该属性将导致显示较小的网格线。分配False会使它们被删除。

- has_title
读/写布尔值，指定此轴是否具有标题。
True如果该轴有标题，则为Falsefalse。
分配True 会导致添加轴标题（如果尚不存在）。
分配将 False导致删除任何现有标题。

- major_gridlines
MajorGridlines代表该轴主要网格线的对象。

- major_tick_mark
读/写XL_TICK_MARK值，指定要在此轴上显示的主要刻度线的类型。

- maximum_scale
读/写浮点值，指定该轴的值范围的上限，
分别是垂直或水平值刻度的顶部或右侧的数字。
该值None指示应根据与轴关联的数据点值的范围自动确定上限。

- minimum_scale
读/写浮点值，指定值范围的下限，值刻度底部或左侧的数字。
None如果未设置最小刻度。该值None指示应根据与轴关联的数据点值的范围自动确定下限。

- minor_tick_mark
读/写XL_TICK_MARK值，指定该轴的次刻度线的类型。

- tick_labels
该TickLabels实例提供对轴刻度标签格式设置属性的访问。
刻度标签是出现在值轴上的数字或出现在类别轴上的类别名称。

- tick_label_position
读/写XL_TICK_LABEL_POSITION值，指定该轴的刻度标签应出现的位置。

- visible
读/写。True如果轴可见，False否则。

***class pptx.chart.axis.CategoryAxis***
图表的类别轴。

- category_type
XL_CATEGORY_TYPE的成员，指定此轴的比例类型。
无条件CATEGORY_SCALE的CategoryAxis对象。

***class pptx.chart.axis.DateAxis***
具有日期作为其类别标签的类别轴，并且具有一些特殊的显示行为，
例如，使等长的时间相等，并且使月份开始日期归一化，尽管月份长度不相等。

- category_type
XL_CATEGORY_TYPE的成员，指定此轴的比例类型。
无条件TIME_SCALE的DateAxis对象。

***class pptx.chart.axis.AxisTitle***
提供用于操纵轴标题的属性。

- format
ChartFormat 提供访问形状格式的对象。
返回ChartFormat提供此轴标题的形状格式设置属性的对象，例如其线条颜色和填充。

- has_text_frame
读/写布尔值，指定是否存在文本框架。
返回True如果此轴标题有一个文本框，和False 其他。
分配True会导致添加文​​本框（如果尚不存在）。
分配False会导致删除任何现有文本框架以及该文本框架中包含的所有文本。

- text_frame
TextFrame 该轴标题的实例。
返回一个TextFrame实例，该实例允许对该轴标题的文本及其文本格式设置属性进行读/写访问。
访问此属性具有破坏性，因为它会添加新的文本框（如果尚不存在）。

#  ValueAxis
一些轴属性仅与值轴相关，特别是那些与数字值相关的属性，而不是与文本类别标签相关的属性。

***class pptx.chart.axis.ValueAxis***
具有连续（相对于离散）值的轴。纵轴通常是值轴，但是XY型图表的两个轴都是值轴。

- crosses
XL_AXIS_CROSSES枚举的成员，指定该轴上另一个轴与之交叉的点，例如自动/零，最小或最大。
当定义了特定的数字交叉点（例如1.5）时，返回XL_AXIS_CROSSES.CUSTOM。

- crosses_at
垂直轴相交的轴上的数值。None如果未设置交叉值，则返回。

- major_unit
该值轴上主要刻度线之间的浮点数。
None对应于用户界面中的“自动”设置，并指定该值应由PowerPoint基于基础图表数据进行计算。

- minor_unit
该值轴上次刻度线之间的浮点数。
None对应于用户界面中的“自动”设置，并指定该值应由PowerPoint基于基础图表数据进行计算。

#  MajorGridlines对象
网格线是垂直和水平线，它们在图表上延伸轴的主要刻度线，以便于比较数据点与轴的划分。

***class pptx.chart.axis.MajorGridlines***
提供对出现在轴上的主要网格线属性的访问。

- format
在ChartFormat提供对所述形状格式化此数据点的属性，如线和填充对象。

#  TickLabels对象
刻度标签是出现在值轴上的数字或出现在类别轴上的类别名称。
某些格式设置选项可用于更改这些标签的显示方式。

***class pptx.chart.axis.TickLabels***
一个服务类，提供对轴刻度标记标签格式的访问。

- font
Font提供访问这些刻度标签的文本属性的对象，例如粗体，斜体等。

- number_format
读/写字符串（例如“ $＃，##  0.00”），指定该轴上数字的格式。
这些字符串的语法与PowerPoint或Excel UI中显示的语法相同。
如果未设置数字格式，则返回“常规”。
请注意，当number_format_is_linked()is 时，此格式字符串对渲染的刻度标签不起作用True。
为该属性分配格式字符串会自动设置 number_format_is_linked()为False。

- number_format_is_linked
读/写布尔值，指定是否应从源电子表格中获取数字格式，而不是的值 number_format()。

- offset
读/写int值，范围为0-1000，指定刻度线标签和轴之间的间距，
以默认值的百分比表示。如果没有标签偏移设置，则为100。

#  _BasePlot对象
甲情节是一组系列的所有使用相同的图表类型，例如棒，柱，线等描绘大多数图表仅具有单个曲线图; 
但是，一个图表可能有多个，就像在同一图表中的线形图叠加在条形图上一样。在Microsoft API中，
此概念具有名称图表组。为python-pptx选择了术语图，以避免将图表组理解为一组图表对象的常见错误。
必须在绘图级别设置某些属性。所有这些图表类型的图上都不存在其中某些属性。
例如，gap_width 仅出现在条形图或柱形图上。

***class pptx.chart.plot._BasePlot***
在图表的绘图区域中显示的独特绘图。一张图表可能有多个图，
在这种情况下，它们会显示为叠加的图层，例如在条形图的顶部出现折线图。

- categories
返回一个Categories序列对象，其中包含Category与该图相关联的每个类别标签的对象。
本Category类派生从 str，所以返回的值，
所有你需要的是在它们出现在图上的顺序标签被视为对于通常的情况简单的字符串序列。
Categories在需要时提供用于处理层次结构类别的其他属性。

- chart
Chart包含该图的对象。

- data_labels
DataLabels 实例提供与该图关联的数据标签集合的属性和方法。

- has_data_labels
True如果该系列具有数据标签，则读/写布尔值。
分配 True导致将数据标签添加到绘图中。
分配False会删除所有现有的数据标签。

- series
的序列Series代表在该地块的一系列的对象，他们的顺序出现的情节。

- vary_by_categories
读/写布尔值，指定是否对该图中的每个点使用不同的颜色。
仅在单个系列时有效；当出现多个系列时，
PowerPoint会按系列自动更改颜色。

#  BarPlot对象
以下属性仅出现在条形图上，包括条形图和柱形图。

***class pptx.chart.plot.BarPlot***
条形图样式的图。

- gap_width
每个类别的条之间的间隙宽度，以条宽度的整数百分比表示。
新条形图的默认值为150，表示单个条形图宽度的150％或1.5倍。

- overlap
读/写int值，范围为-100..100，该值指定条形宽度的百分比，
通过该百分比可以重叠多系列条形图中的相邻条形。
默认值为0。设置为-100会创建整个条形宽度的间隙，
设置为100会使类别中的所有条形重叠。
默认情况下，堆积条形图的重叠量为100。

#  BubblePlot对象
以下属性仅在气泡型图上存在。

***class pptx.chart.plot.BubblePlot***
气泡图图。

- bubble_scale
0到300之间的一个整数（包括0和300），
指示应显示气泡的默认大小的百分比。
分配 None产生与分配100相同的行为。

#  Categories对象
类别图Categories通过其.categories属性提供对对象的 访问。

***class pptx.chart.category.Categories***
一系列Category对象，每个对象代表图表上的类别标签。
提供用于处理层次结构类别的属性。

- depth
返回一个整数，该整数表示此类别集合中的层次结构级别数。
对于非分层类别，返回1；如果不存在类别，则返回0（通常意味着不存在序列）。

- flattened_labels
返回一个元组序列，每个元组都包含一个叶子类别的类别标签的扁平层次结构。
每个元组按父级->子级顺序排列，例如，叶子类别最后出现。
如果此类别集合不是分层的，则每个元组将仅包含叶类别标签。
如果该图没有序列（因此没有类别），则返回一个空的元组。('US', 'CA', 'San Francisco')

- levels
返回CategoryLevel表示此类别集合层次结构的对象序列。
如果类别集合不是分层的，即仅包含叶级别的类别，则序列为空。
级别从叶级别到根级别排序；因此第一级将包含与此类别集合相同的类别。

#  Category对象
***class pptx.chart.category.Category***
str的扩展，提供类别标签作为其字符串值，以及代表类别其他方面的其他属性。

- idx
返回一个整数，表示该类别的索引引用。
对于叶节点，索引标识类别。
对于父（或其他祖先）类别，索引指定祖先所包含的第一个叶子类别。

- label
以字符串形式返回此类别的标签。

#  CategoryLevel对象
***class pptx.chart.category.CategoryLevel***
Category代表分层类别集合中单个级别的对象序列。
仅当类别是分层的时才使用此对象，这意味着它们具有多个级别，而较高级别的类别将较低级别的类别分组。

#  DataLabels对象
甲数据标签是文本标签的特定数据点，通常与它的值，
从而允许指向不仅仅是视觉其标记与它的轴线相比较更清楚地进行解释。
甲DataLabels对象不是集合，如序列，并且它不提供访问个别数据点。
相反，它提供的属性允许立即格式化其范围内的所有数据标签。

***class pptx.chart.datalabel.DataLabels***
提供对绘图或系列数据标签属性的访问。
这不是集合，并且不提供对单个数据标签的访问。
通过Point对象访问单个标签。该对象的属性提供其范围内所有数据标签的控件格式。

- font
Font提供访问这些数据标签的文本属性的对象，例如粗体，斜体等。

- number_format
读/写字符串，用于指定这组数据标签上数字的格式。
如果未设置数字格式，则返回“常规”。
请注意，当number_format_is_linked()is 时，此格式字符串对呈现的数据标签无效True。
为该属性分配格式字符串会自动设置 number_format_is_linked()为False。

- number_format_is_linked
读/写布尔值，指定是否应从源电子表格中获取数字格式，而不是的值 number_format()。

- position
读/写XL_DATA_LABEL_POSITION枚举值，指定数据标签相对于其数据点的位置，
或者 None如果未指定位置。分配None使PowerPoint选择默认位置，默认位置因图表类型而异。

- show_category_name
读/写。当类别名称应出现在标签中时为真。

- show_legend_key
读/写。当数据标签显示图例色样本时为true。

- show_percentage
读/写。当数据标签显示百分比时为True。
此选项不适用于所有图表类型。百分比显示在极坐标图上，例如饼图和甜甜圈。

- show_series_name
读/写。当数据标签显示系列名称时为True。

- show_value
读/写。当label显示数据点的数值时为True。

***class pptx.chart.datalabel.DataLabel***
与单个数据点关联的数据标签。

- font
Font提供此数据标签文本格式的对象。
此字体对象用于自定义自动插入的文本的外观，例如数据点值。字体适用于整个数据标签。
自定义数据标签文本外观的更精细控制由字体对象在文本框中的运行控制。

- has_text_frame
返回True如果该数据标签具有文本框（这意味着它具有自定义数据标签文本），以及False其他。
分配True 会导致添加文​​本框（如果尚不存在）。分配 False会导致删除任何现有文本框架以及该文本框架中包含的所有文本。

- position
读/写XL_DATA_LABEL_POSITION成员，指定此数据标签相对于其数据点的位置，
或者None如果未指定位置。分配None使PowerPoint选择默认位置，默认位置因图表类型而异。

- text_frame
TextFrame 该数据标签的实例，包含数据标签的文本并提供对其文本格式属性的访问。

#  Series对象
甲系列是表示一组连贯跨过每个图表中的类别的观测数据的点的序列。
例如，在区域类别为“西部”，“东部”和“中西部”的图表上，
一个序列可能是“第一季度销售额”，其值分别为42、120和34。在这种情况下，该序列围绕着第一季度时间段。
通常，系列对象的类型（类）取决于图表类型。以下属性可用于所有类型的系列对象。

***class pptx.chart.series._BaseSeries***
BarSeries和其他系列类的基类。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

#  AreaSeries对象
这些属性在属于区域类型图的序列上可用，例如AREA_STACKED。

***class pptx.chart.series.AreaSeries***
属于面积图的数据点系列。

- data_labels
DataLabels 此系列的对象控制数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- points
该CategoryPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  BarSeries对象
这些属性在属于条形图的系列上可用。请注意，柱形图也是条形图。

***class pptx.chart.series.BarSeries***
属于条形图的数据点系列。

- invert_if_negative
True如果值小于零的点的填充应该不同于正值的填充。False不管柱的值如何，填充都应该相同。
当为时True，出现一个带有实心填充的条，并带有白色填充。在带有渐变填充的条中，渐变的方向相反，
例如，暗->亮而不是亮->暗。术语“转化”在这里应该被理解为“反转的方向的的填充渐变 ”。

- data_labels
DataLabels 此系列的对象控制数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- points
该CategoryPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  BubbleSeries对象
这些属性在属于气泡图的系列中可用。

***class pptx.chart.series.BubbleSeries***
属于气泡图的数据点系列。

- points
该BubblePoints对象提供对单个数据点对象的访问，
这些对象用于发现和调整数据点的格式和数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- iter_values（）
按照它们在图表上出现的顺序，生成此系列中的每个float Y值。
的值没有表示丢失的Y值（对应于空白Excel小区）。

- marker
该Marker系列的实例，提供对数据点标记属性（例如填充和线）的访问。
设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  LineSeries对象
这些属性在属于线型图的系列中可用。

***class pptx.chart.series.LineSeries***
属于折线图的数据点系列。

- smooth
读/写布尔值，指定是否使用曲线平滑来形成将该系列中的数据点连接成连续曲线的线。
如果为False，则使用一系列直线段连接这些点。

- data_labels
DataLabels 此系列的对象控制数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- marker
该Marker系列的实例，提供对数据点标记属性（例如填充和线）的访问。
设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- points
该CategoryPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  Marker对象
标记是一种小的形状（例如菱形或圆形），可以在线型图中“标记”由串行线连接的每个单独的数据点。

***class pptx.chart.marker.Marker
表示线型图表上的数据点标记，例如菱形或圆形。

- format
该ChartFormat标记的实例，提供对形状属性（例如填充和线条）的访问。

- size
2到72之间（包括2和72）的整数，指示此标记的大小（以磅为单位）。
值None表示未设置任何显式值，并且该大小是从更高级别的设置或PowerPoint默认值（可能为9）继承的。
分配将None删除任何显式分配的大小，从而导致该值被继承。

- element
该对象代理的lxml元素。

- style
XL_MARKER_STYLE枚举的成员，指示此标记的形状。
None如果未设置显式样式，则返回该样式，该样式对应于PowerPoint UI中的“自动”选项。

#  PieSeries对象
这些属性在属于饼图的系列中可用。

***class pptx.chart.series.PieSeries***
属于饼图的数据点系列。

- data_labels
DataLabels 此系列的对象控制数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- points
该CategoryPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  RadarSeries对象
这些属性在属于雷达图的系列中可用。

***class pptx.chart.series.RadarSeries***
属于雷达图的数据点系列。

- data_labels
DataLabels 此系列的对象控制数据标签。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- marker
该Marker系列的实例，提供对数据点标记属性（例如填充和线）的访问。
设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

- points
该CategoryPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

#  XySeries对象
这些属性在属于XY图的序列上可用。

***class pptx.chart.series.XySeries***
属于XY（散点）图的数据点序列。

- iter_values（）
按照它们在图表上出现的顺序，生成此系列中的每个float Y值。
的值没有表示丢失的Y值（对应于空白Excel小区）。

- points
该XyPoints对象提供对本系列中各个数据点的访问。

- values
只读。一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。

- format
该ChartFormat系列的实例，提供对形状属性（例如填充和线条）的访问。

- index
在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引 。

- marker
该Marker系列的实例，提供对数据点标记属性（例如填充和线）的访问。
设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。

- name
赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
它还在图例中显示为该系列的标签。

#  Point对象
XY或气泡图具有points提供对一系列Point对象的访问权限的属性。
该序列支持迭代，索引访问和len()。

***class pptx.chart.point.CategoryPoints***
提供访问单个Point对象的序列，每个对象代表指定类别系列中数据点的视觉属性。

***class pptx.chart.point.BubblePoints***
序列提供对BubbleSeries对象中各个数据点的访问。

***class pptx.chart.point.XyPoints***
序列提供对XySeries 对象中各个数据点的访问。

***class pptx.chart.point.Point***
提供对系列中单个数据点的属性的访问，
例如其标记的视觉属性以及其数据标签的文本和字体。

- data_label
DataLabel表示此数据点上的标签的对象。

- format
在ChartFormat提供对所述形状格式化此数据点的属性，如线和填充对象。

- marker
该Marker点的实例，提供对数据点标记的视觉属性（例如填充和线）的访问。
设置这些属性将覆盖在系列级别设置的任何值。
# Note
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation
from pptx.chart.chart import Chart
from pptx.chart.chart import ChartTitle
from pptx.chart.chart import Legend
from pptx.chart.axis import _BaseAxis
from pptx.chart.axis import CategoryAxis
from pptx.chart.axis import DateAxis
from pptx.chart.axis import AxisTitle
from pptx.chart.axis import ValueAxis 
from pptx.chart.axis import MajorGridlines 
from pptx.chart.axis import TickLabels
from pptx.chart.plot import _BasePlot
from pptx.chart.plot import BarPlot
from pptx.chart.plot import BubblePlot
from pptx.chart.category import Categories
from pptx.chart.category import Category
from pptx.chart.category import CategoryLevel 
from pptx.chart.datalabel import DataLabels 
from pptx.chart.datalabel import DataLabel
from pptx.chart.series import _BaseSeries
from pptx.chart.series import AreaSeries 
from pptx.chart.series import BarSeries 
from pptx.chart.series import BubbleSeries
from pptx.chart.series import LineSeries 
from pptx.chart.marker import Marker 
from pptx.chart.series import PieSeries 
from pptx.chart.series import RadarSeries
from pptx.chart.series import XySeries
from pptx.chart.point import CategoryPoints
from pptx.chart.point import BubblePoints
from pptx.chart.point import XyPoints
from pptx.chart.point import Point
from pptx.enum.chart import XL_TICK_MARK
from pptx.enum.chart import XL_TICK_LABEL_POSITION
from pptx.enum.chart import XL_AXIS_CROSSES
from pptx.enum.chart import XL_LABEL_POSITION


#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回通过索引slides中的第四个对象
slide = slides[3]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  该Chart对象是组成对象的一般分层图的根，
#  这些图共同提供对指定和设置图表格式所需的属性和方法的访问。
chart = Chart

#  此图表的类别轴。 对于XY或气泡图，这是X轴。 
#  如果未定义类别轴，则引发ValueError（例如，饼图的情况）。
category_axis = chart.category_axis

#  用于格式化此图表的图表样式的读/写整数索引。 
#  范围是1到48。如果未分配任何显式样式，
#  则值为None（在这种情况下，将使用默认图表样式）。 
#  分配无将导致删除任何显式设置。 
#  整数索引对应于PowerPoint UI中图表样式库中样式的位置。
chart.chart_style = 1
chart_style = chart.chart_style

#  提供对标题属性访问的ChartTitle对象。
#  调用这个属性是破坏性的，因为它会向图表XML添加一个图表标题元素(c:title)，
#  如果还没有这个元素的话。使用has_title无损地测试图表标题是否存在。
chart_title = chart.chart_title

#  只读XL_CHART_TYPE枚举值，指定此图表的类型。 
#  如果图表有两个图，例如在条形图上叠加了一个线图，
#  则报告的类型适用于第一个（最后一个）图。
chart_type = chart.chart_type

#  此图表的默认字体对象控制文本格式。
font = chart.font

#  读/写布尔值，如果图表有图例，则为True。 
#  如果指定为True，则会将图例添加到图表（如果没有）。 
#  分配False会删除所有现有的图例定义以及任何现有的图例设置。
chart.has_legend = True
has_legend = chart.has_legend

#  读/写布尔值，指定此图表是否具有标题。
#  分配True会导致添加标题（如果尚不存在）。 
#  分配为False会删除所有现有标题及其文本和设置。
chart.has_title = True
has_title = chart.has_title

#  一个Legend对象，提供对该图表的图例属性的访问。
legend = chart.legend

#  此图中的绘图顺序。 图表在Microsoft API中称为图表组，
#  是在特定图表类型中描绘的一个或多个系列的不同序列。 
#  例如，如果一个图表的序列绘制为一条线，而三个序列绘制为列，
#  则该图表将具有两个图。 第一个对应于三列系列，第二个对应于线系列。 
#  绘图按绘制顺序排序，即从最后到最前。 支持len（），
#  成员资格（例如，图中的p），迭代，
#  切片和索引访问（例如，plot = plots [i]）。
plots = chart.plots

#  使用ChartData对象chart_data中的类别和系列值
#  替换此图表的XML和Excel工作表中的类别和系列值。
replace_data = chart.replace_data

#  一个SeriesCollection对象，它包含此图表中的所有系列。 
#  当图表具有多个图时，第一个图的所有序列出现在第二个图的所有序列之前，依此类推。 
#  绘图中的系列具有明确的顺序，并按该顺序显示。
series = chart.series

#  通过ValueAxis对象可以访问此图表的值轴的属性。 
#  如果图表没有值轴，则引发ValueError。
value_axis = chart.value_axis

#  提供用于操纵图表标题的属性。
chart_title = ChartTitle

#  ChartFormat对象提供对行和填充格式的访问。
#  返回提供此图表标题的形状格式设置属性的ChartFormat对象，例如其线条颜色和填充。
format = chart_title.format

#  读/写布尔值，指定此标题是否具有文本框架。
#  如果此图表标题具有文本框，则返回True，否则返回False。 
#  分配True会导致添加文本框（如果尚不存在）。 
#  分配False会导致所有现有文本框架以及其文本和格式被删除。
chart_title.has_text_frame = True
has_text_frame = chart_title.has_text_frame

#  此图表标题的TextFrame实例。
#  返回一个TextFrame实例，
#  该实例允许对该图表标题的文本及其文本格式设置属性进行读/写访问。 
#  从某种意义上说，如果不存在该属性，则访问该属性会破坏性。 
#  使用has_text_frame可以非破坏性地测试文本框架的存在。
text_frame = chart_title.text_frame

#  在图表中表示图例。 
#  一张图表最多可以包含一个图例。
legend = Legend

#  Font对象，用于访问此图例的文本属性，例如粗体，斜体等。
font = legend.font

#  从图例的默认值调整图例的x位置。 
#  表示为-1.0和1.0之间的浮点数，表示图表宽度的一部分。 
#  负值将图例向左移动，正值将其向右移动。 如果未指定任何设置，则为None。
horz_offset = legend.horz_offset

#  如果图例应位于绘图区域内，则为true。
#  读/写布尔值，指定是否应在图例区域内放置图例。 
#  在许多情况下，这将使其叠加在图表本身上。 
#  为该属性分配None将导致删除所有c：overlay元素，其解释与True相同。 
#  很少需要这种用例，建议分配一个布尔值。
legend.include_in_layout = True
include_in_layout = legend.include_in_layout

#  读/写XL_LEGEND_POSITION枚举值，指定要在其中放置图例的图表的常规区域。
legend.position = True
position = legend.position

#  图表轴对象的基类。 所有轴对象共享这些属性。
base_axis = _BaseAxis

#  提供对标题属性的访问的AxisTitle对象。
#  调用此属性具有破坏性，因为该属性会在轴XML中添加轴标题元素（c：title）（如果尚不存在）。 
#  使用has_title可无损地测试轴标题的存在。
axis_title = base_axis.axis_title

#  通过ChartFormat对象可以访问此轴的形状格式设置属性，例如其线条颜色和填充。
format = base_axis.format

#  读/写布尔值，指定此轴在其主要刻度线位置处是否具有网格线。 
#  将True分配给此属性将导致显示主要网格线。 分配False会导致将其删除。
base_axis.has_major_gridlines = True
has_major_gridlines = base_axis.has_major_gridlines

#  读/写布尔值，指定此轴在其次刻度线位置是否具有网格线。 
#  将True分配给此属性将导致显示较小的网格线。 分配False会导致将其删除。
base_axis.has_minor_gridlines = True
has_minor_gridlines = base_axis.has_minor_gridlines

#  读/写布尔值，指定此轴是否具有标题。
#  如果该轴具有标题，则为True，否则为False。 
#  分配True会导致添加轴标题（如果尚不存在）。 
#  分配False会导致任何现有标题被删除。
base_axis.has_title = True 
has_title = base_axis.has_title

#  MajorGridlines对象，表示该轴的主要网格线。
major_gridlines = base_axis.major_gridlines

#  读/写XL_TICK_MARK值，指定要在此轴上显示的主要刻度线的类型。
base_axis.major_tick_mark = XL_TICK_MARK.INSIDE
major_tick_mark = base_axis.major_tick_mark

#  读/写浮点值，指定该轴的值范围的上限，分别是垂直或水平值刻度的顶部或右侧的数字。 
#  值无表示上限应根据与轴关联的数据点值的范围自动确定。
base_axis.maximum_scale = 5
maximum_scale = base_axis.maximum_scale

#  读/写浮点值，指定值范围的下限，值刻度底部或左侧的数字。 
#  如果未设置最小刻度，则没有。 值无表示下限应根据与轴关联的数据点值的范围自动确定。
base_axis.minimum_scale = 7
minimum_scale = base_axis.minimum_scale

#  读/写XL_TICK_MARK值，指定该轴的次刻度线的类型。
base_axis.major_tick_mark = XL_TICK_MARK.INSIDE
minor_tick_mark = base_axis.minor_tick_mark

#  TickLabels实例提供对轴刻度标签格式属性的访问。 
#  刻度标签是出现在值轴上的数字或出现在类别轴上的类别名称。
tick_labels = base_axis.tick_labels

#  读/写XL_TICK_LABEL_POSITION值，指定该轴的刻度标签应出现的位置。
base_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
tick_label_position = base_axis.tick_label_position

#  读/写。 如果轴可见，则为True，否则为False。
base_axis.visible = True
visible = base_axis.visible

#  图表的类别轴。
category_axis = CategoryAxis

#  XL_CATEGORY_TYPE的成员，指定此轴的比例类型。 
#  对CategoryAxis对象无条件CATEGORY_SCALE。
category_type = category_axis.category_type

date_axis = DateAxis
#  具有日期作为其类别标签的类别轴，并且具有一些特殊的显示行为，
#  例如，使等长的时间相等，并且使月份开始日期归一化，尽管月份长度不相等。

#  XL_CATEGORY_TYPE的成员，指定此轴的比例类型。 
#  对于DateAxis对象，无条件TIME_SCALE。
category_type = date_axis.category_type

#  提供用于操纵轴标题的属性。
axis_title = AxisTitle

#  ChartFormat对象提供对形状格式的访问。
#  返回提供该轴标题的形状格式设置属性的ChartFormat对象，例如其线条颜色和填充。
format = axis_title.format

#  读/写布尔值，指定是否存在文本框架。
#  如果此轴标题具有文本框架，则返回True，否则返回False。 
#  分配True会导致添加文本框（如果尚不存在）。 
#  赋值为False会导致删除任何现有文本框架以及该文本框架中包含的所有文本。
axis_title.has_text_frame = True
has_text_frame = axis_title.has_text_frame

#  此轴标题的TextFrame实例。返回一个TextFrame实例，
#  该实例允许对该轴标题的文本及其文本格式设置属性进行读/写访问。 
#  访问此属性具有破坏性，因为它会添加新的文本框（如果尚不存在）。
text_frame = axis_title.text_frame

#  具有连续（相对于离散）值的轴。 纵轴通常是值轴，但是XY型图表的两个轴都是值轴。
value_axis = ValueAxis

#  XL_AXIS_CROSSES枚举的成员，
#  指定该轴上另一个轴与之交叉的点，例如自动/零，最小或最大。 
#  当定义了特定的数字交叉点（例如1.5）时，返回XL_AXIS_CROSSES.CUSTOM。
value_axis.crosses = XL_AXIS_CROSSES.MAXIMUM
crosses = value_axis.crosses

#  垂直轴相交的轴上的数值。 如果未设置交叉值，则返回None。
value_axis.crosses_at = 10
crosses_at = value_axis.crosses_at

#  该值轴上主要刻度线之间的浮点数。 “无”对应于UI中的“自动”设置，
#  并指定该值应由PowerPoint根据基础图表数据进行计算。
value_axis.major_unit = 1
major_unit = value_axis.major_unit

#  该值轴上次刻度线之间的浮点数。 “无”对应于UI中的“自动”设置，
#  并指定该值应由PowerPoint根据基础图表数据进行计算。
value_axis.minor_unit = 1
minor_unit = value_axis.minor_unit

#  提供对出现在轴上的主要网格线属性的访问。
major_gridlines = MajorGridlines

#  通过ChartFormat对象可以访问此数据点的形状格式属性，例如线条和填充。
format = major_gridlines.format

#  一个服务类，提供对轴刻度标记标签格式的访问。
tick_labels = TickLabels

font = tick_labels.font

#  指定该轴上数字格式的读/写字符串（例如“ $＃，##  0.00”）。 
#  这些字符串的语法与PowerPoint或Excel UI中显示的语法相同。 
#  如果未设置数字格式，则返回“常规”。 
#  请注意，当number_format_is_linked（）为True时，
#  此格式字符串对渲染的刻度标签无效。 
#  为该属性分配格式字符串会自动将number_format_is_linked（）设置为False。
tick_labels.number_format = '1.00'
number_format = tick_labels.number_format

#  读/写布尔值，指定是否应从源电子表格中获取数字格式，而不是number_format（）的值。
tick_labels.number_format_is_linked = True
number_format_is_linked = tick_labels.number_format 

#  读/写int值，范围为0-1000，指定刻度标记和轴之间的间距，以默认值的百分比表示。 
#  如果没有标签偏移设置，则为100。
tick_labels.offset = 100
offset = tick_labels.offset

#  在图表的绘图区域中显示的独特绘图。 一张图表可能有多个图，在这种情况下，
#  它们会显示为叠加的图层，例如在条形图的顶部出现折线图。
base_plot = _BasePlot

#  返回一个类别序列对象，该序列对象包含与此图关联的每个类别标签的类别对象。 
#  Category类是从str派生的，因此对于通常情况下返回的值可以视为简单的字符串序列，
#  在这种情况下，您需要的只是标签在图表上出现的顺序。 
#  类别在需要时提供了用于处理分层类别的其他属性。
categories = base_plot.categories

#  包含该图的Chart对象。
chart = base_plot.chart

#  DataLabels实例在与此图关联的数据标签集合上提供属性和方法。
data_labels = base_plot.data_labels

#  读/写布尔值，如果系列具有数据标签，则为True。 
#  分配True将导致将数据标签添加到绘图中。 
#  分配False会删除所有现有的数据标签。
base_plot.has_data_labels = True
has_data_labels = base_plot.has_data_labels

#  一系列Series对象，代表此图中的系列，顺序是它们在图中显示的顺序。
series = base_plot.series

#  读/写布尔值，指定是否对该图中的每个点使用不同的颜色。 
#  仅在单个系列时有效； 当出现多个系列时，PowerPoint会按系列自动更改颜色。
base_plot.vary_by_categories = True
vary_by_categories = base_plot.vary_by_categories

#  条形图样式的图。
bar_plot = BarPlot

#  每个类别的条之间的间隙宽度，以条宽度的整数百分比表示。 
#  新条形图的默认值为150，表示单个条形图宽度的150％或1.5倍。
bar_plot.gap_width = 160
gap_width = bar_plot.gap_width

#  读/写int值，范围为-100~100，该值指定条形宽度的百分比，
#  通过该百分比可以使多系列条形图中的相邻条形重叠。 
#  默认值为0。设置为-100会创建整个条形宽度的间隙，
#  设置为100会使类别中的所有条形重叠。 
#  默认情况下，堆积条形图的重叠量为100。
bar_plot.overlap = 100
overlap = bar_plot.overlap

#  气泡图。
bubble_plot = BubblePlot

#  0到300之间的一个整数（包括0和300），指示应显示气泡的默认大小的百分比。 
#  分配无产生与分配100相同的行为。
bubble_scale = bubble_plot.bubble_scale

#  一系列的类别对象，每个对象代表图表上的类别标签。 
#  提供用于处理层次结构类别的属性。
cate_gories = Categories

#  返回一个整数，该整数表示此类别集合中的层次结构级别数。 
#  对于非分层类别，返回1；如果不存在类别，则返回0（通常意味着不存在序列）。
depth = cate_gories.depth

#  返回一个元组序列，每个元组都包含一个叶子类别的类别标签的扁平层次结构。 
#  每个元组按父级->子级顺序排列，例如 （“ US”，“ CA”，“ San Francisco”），
#  最后显示叶子类别。 如果此类别集合不是分层的，则每个元组将仅包含叶类别标签。 
#  如果该图没有序列（因此没有类别），则返回一个空的元组。
flattened_labels = cate_gories.flattened_labels

#  返回表示该类别集合层次结构的CategoryLevel对象的序列。 
#  如果类别集合不是分层的，即仅包含叶级别的类别，则序列为空。 
#  级别从叶级别到根级别排序； 因此第一级将包含与此类别集合相同的类别。
levels = cate_gories.levels

#  str的扩展，提供类别标签作为其字符串值，以及代表类别其他方面的其他属性。
cate_gory = Category

#  返回一个整数，表示该类别的索引引用。 
#  对于页节点，索引标识类别。 
#  对于父（或其他祖先）类别，索引指定祖先所包含的第一页类别。
idx = cate_gory.idx

#  以字符串形式返回此类别的标签。
label = cate_gory.label

#  表示类别对象的序列，该对象表示层次结构类别集合中的单个级别。 
#  仅当类别是分层的时才使用此对象，这意味着它们具有多个级别，
#  而较高级别的类别将较低级别的类别分组。
cate_gory_level = CategoryLevel


#  提供对绘图或系列数据标签属性的访问。
#  这不是集合，并且不提供对单个数据标签的访问。 
#  通过Point对象访问单个标签。 
#  该对象的属性提供其范围内所有数据标签的控件格式。
data_labels = DataLabels

#  Font对象，用于访问这些数据标签的文本属性，例如粗体，斜体等。
font = data_labels.font

#  读/写字符串，用于指定这组数据标签上数字的格式。 
#  如果未设置数字格式，则返回“常规”。 
#  请注意，当number_format_is_linked（）为True时，
#  此格式字符串对呈现的数据标签无效。 
#  为该属性分配格式字符串会自动将number_format_is_linked（）设置为False。
data_labels.number_format = '1.00'
number_format = data_labels.number_format

#  读/写布尔值，指定是否应从源电子表格中获取数字格式，
#  而不是number_format（）的值。
data_labels.number_format_is_linked = True
number_format_is_linked = data_labels.number_format_is_linked

#  读/写XL_DATA_LABEL_POSITION枚举值，
#  指定数据标签相对于其数据点的位置；如果未指定位置，则为None。 
#  分配“无”会使PowerPoint选择默认位置，默认位置因图表类型而异。
data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
position = data_labels.position

#  读/写。 当类别名称应出现在标签中时为真。
data_labels.show_category_name = True
show_category_name = data_labels.show_category_name

#  读/写。 当数据标签显示图例色样本时为true。
data_labels.show_legend_key = True
show_legend_key = data_labels.show_legend_key

#  读/写。 当数据标签显示百分比时为True。
#  此选项不适用于所有图表类型。 百分比显示在极坐标图上，例如饼图和圆环图。
data_labels.show_percentage = True
show_percentage = data_labels.show_percentage

#  读/写。 当数据标签显示系列名称时为True。
data_labels.show_series_name = True
show_series_name = data_labels.show_series_name

#  读/写。 当label显示数据点的数值时为True。
data_labels.show_value = True
show_value = data_labels.show_value

#  与单个数据点关联的数据标签。
data_label = DataLabel

#  提供此数据标签文本格式的Font对象。
#  此字体对象用于自定义自动插入的文本的外观，例如数据点值。 
#  字体适用于整个数据标签。 
#  自定义数据标签文本外观的更精细控制由字体对象在文本框中的运行控制。
font = data_label.font

#  如果此数据标签具有文本框架（表示它具有自定义数据标签文本），
#  则返回True，否则返回False。 
#  分配True会导致添加文本框（如果尚不存在）。 
#  赋值为False会导致删除任何现有文本框架以及该文本框架中包含的所有文本。
has_text_frame = data_label.has_text_frame

#  读/写XL_DATA_LABEL_POSITION成员，指定此数据标签相对于其数据点的位置；
#  如果未指定位置，则为None。 
#  分配“无”会使PowerPoint选择默认位置，默认位置因图表类型而异。
data_label.position = XL_LABEL_POSITION.OUTSIDE_END
position = data_label.position

#  此数据标签的TextFrame实例，包含数据标签的文本，
#  并提供对其文本格式属性的访问。
text_frame = data_label.text_frame

#  BarSeries和其他系列类的基类。
baseSeries = _BaseSeries

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = baseSeries.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = baseSeries.index

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = baseSeries.name

#  属于面积图的数据点系列。
area_series = AreaSeries

#  DataLabels对象控制此系列的数据标签。
data_labels = area_series.data_labels

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = area_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = area_series.index

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = area_series.name

#  CategoryPoints对象提供对本系列中各个数据点的访问。
points = area_series.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = area_series.values

#  属于条形图的数据点系列。
bar_series = BarSeries

#  如果具有小于零值的点应出现的填充与具有正值的填充不同，则为true。
#  如果填充值应与条形值无关而相同，则为False。
#  设为True时，会出现一个带有白色填充的实心条；
#  在带有渐变填充的条中，渐变的方向相反，例如 深色->浅色而不是浅色->深色。
#  术语“反转”在这里应理解为意指“反转填充梯度的方向”。
invert_if_negative = bar_series.invert_if_negative

#  DataLabels对象控制此系列的数据标签。
data_labels = bar_series.data_labels

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = bar_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = bar_series.index

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = bar_series.name

#  CategoryPoints对象提供对本系列中各个数据点的访问。
points = bar_series.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = bar_series.values

#  属于气泡图的数据点系列。
bubble_series = BubbleSeries

#  BubblePoints对象提供对用于发现和调整数据点的格式和数据标签的单个数据点对象的访问。
points = bubble_series.points

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = bubble_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = bubble_series.index

#  按照它们在图表上出现的顺序，生成此系列中的每个float Y值。
#  无值表示缺少的Y值（对应于空白的Excel单元格）。
iter_values = bubble_series.iter_values

#  此系列的Marker实例，提供对数据点标记属性（例如填充和线）的访问。
#  设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。
marker = bubble_series.marker

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = bubble_series.name

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = bubble_series.values

#  属于折线图的数据点系列。
lineSeries = LineSeries

#  读/写布尔值，指定是否使用曲线平滑来形成将该系列中的数据点连接成连续曲线的线。
#  如果为False，则使用一系列直线段连接这些点。
smooth = lineSeries.smooth

#  DataLabels对象控制此系列的数据标签。
data_labels = lineSeries.data_labels

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = lineSeries.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = lineSeries.index

#  此系列的Marker实例，提供对数据点标记属性（例如填充和线）的访问。
#  设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。
marker = lineSeries.marker

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = lineSeries.name

#  CategoryPoints对象提供对本系列中各个数据点的访问。
points = lineSeries.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = lineSeries.values

#  表示线型图表上的数据点标记，例如菱形或圆形。
marker = Marker

#  此标记的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = marker.format

#  2到72之间（包括2和72）的整数，指示此标记的大小（以磅为单位）。
#  值None表示未设置任何显式值，并且大小是从更高级别的设置或PowerPoint默认值（可能为9）继承的。
#  分配无将删除任何显式分配的大小，从而导致该值被继承。
size = marker.size

#  该对象代理的lxml元素。
element = marker.element

#  XL_MARKER_STYLE枚举的成员，指示此标记的形状。
#  如果未设置任何显式样式（对应于PowerPoint UI中的“自动”选项），则返回None。
style = marker.style

#  属于饼图的数据点系列。
pie_series = PieSeries

#  DataLabels对象控制此系列的数据标签。
data_labels = pie_series.data_labels

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = pie_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = pie_series.index

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = pie_series.name

#  CategoryPoints对象提供对本系列中各个数据点的访问。
points = pie_series.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = pie_series.values

#  属于雷达图的数据点系列。
radar_series = RadarSeries

#  DataLabels对象控制此系列的数据标签。
data_labels = radar_series.data_labels

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = radar_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = radar_series.index

#  此系列的Marker实例，提供对数据点标记属性（例如填充和线）的访问。
#  设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。
marker = radar_series.marker

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。
#  它还在图例中显示为该系列的标签。
name = radar_series.name

#  CategoryPoints对象提供对本系列中各个数据点的访问。
points = radar_series.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = radar_series.values

#  这些属性在属于XY图的序列上可用。
xy_series = XySeries

#  按照它们在图表上出现的顺序，生成此系列中的每个float Y值。 
#  无值表示缺少的Y值（对应于空白的Excel单元格）。
iter_values = xy_series.iter_values

#  XyPoints对象提供对本系列中各个数据点的访问。
points = xy_series.points

#  只读。 一个序列，该序列包含该系列的浮点值，按它们在图表上出现的顺序。
values = xy_series.values

#  本系列的ChartFormat实例，提供对形状属性（例如填充和线条）的访问。
format = xy_series.format

#  在其c：ser / c：idx元素中报告的该系列的从零开始的整数索引。
index = xy_series.index

#  此系列的Marker实例，提供对数据点标记属性（例如填充和线）的访问。 
#  设置这些属性可以确定该系列中所有点的标记外观，这些标记不会被点级别的设置所覆盖。
marker = xy_series.marker

#  赋予该系列的字符串标签在Excel工作表中显示为该系列的列标题。 
#  它还在图例中显示为该系列的标签。
name = xy_series.name

#  提供访问单个Point对象的序列，每个对象代表指定类别系列中数据点的视觉属性。
category_points = CategoryPoints

#  序列提供对BubbleSeries对象中各个数据点的访问。
bubble_points = BubblePoints

#  序列提供对XySeries 对象中各个数据点的访问。
xy_points = XyPoints

#  提供对系列中单个数据点的属性的访问，例如其标记的视觉属性以及其数据标签的文本和字体。
point = Point

#  DataLabel表示此数据点上的标签的对象。
data_label = point.data_label

#  在ChartFormat提供对所述形状格式化此数据点的属性，如线和填充对象。
format = point.format

#  该Marker点的实例，提供对数据点标记的视觉属性（例如填充和线）的访问。设置这些属性将覆盖在系列级别设置的任何值。
marker = point.marker

print marker
```
