---
title: Python-pptx-Shapes
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-4949e09bae8c6175.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# SlideShapes对象
SlideShapes对象是Slide的形状属性。
**class pptx.shapes.shapetree.SlideShapes**
形状顺序出现在幻灯片上。
序列中的第一个形状是z顺序中的最后一个形状，最后一个形状是最顶部。
支持索引访问，len()，index()和迭代。

- add_chart(chart_type，x，y，cx，cy，chart_data )
> 将新的chart_type图表添加到幻灯片。
图表位于(x，y)，大小为(cx，cy)，并描述了chart_data。
chart_type是XL_CHART_TYPE 枚举值之一。
chart_data是一个ChartData对象，其中填充了图表的类别和系列值。
注意，返回的是GraphicFrame形状对象，而不是该图形框架形状中包含的图表对象。
可以使用chart返回GraphicFrame对象的属性 访问图表对象。

- add_connector(connector_type，begin_x，begin_y，end_x，end_y )
> 将一个新创建的连接器形状添加到此形状树的末尾。
connector_type是MSO_CONNECTOR_TYPE 枚举的成员，并且端点值指定为EMU值。
返回的连接器的类型为connector_type，并且具有指定的起点和终点。

- add_group_shape(shapes = [] )
> 返回新附加到此形状树的GroupShape对象。
组形状为空，必须使用其形状树上的方法填充形状，该方法可通过其.shapes属性获得。
组形状的位置和范围由其包含的形状决定；每次添加形状时都会重新计算其位置和范围。

- add_movie(movie_file，left，top，width，height，poster_frame_image = None，mime_type ='video / unknown' )
> 返回在movie_file中显示视频的新添加的影片形状。
实验性的。此方法有重要限制：
1、必须指定尺寸;不会执行像add_picture()所提供的那样的自动伸缩。
2、应指定视频文件的MIME类型，例如“ video / mp4”。
3、所提供的视频文件的类型不会被询问。
缺省情况下，使用MIME类型video / unknown(在撰写本文时的测试中效果很好)。
4、必须提供海报框架图像，不能从视频文件中自动提取它。
如果未提供海报框，则将使用默认的“媒体扬声器”图像。
将新添加的影片形状返回到幻灯片，位于(左侧， 顶部)，大小(宽度，高度)并包含movie_file。
在视频开始播放之前，poster_frame_image将显示为视频的占位符。

- add_picture(image_file，left，top，width = None，height = None )
> 在image_file中添加显示图片的图片形状。
image_file可以是文件(字符串)的路径，也可以是类似文件的对象。
图片的左上角位于(top， left)。如果width和height都为None，则使用图像的原始大小。
如果仅使用宽度或高度之一，则将计算未指定的尺寸以保留图像的纵横比。
如果同时指定了两者，则将其拉伸以适合图像，而不考虑其原始纵横比。

- add_shape(autoshape_type_id，left，top，width，height )
> 返回附加到此形状树的新形状对象。
autoshape_type_id是其成员MSO_AUTO_SHAPE_TYPE例如 MSO_SHAPE.RECTANGLE要被添加指定形状的类型。
其余参数指定新形状的位置和大小。

- add_table(rows，cols，left，top，width，height )
> 添加GraphicFrame含有指定数目的表对象行和COLS和指定的位置和大小。 
宽度在新表的各列之间平均分配。
同样，高度在各行之间均匀分布。
请注意，必须使用.table返回的GraphicFrame形状上的属性访问封闭的Table对象。

- add_textbox(left，top，width，height )
> 返回添加到此形状树的新添加的文本框形状。
文本框具有指定的大小，位于幻灯片上的指定位置。

- build_freeform(start_x = 0，start_y = 0，scale = 1.0 )
> 返回FreeformBuilder对象以指定自由形状。
> 可选的start_x和start_y参数指定局部坐标中的起始笔位置。
使用前将它们四舍五入到最接近的整数，并且每个默认值都为零。
可选的scale参数指定与滑动坐标(EMU)成比例的局部坐标的大小。
如果垂直比例尺与水平比例尺不同(局部坐标单位为“矩形”)，
则可以提供一对数值作为 比例尺参数，例如scale =(1.0，2.0)。
在这种情况下，第一个数字解释为水平(X)比例尺，第二个数字解释为垂直(Y)比例尺。
一种方便的比例尺计算方法是将Length 对象除以等效数量的局部坐标单位。
例如， 每英寸1000个局部单位的比例尺= Inches(1)/ 1000。

- element
> 该对象代理的lxml元素。

- index(形状)
> 按此顺序返回形状索引。
如果形状不在集合中，则引发ValueError。

- parent
> 此对象的祖先代理对象。例如，形状的父级通常SlideShapes是包含它的对象。

- part
> 包含此对象的包装部件

- placeholders
> SlidePlaceholders在此幻灯片中包含占位符形状序列的实例。

- title
> 幻灯片上的标题占位符形状，或者None幻灯片上没有标题占位符时。

- turbo_add_enabled
> 如果启用了“涡轮添加”模式，则为true。 读/写。
实验性：向幻灯片添加大量（数百种形状）时，此功能可以从根本上改善性能。 
它通过缓存使用的上一个形状ID并递增该值来分配下一个形状ID来工作。 
这样可以避免在每次需要新的ID时重复搜索幻灯片中的所有形状ID。
对于形状相对较少的幻灯片，性能并未得到明显改善，
但是由于搜索时间随形状数的平方增加，
因此此选项对于优化由许多形状组成的幻灯片的生成可能很有用。
如果使用多个幻灯片对象与演示文稿中的同一张幻灯片进行交互，
则可能发生Shape-id碰撞（导致加载时发生修复错误）。 
请注意，每次访问幻灯片时，Slides集合都会创建一个新的Slide对象
例如，slide = prs.slides [0]，因此您必须注意将其限制为单个Slide对象。

# GroupShapes对象
GroupShapes遇到的对象是的shapes 属性GroupShape。
**class pptx.shapes.shapetree.GroupShapes**
属于组形状的子形状的序列。
请注意，此集合本身可以包含组形状，从而使该部分成为递归树数据结构(非循环图)。

- add_chart(chart_type，x，y，cx，cy，chart_data )
> 将新的chart_type图表添加到幻灯片。
图表位于(x，y)，大小为(cx，cy)，并描述了chart_data。
chart_type是XL_CHART_TYPE 枚举值之一。
chart_data是一个ChartData对象，其中填充了图表的类别和系列值。
请注意，将GraphicFrame返回一个形状对象，
而不是该Chart 图形框架形状中包含的对象。
可以使用chart返回GraphicFrame对象的属性 访问图表对象。

- add_connector(connector_type，begin_x，begin_y，end_x，end_y )
> 将一个新创建的连接器形状添加到此形状树的末尾。
connector_type是MSO_CONNECTOR_TYPE 枚举的成员，并且端点值指定为EMU值。
返回的连接器的类型为connector_type，并且具有指定的起点和终点。

- add_group_shape(shapes = [] )
> 返回新附加到此形状树的GroupShape对象。
组形状为空，必须使用其形状树上的方法填充形状，该方法可通过其.shapes属性获得。
组形状的位置和范围由其包含的形状决定；每次添加形状时都会重新计算其位置和范围。

- add_picture(image_file，left，top，width = None，height = None )
> 在image_file中添加显示图片的图片形状。
image_file可以是文件(字符串)的路径，也可以是类似文件的对象。
图片的左上角位于(top， left)。如果width和height都为None，则使用图像的原始大小。
如果仅使用宽度或高度之一，则将计算未指定的尺寸以保留图像的纵横比。
> 如果同时指定了两者，则将其拉伸以适合图像，而不考虑其原始纵横比。

- add_shape(autoshape_type_id，left，top，width，height )
> 返回附加到此形状树的新形状对象。
autoshape_type_id是其成员MSO_AUTO_SHAPE_TYPE
例如 MSO_SHAPE.RECTANGLE要被添加指定形状的类型。
其余参数指定新形状的位置和大小。

- add_textbox(left，top，width，height )
> 返回添加到此形状树的新添加的文本框形状。
文本框具有指定的大小，位于幻灯片上的指定位置。

- build_freeform(start_x = 0，start_y = 0，scale = 1.0 )
> 返回FreeformBuilder对象来指定一个freeform形状。
可选的start_x和start_y参数指定局部坐标中的起始笔位置。
使用前将它们四舍五入到最接近的整数，并且每个默认值都为零。
可选的scale参数指定与滑动坐标(EMU)成比例的局部坐标的大小。
如果垂直比例尺与水平比例尺不同(局部坐标单位为“矩形”)，
则可以提供一对数值作为 比例尺参数。例如scale =(1.0，2.0)。
在这种情况下，第一个数字解释为水平(X)比例尺，第二个数字解释为垂直(Y)比例尺。
一种方便的比例尺计算方法是将Length 对象除以等效数量的局部坐标单位。
例如， 每英寸1000个局部单位的比例尺= Inches(1)/ 1000。

- element
> 该对象代理的lxml元素。

- index(shape)
> 按此顺序返回形状索引。
如果形状不在集合中，则引发ValueError。

- parent
> 此对象的祖先代理对象。例如，形状的父级通常SlideShapes是包含它的对象。

- part
> 包含此对象的包装部件

- turbo_add_enabled
> 如果启用了“涡轮添加”模式，则为true。 读/写。
实验性：向幻灯片添加大量（数百种形状）时，此功能可以从根本上改善性能。 
它通过缓存使用的上一个形状ID并递增该值来分配下一个形状ID来工作。 
这样可以避免在每次需要新的ID时重复搜索幻灯片中的所有形状ID。
对于形状相对较少的幻灯片，性能并未得到明显改善，
但是由于搜索时间随形状数的平方增加，
因此此选项对于优化由许多形状组成的幻灯片的生成可能很有用。
如果使用多个幻灯片对象与演示文稿中的同一张幻灯片进行交互，
则可能发生Shape-id碰撞（导致加载时发生修复错误）。 
请注意，每次访问幻灯片时，Slides集合都会创建一个新的Slide对象
例如，slide = prs.slides [0]，因此您必须注意将其限制为单个Slide对象。

# 一般形状对象
以下属性和方法是所有形状共有的。
**class pptx.shapes.base.BaseShape**
形状对象的基类。
子类包括Shape，Picture，和GraphicFrame。

- click_action
> 提供对单击行为的访问的Actionset实例。
单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
单击操作是在整个形状上定义的，而不是在形状内的文本运行。
即使在形状上没有定义单击行为，也总是返回Actionset对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- has_chart
> 如果此形状是包含图表对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.chart属性访问图表对象。

- has_table
> 如果此形状是包含表格对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.table属性访问表对象。

- has_text_frame
> True 如果此形状可以包含文本。

- height
> 读/写。EMU中形状的顶部和底部范围之间的整数距离

- is_placeholder
> 如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- name
> 形状的名称，例如“图片7”

- placeholder_format
> 一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat 提供访问此形状阴影的对象。
一个ShadowFormat对象总是返回，即使没有影子明确对这种形状定义(即它继承了它的身影行为)。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> 标识此形状类型的唯一整数，例如 MSO_SHAPE_TYPE.CHART。必须由子类实现。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。此形状左右范围之间的整数距离，以英制公制单位(EMU)

# Shape对象(自选图形)
为自选图形定义了以下属性和方法，其中包括文本框和占位符。
**class pptx.shapes.autoshape.Shape**
可以出现在幻灯片上的形状。
对应于<p:sp>可以出现在任何幻灯片类型的部分中的元素(slide，slideLayout，slideMaster，notesPage，notesMaster，handoutMaster)。

- adjustments
> AdjustmentCollection对此实例的只读引用

- auto_shape_type
> 标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
如果此形状不是自动形状，则引发ValueError。

- fill
> FillFormat 此形状的实例，提供对填充属性(例如填充颜色)的访问。

- has_text_frame
> True如果此形状可以包含文本。始终True是自选图形。

- line
> LineFormat 该形状的实例，提供对线属性(如线颜色)的访问。

- shape_type
> 标识此形状类型的唯一整数，例如 MSO_SHAPE_TYPE.TEXT_BOX。

- text
> 读/写。形状文本的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
分配给文本将替换形状中先前包含的所有文本，
> 以及应用于该形状的任何段落或字体格式。
分配的文本中的换行符("\n")导致新段落开始。
> 分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。

- text_frame
> TextFrame 这种形状的实例。
包含形状的文本，并提供对文本格式设置属性的访问。

# AdjustmentCollection对象
自选图形的独特之处在于它可以进行调整，在PowerPoint用户界面中以小黄色菱形表示，
每个菱形均允许调整形状参数(例如箭头的角度)。
该AdjustmentCollection对象保存用于AutoShape的这些调整值，
每个调整值都是一个Adjustment实例。
AdjustmentCollection使用Shape.adjustments属性(只读)访问AutoShape 的实例 。
**class pptx.shapes.autoshape.AdjustmentCollection**(prstGeom )
Adjustment自动形状的实例序列，每个实例代表其形状的可用调整。
支持len()和索引访问，例如。shape.adjustments[1] = 0.15

# Adjustment对象
**class pptx.shapes.autoshape.Adjustment**(name，def_val，actual = None )
自动调整形状的调整值。调整值对应于自动形状上调整手柄的位置。
调整手柄是出现在某些自动形状上的黄色菱形小手柄，可以调整形状的轮廓。
例如，一个圆角矩形具有一个调整手柄，可以调整其圆角倒角的半径。
值float通常为0.0到1.0，尽管在某些情况下该值可以为负或大于1.0。

- effective_value
> 读/写float表示此调整的标准化调整值。实际值是一个大的整数，用形状坐标表示，
名义上在0到100,000之间。有效值被标准化为名义上介于0.0和1.0之间的相应值。
从直觉上讲，它表示形状的宽度或高度的比例，调整值从其起点开始位于该位置。
对于简单的形状(例如圆角矩形)，此直观的对应关系成立。
对于更复杂的形状和更极端的形状比例(例如，宽度远大于高度)，该值可以变为负数或大于1.0。

- val
> 非规格化的有效值(以形状坐标表示)，适合在XML中使用。

# Connector对象
为连接器形状定义了以下属性和方法：
**class pptx.shapes.connector.Connector**
连接器(线)的形状。
连接器为线性形状，其端点可以连接到其他对象(但不能连接到其他连接器)。
连接器可以是直的，有弯头的，也可以是弯曲的。

- begin_connect(shape，cxn_pt_idx )
> 实验 - 当前的实现仅适用于矩形形状，例如图片和矩形。
与其他形状类型一起使用时，如果cxn_pt_idx超出了所连接形状上可用的连接点数量，
则可能导致所连接端点的视觉外观意外对齐，并可能导致加载错误。
就是说，快速测试应该可以揭示将这种方法与其他形状类型一起使用时的预期结果。
将此连接器的起点连接到cxn_pt_idx指定的连接点处的形状。
每个形状都有零个或多个连接点，并通过索引(从0开始)进行标识。
通常，形状的第一个连接点位于其边界框的顶部中心，并且从那里开始逆时针编号。
但是，这只是一个约定，可能会有所不同，尤其是对于非内置形状。

- begin_x
> 以英制公制单位(作为Length对象)返回此连接器起点的X位置。

- begin_y
> 以英制公制单位(作为Length对象)返回此连接器起点的Y位置。

- end_connect(shape，cxn_pt_idx )
> 实验 - 当前的实现仅适用于矩形形状，例如图片和矩形。
与其他形状类型一起使用时，如果cxn_pt_idx超出了所连接形状上可用的连接点数量，
则可能导致所连接端点的视觉外观意外对齐，并可能导致加载错误。
就是说，快速测试应该可以揭示将这种方法与其他形状类型一起使用时的预期结果。
将此连接器的末端连接到cxn_pt_idx指定的连接点处的形状。

- end_x
> 以英制公制单位(作为Length对象)返回此连接器端点的X位置。

- end_y
> 以英制公制单位(作为Length对象)返回此连接器端点的Y位置。

- line
> LineFormat 该连接器的实例。
提供对线条属性的访问，例如线条颜色，宽度和线条样式。

# FreeformBuilder对象
为FreeformBuilder对象定义了以下属性和方法。自由格式生成器用于创建具有自定义几何形状的形状：
**class pptx.shapes.freeform.FreeformBuilder**
允许指定和创建自由形状。
初始笔位置在结构上提供。从那里开始，使用连续的调用进行绘制以绘制线段。
可以通过调用该close()方法来关闭自由形状。
形状可以具有多个轮廓，在这种情况下，“减去”重叠区域。轮廓是从“移至”操作开始的一系列线段。
移动到的操作会自动插入到每个新的自由格式中。可以使用.move_to()方法插入其他移动 对象。

- add_line_segments(顶点，close = True )
> 在顶点的每个点上添加一条直线段。
顶点必须是(x，y)对(2元组)的可迭代对象。
使用前，每个x和y值均四舍五入为最接近的整数。
可选的 close参数确定生成的轮廓是 闭合的还是保持打开状态。
返回此FreeformBuilder对象，以便可以在链接调用中使用。

- convert_to_shape(origin_x = 0，origin_y = 0 )
> 返回相对于指定偏移量定位的新自由形状。
origin_x和origin_y可能通过使用Length对象在滑动坐标(EMU)中定位局部坐标系的原点。
请注意，可以多次调用此方法，以在幻灯片的不同位置添加相同几何形状的多个形状。

- move_to(x，y )
> 将笔移到(x，y)(局部坐标)而不画线。
返回此FreeformBuilder对象，以便可以在链接调用中使用。

# Picture对象
为图片形状定义了以下属性和方法。
**class pptx.shapes.picture.Picture**
图片形状，将图像放置在幻灯片上的形状。
基于p：pic元素。

- click_action
> 提供对单击行为的访问的Actionset实例。
单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
单击操作是在整个形状上定义的，而不是在形状内的文本运行。
即使在形状上没有定义单击行为，也总是返回Actionset对象。

- crop_bottom
> float 表示从形状底部裁剪的相对部分。
读/写。1.0代表100％。例如，25％用0.25表示。负值和大于1.0的值都是有效的。

- crop_left
> float 表示从形状左侧裁剪的相对部分。
读/写。1.0代表100％。负值将边延伸到图像边界之外。

- crop_right
> float 表示从形状右侧裁剪的相对部分。
读/写。1.0代表100％。

- crop_top
> float 表示从形状顶部裁剪的相对部分。
读/写。1.0代表100％。

- element
> 此形状的lxml元素，例如CT_Shape实例。
请注意，不当操作此元素可能会生成无效的演示文稿文件。如果使用它来更改基础XML，请确保您知道自己在做什么。

- has_chart
> 如果此形状是包含图表对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.chart属性访问图表对象。

- has_table
> 如果此形状是包含表格对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.table属性访问表对象。

- has_text_frame
> True 如果此形状可以包含文本。

- height
> 读/写。EMU中形状的顶部和底部范围之间的整数距离

- is_placeholder
> 如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- line
> 此形状的LineFormat实例，提供对线属性(如线颜色)的访问。

- name
> 形状的名称，例如“图片7”

- part
> 包含此形状的包装部件。
一个BaseSlidePart在这种情况下，子类。仅当您扩展python-pptx API对象的行为时，才需要访问幻灯片部分。

- placeholder_format
> 一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat 提供访问此形状阴影的对象。
一个ShadowFormat对象总是返回，即使没有影子明确对这种形状定义(即它继承了它的身影行为)。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。EMU中左右形状范围之间的整数距离

- auto_shape_type
> MSO_SHAPE的成员，指示遮罩形状。
PowerPoint中可用的任何所谓的“自动形状”(例如椭圆形或三角形)都可以掩盖图片。当图片被形状遮盖时，该形状采用与图片相同的尺寸，并且不会出现图片超出形状边界的部分。请注意，新插入图片的默认值为MSO_AUTO_SHAPE_TYPE.RECTANGLE，由于矩形的范围与图片的范围完全对应，因此不会进行裁剪。
可用的形状对应于MSO_AUTO_SHAPE_TYPE的成员 。
返回值也可以是None，表示图片没有几何形状(不期望)或具有自定义几何形状(如自由形状)。尽管没有几何图形，但是可以选择，但幻灯片上没有可见的图像。这是因为没有几何形状，就不会出现“内部形状”。

- image
> 一个Image对象，可以访问此图片形状中的图像的属性和字节。

- shape_type
> MSO_SHAPE_TYPE.PICTURE在这种情况下，无条件地标识此形状类型的唯一整数 。

# GraphicFrame对象
为图形框架形状定义了以下属性和方法。图形框架是包含表格，图表或智能艺术品的形状。

**class pptx.shapes.graphfrm.GraphicFrame**
基数： pptx.shapes.base.BaseShape
表格，图表，智能艺术品和媒体对象的容器形状。
对应<p:graphicFrame>于形状树中的一个元素。

- chart
> Chart在此图形框架中包含图表的对象。如果此图形框架不包含图表，则引发ValueError 。

- click_action
> 提供对单击行为的访问的Actionset实例。
单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
单击操作是在整个形状上定义的，而不是在形状内的文本运行。
即使在形状上没有定义单击行为，也总是返回Actionset对象。

- element
> 此形状的lxml元素，例如CT_Shape实例。
请注意，不当操作此元素可能会生成无效的演示文稿文件。如果使用它来更改基础XML，请确保您知道自己在做什么。

- has_chart
> 如果此形状是包含图表对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.chart属性访问图表对象。

- has_table
> 如果此形状是包含表格对象的图形框架，则为true。 否则为假。 
如果为True，则可以使用.table属性访问表对象。

- height
> 读/写。EMU中形状的顶部和底部范围之间的整数距离

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- name
> 形状的名称，例如“图片7”

- rotation
> 读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。

- shadow
> 无条件加薪NotImplementedError。
图形框架对象对阴影效果的访问是特定于内容的(即，对于图表，表格等而言是不同的)，并且尚未实现。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- table
> Table此图形框中包含的对象。如果此图形框架不包含表格，则引发ValueError 。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。EMU中左右形状范围之间的整数距离

# GroupShape对象
为组形状定义了以下属性和方法。组形状充当其他形状的容器。
注意：
组形状没有文本框架，也不能有一个。
组形状不能具有单击操作，例如超链接。
**class pptx.shapes.group.GroupShape**
基数： pptx.shapes.base.BaseShape
充当其他形状的容器的形状。

- click_action
> 无条件引发TypeError。
组形状不能具有单击动作或悬停动作。

- element
> 此形状的lxml元素，例如CT_Shape实例。
请注意，不当操作此元素可能会生成无效的演示文稿文件。如果使用它来更改基础XML，请确保您知道自己在做什么。

- has_text_frame
> 无条件的False。
组形状没有文本框，并且本身不能包含文本。这不会影响组包含的形状各自具有自己的文本的能力。

- height
> 读/写。EMU中形状的顶部和底部范围之间的整数距离

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- name
> 形状的名称，例如“图片7”

- part
> 包含此形状的包装部件。
一个BaseSlidePart在这种情况下，子类。仅当您扩展python-pptx API对象的行为时，才需要访问幻灯片部分。

- rotation
> 读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat 代表此组阴影效果的对象。
甲ShadowFormat对象总是返回，即使当没有阴影明确地在此组的形状(即，当组继承其影子的行为)所定义。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> MSO_SHAPE_TYPE的成员，用于标识此形状的类型。
在这种情况下，无条件MSO_SHAPE_TYPE.GROUP

- shapes
> GroupShapes 该组的对象。
该GroupShapes对象提供对组成员形状的访问，并提供添加新形状的方法。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。EMU中左右形状范围之间的整数距离

# Note
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation

#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回通过索引slides中的第三个对象
slide = slides[3]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from pptx.chart.data import ChartData
#  按英尺标准指定x，y值
x, y, cx, cy = Inches(0.5), Inches(1), Inches(4), Inches(3)  
#  图表data类 
chart_data = ChartData()
#  图表加入两栏
chart_data.categories = [u'A班级得分率', u'B班级得分率']  
#  在两栏分别填入数据
chart_data.add_series(u'得分率对比', (80.5, 60.5))  
#  将新的chart_type图表添加到幻灯片。
#  add_chart(图表类型，x、y表示图表位置，cx、cy表示图表宽高，并且插入chart_data中规定好的数据)
#  注意，返回的是GraphicFrame形状对象，而不是该图形框架形状中包含的图表对象。
#  可以使用返回的GraphicFrame对象的chart属性访问图表对象。
add_chart = shapes.add_chart(
	XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
)  

from pptx.enum.shapes import MSO_CONNECTOR
from pptx.util import Cm
#  将一个新创建的连接器形状添加到此形状树的末尾。
#  connector_type是MSO_CONNECTOR_TYPE 枚举的成员，并且端点值指定为EMU值。
#  返回的连接器的类型为connector_type，并且具有指定的起点和终点。
add_connector = shapes.add_connector(
	MSO_CONNECTOR.STRAIGHT, Cm(2), Cm(2), Cm(10), Cm(10)
)

#  返回GroupShape新添加到此形状树的对象。
#  组形状为空，必须使用其形状树上的方法填充形状，该方法可通过其.shapes属性获得。
#  组形状的位置和范围由其包含的形状决定；每次添加形状时都会重新计算其位置和范围。
add_group_shape = shapes.add_group_shape(shapes = [])

#  视频文件路径
movie_file = 'movie/1571365443211539.mp4'
#  预设位置及大小
left,top,width,height = Inches(5), Inches(1), Inches(4), Inches(3)  
#  海报框架图像，不能从视频文件中自动提取它。如果未提供海报框，则将使用默认的“媒体扬声器”图像。
poster_frame_image = 'image/bg2.jpg'
#  指定视频文件的MIME类型，例如“ video / mp4”。
#  所提供的视频文件的类型不会被询问。缺省情况下，使用MIME类型video / unknown。
mime_type = 'video / mp4'
#  返回在movie_file中显示视频的新添加的电影形状。
#  实验性的。此方法有重要限制：
#  必须指定大小；不add_picture()执行诸如提供的自动缩放。
#  应指定视频文件的MIME类型，例如“ video / mp4”。所提供的视频文件的类型不会被询问。
#  缺省情况下，使用MIME类型video / unknown。
#  必须提供海报框架图像，不能从视频文件中自动提取它。如果未提供海报框，则将使用默认的“媒体扬声器”图像。
#  将新添加的影片形状返回到幻灯片，位于(左侧， 顶部)，大小(宽度，高度)并包含movie_file。
#  在视频开始播放之前，poster_frame_image将显示为视频的占位符。
add_movie = shapes.add_movie(
	movie_file,left,top,width,height,poster_frame_image,mime_type
)

#  图片文件路径
image_file = 'image/bg1.jpg'
#  预设位置及大小
left,top,width,height = Inches(0.5), Inches(4), Inches(4), Inches(3) 
#  在image_file中添加显示图片的图片形状。
#  image_file可以是文件(字符串)的路径，也可以是类似文件的对象。图片的左上角位于(top， left)。
#  如果width和height都为None，则使用图像的原始大小。
#  如果仅使用宽度或高度之一，则将计算未指定的尺寸以保留图像的纵横比。
#  如果同时指定了两者，则将其拉伸以适合图像，而不考虑其原始纵横比。
add_picture = shapes.add_picture(
	image_file,left,top,width,height
)

from pptx.enum.shapes import MSO_SHAPE
#  autoshape_type_id是其成员MSO_AUTO_SHAPE_TYPE要被添加指定形状的类型
#  例如 MSO_SHAPE.RECTANGLE
autoshape_type_id = MSO_SHAPE.CHEVRON
#  预设位置及大小
left,top,width,height = Inches(5), Inches(4), Inches(4), Inches(3) 
#  返返回Shape附加到此形状树的新对象。
add_shape = shapes.add_shape(
	autoshape_type_id,left,top,width,height
)

#  返回通过索引slides中的第四个对象
slide = slides[4]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  表格的行列
rows,cols = 3,5
#  预设位置及大小
left,top,width,height = Inches(0.5), Inches(1), Inches(4), Inches(3) 
#  添加一个GraphicFrame对象，其中包含一个具有指定行数和cols以及指定位置和大小的表。
#  宽度均匀地分布在新表的列之间。同样地，高度均匀地分布在行之间。
#  请注意，必须使用返回的GraphicFrame形状上的.table属性来访问所包含的表对象。 
add_table = shapes.add_table(
	rows,cols,left,top,width,height 
)

#  预设位置及大小
left,top,width,height = Inches(5), Inches(1), Inches(4), Inches(3) 
add_textbox = shapes.add_textbox(
	left,top,width,height 
)

#  可选的start_x和start_y参数指定局部坐标中的起始笔位置。
#  使用前将它们四舍五入到最接近的整数，并且每个默认值都为零。
start_x,start_y = 100,200
#  可选的scale参数指定了与滑动坐标(EMU)成比例的局部坐标的大小。
#  如果垂直比例尺不同于水平比例尺(局部坐标单位为“矩形”)，可以提供一对数值作为scale参数，例如scale=(1.0, 2.0)。
#  在这种情况下，第一个数字被解释为水平(X)刻度，第二个数字被解释为垂直(Y)刻度。
#  计算比例的一个方便的方法是用一个长度对象除以一个等价的局部坐标单位，例如比例=英寸(1)/1000，对应1000个局部单位每英寸。
scale = (1.0,2.0)
#  返回FreeformBuilder对象来指定一个freeform形状。
build_freeform = shapes.build_freeform(
	start_x,start_y,scale
)

#  返回该对象代理的lxml元素。
element = shapes.element

#  遍历shapes
for shape in shapes:
	
	#  按此顺序返回形状索引。
	#  如果形状不在集合中，则引发ValueError。
	index = shapes.index(shape)

	pass

#  返回此对象的祖先代理对象
parent = shapes.parent

#  返回包含此对象的包装部件
part = shapes.part

#  返回幻灯片中包含占位符形状序列的slideplaceholder实例。
placeholders = shapes.placeholders

#  返回幻灯片上的标题占位符形状，如果幻灯片没有标题占位符，则为None。
title = shapes.title

#  如果启用了“涡轮添加”模式，则为true。 读/写。
#  实验性：向幻灯片添加大量（数百种形状）时，此功能可以从根本上改善性能。 
#  它通过缓存使用的上一个形状ID并递增该值来分配下一个形状ID来工作。 
#  这样可以避免在每次需要新的ID时重复搜索幻灯片中的所有形状ID。
#  对于形状相对较少的幻灯片，性能并未得到明显改善，
#  但是由于搜索时间随形状数的平方增加，
#  因此此选项对于优化由许多形状组成的幻灯片的生成可能很有用。
#  如果使用多个幻灯片对象与演示文稿中的同一张幻灯片进行交互，
#  则可能发生Shape-id碰撞（导致加载时发生修复错误）。 
#  请注意，每次访问幻灯片时，Slides集合都会创建一个新的Slide对象
#  例如，slide = prs.slides [0]，因此您必须注意将其限制为单个Slide对象。
turbo_add_enabled = shapes.turbo_add_enabled

#  ActionSetting 提供对点击行为的访问权限的实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(网页)或演示文稿中的另一张幻灯片。
#  单击动作是在整体形状上定义的动作，而不是形状内的一连串文字。一个ActionSetting对象总是返回，即使没有点击行为的形状定义。
click_action = shape.click_action

#  此形状的lxml元素，例如CT_Shape实例。
#  请注意，不当操作此元素可能会生成无效的演示文稿文件。
#  如果使用它来更改基础XML，请确保您知道自己在做什么。
element = shape.element

#  如果此形状是包含图表对象的图形框架，则为True。否则False。
#  如果为True，则可以使用.chart属性访问图表对象。
has_chart = shape.has_chart

#  如果此形状是包含表对象的图形框架，则为True。否则False。
#  为True时，可以使用.table属性访问表对象。
has_table =  shape.has_table

#  如果此形状可以包含文本，则为真。
has_text_frame = shape.has_text_frame

#  读/写。EMU中形状的顶部和底部范围之间的整数距离
shape.height = 2743100
height = shape.height

#  如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。
is_placeholder = shape.is_placeholder

#  读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)
shape.left = 4571000
left = shape.left

#  形状的名称，例如“图片7”
name = shape.name

#  一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。
#  如果形状不是占位符，则在访问时引发ValueError。
#  placeholder_format = shape.placeholder_format

#  读/写浮点数。顺时针旋转的度数。
#  可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。
shape.rotation = -45.0
rotation = shape.rotation

#  ShadowFormat 提供访问此形状阴影的对象。
#  一个ShadowFormat对象总是返回，即使没有影子明确对这种形状定义(即它继承了它的身影行为)。
shadow = shape.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = shape.shape_id

#  标识此形状类型的唯一整数，例如 MSO_SHAPE_TYPE.CHART。必须由子类实现。
shape_type = shape.shape_type

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)
shape.top = 914300
top = shape.top

#  读/写。EMU中左右形状区段之间的整数距离
shape.width = 3657500
width = shape.width

#  AdjustmentCollection对此实例的只读引用
adjustments = shape.adjustments

#  标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
#  如果此形状不是自动形状，则引发ValueError。
#  auto_shape_type = shape.auto_shape_type

#  此形状的FillFormat实例，提供对填充属性(如填充颜色)的访问。
fill = shape.fill

#  如果此形状可以包含文本，则为True。对于自动生成总是正确的。
has_text_frame = shape.has_text_frame

#  此形状的LineFormat实例，提供对线属性(如线颜色)的访问。
line = shape.line

#  标识此形状类型的唯一整数，例如 MSO_SHAPE_TYPE.TEXT_BOX。
shape_type = shape.shape_type

#  读/写。形状文本的Unicode (python3中的str)表示。
#  返回的字符串将包含一个换行符(“\n”)来分隔每个段落，并为形状的文本中的每个换行符(软回车)使用一个垂直制表符(“\v”)。
#  文本赋值将替换形状中先前包含的所有文本以及应用于其上的任何段落或字体格式。
#  指定文本中的换行字符(“\n”)将导致开始一个新段落。指定文本中的垂直制表符(“\v”)将导致插入换行符(软载波返回)。
#  (垂直制表符作为换行编码出现在从PowerPoint复制的剪贴板文本中。)
#  可以分配字节(python2str)或unicode (python3str)。
#  字节可以是7位ASCII或UTF-8编码的8位字节。
#  假设采用UTF-8编码(这也适用于ASCII)，则将字节值转换为unicode。
shape.text = 'HaI\'s text(中文)'
text = shape.text

#  此形状的TextFrame实例。
#  包含形状的文本，并提供对文本格式设置属性的访问。
text_frame = shape.text_frame


#  实验 - 当前的实现仅适用于矩形形状，例如图片和矩形。
#  与其他形状类型一起使用时，如果cxn_pt_idx超出了所连接形状上可用的连接点数量，
#  则可能导致所连接端点的视觉外观意外对齐，并可能导致加载错误。
#  就是说，快速测试应该可以揭示将这种方法与其他形状类型一起使用时的预期结果。
#  将此连接器的起点连接到cxn_pt_idx指定的连接点处的形状。
#  每个形状都有零个或多个连接点，并通过索引(从0开始)进行标识。
#  通常，形状的第一个连接点位于其边界框的顶部中心，并且从那里开始逆时针编号。
#  但是，这只是一个约定，可能会有所不同，尤其是对于非内置形状。
add_connector.begin_connect(
	shape,0
)

#  以英制公制单位(作为Length对象)返回此连接器起点的X位置。
begin_x = add_connector.begin_x

#  以英制公制单位(作为Length对象)返回此连接器起点的Y位置。
begin_y = add_connector.begin_y

#  实验 - 当前的实现仅适用于矩形形状，例如图片和矩形。
#  与其他形状类型一起使用时，如果cxn_pt_idx超出了所连接形状上可用的连接点数量，
#  则可能导致所连接端点的视觉外观意外对齐，并可能导致加载错误。
#  就是说，快速测试应该可以揭示将这种方法与其他形状类型一起使用时的预期结果。
#  将此连接器的末端连接到cxn_pt_idx指定的连接点处的形状。
add_connector.end_connect(
	shape,2
)

#  以英制公制单位(作为Length对象)返回此连接器端点的X位置。
end_x = add_connector.end_x

#  以英制公制单位(作为Length对象)返回此连接器端点的Y位置。
end_y = add_connector.end_y

#  此连接器的LineFormat实例。
#  提供对线属性(如线颜色、宽度和线样式)的访问。
line = add_connector.line

#  提供对单击行为的访问的actionset实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
#  单击操作是在整个形状上定义的，而不是在形状内的文本运行。
#  即使在形状上没有定义单击行为，也总是返回actionset对象。
click_action = add_picture.click_action

#  float 表示从形状底部裁剪的相对部分。
#  读/写。1.0代表100％。例如，25％用0.25表示。负值和大于1.0的值都是有效的。
add_picture.crop_bottom = 0.25
crop_bottom = add_picture.crop_bottom

#  float 表示从形状左侧裁剪的相对部分。
#  读/写。1.0代表100％。负值将边延伸到图像边界之外。
add_picture.crop_left = 0.25
crop_left = add_picture.crop_left

#  float 表示从形状右侧裁剪的相对部分。
#  读/写。1.0代表100％。
add_picture.crop_right = 0.25
crop_right = add_picture.crop_right


#  float 表示从形状右侧裁剪的相对部分。
#  读/写。1.0代表100％。
add_picture.crop_top = 0.25
crop_top = add_picture.crop_top

#  此形状的lxml元素，例如CT_Shape实例。
#  请注意，不当操作此元素可能会生成无效的演示文稿文件。
#  如果使用它来更改基础XML，请确保您知道自己在做什么。
element = add_picture.element

#  如果此形状是包含图表对象的图形框架返回True。 False除此以外。如果为True，则可以使用.chart属性访问图表对象。
has_chart = add_picture.has_chart

#  如果此形状是包含表格对象的图形框架返回True。 False除此以外。如果为True，则可以使用.table属性访问表对象。
has_table = add_picture.has_table

#  如果此形状可以包含文本返回True。
has_text_frame = add_picture.has_text_frame

#  读/写。EMU中形状的顶部和底部范围之间的整数距离
add_picture.height = 2743100
height = add_picture.height

#  如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。
is_placeholder = add_picture.is_placeholder

#  读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)
add_picture.left = 457100
left = add_picture.left

#  LineFormat的一个实例，提供对与此形状相邻的轮廓的属性(如颜色和宽度)的访问。
line = add_picture.line

#  形状的名称，例如“图片7”
name = add_picture.name

#  包含此形状的包装部件。
#  一个BaseSlidePart在这种情况下，子类。仅当您扩展python-pptx API对象的行为时，才需要访问幻灯片部分。
part = add_picture.part

#  一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。
#  如果形状不是占位符，则在访问时引发ValueError。
#  placeholder_format = add_picture.placeholder_format

#  读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。
add_picture.rotation = -45.0
rotation = add_picture.rotation

#  提供对该形状的阴影访问的ShadowFormat对象。
#  一个ShadowFormat对象总是被返回，即使在这个形状上没有明确定义阴影(也就是说它继承了它的阴影行为)。
shadow = add_picture.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = add_picture.shape_id

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)
add_picture.top = 3657500
top = add_picture.top

add_picture.width = 3657500
width = add_picture.width

#  MSO_SHAPE的成员，指示遮罩形状。
#  PowerPoint中可用的任何所谓的“自动形状”(例如椭圆形或三角形)都可以掩盖图片。
#  当图片被形状遮盖时，该形状采用与图片相同的尺寸，并且不会出现图片超出形状边界的部分。
#  请注意，新插入图片的默认值为MSO_AUTO_SHAPE_TYPE.RECTANGLE，由于矩形的范围与图片的范围完全对应，因此不会进行裁剪。
#  可用的形状对应于MSO_AUTO_SHAPE_TYPE的成员 。
#  返回值也可以是None，表示图片没有几何形状(不期望)或具有自定义几何形状(如自由形状)。
#  尽管没有几何图形，但是可以选择，但幻灯片上没有可见的图像。
#  这是因为没有几何形状，就不会出现“内部形状”。
auto_shape_type = add_picture.auto_shape_type

#  返回一个Image对象，可以访问此图片形状中的图像的属性和字节。
image = add_picture.image

#  返回唯一标识此形状类型的整数，无条件为MSO_SHAPE_TYPE。在这个例子中是图片。
shape_type = add_picture.shape_type

#  在此图形框架中包含图表的图表对象。如果此图形框架不包含图表，则引发ValueError错误。
chart = add_chart.chart

#  提供对单击行为的访问的actionset实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
#  单击操作是在整个形状上定义的，而不是在形状内的文本运行。
#  即使在形状上没有定义单击行为，也总是返回actionset对象。
click_action = add_chart.click_action

#  此形状的lxml元素，例如CT_Shape实例。
#  注意，不正确地操作这个元素可能会产生无效的表示文件。如果要使用它更改底层XML，请确保您知道自己在做什么。
element = add_chart.element

#  如果此图形框架包含一个图表对象，则为True。否则False。如果为True，则可以使用.chart属性访问图表对象。
has_chart = add_chart.has_chart

#  如果此图形框架包含表对象，则为True。否则False。为True时，可以使用.table属性访问表对象。
has_table = add_chart.has_table

#  读/写。EMU中形状的顶部和底部范围之间的整数距离
add_chart.height = 2743100
height = add_chart.height

#  读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)
add_chart.left = 457100
left = add_chart.left

#  形状的名称，例如“图片7”
name = add_chart.name

add_chart.rotation = -45.0
rotation = add_chart.rotation

#  无条件地引发了NotImplementedError。
#  对图形框架对象的阴影效果的访问是特定于内容的(例如，对图表、表格等的访问是不同的)，并且还没有实现。
#  shadow = add_chart.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = add_chart.shape_id

#  Table此图形框中包含的对象。如果此图形框架不包含表格，则引发ValueError。
#  table = add_chart.table

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)
add_chart.top = 914300
top = add_chart.top

#  读/写。EMU中左右形状范围之间的整数距离。
add_chart.width = 3657500
width = add_chart.width

#  无条件引发TypeError。
#  组形状不能具有单击动作或悬停动作。
#  click_action = add_group_shape.click_action

#  此形状的lxml元素，例如CT_Shape实例。
#  请注意，不当操作此元素可能会生成无效的演示文稿文件。如果使用它来更改基础XML，请确保您知道自己在做什么。
element = add_group_shape.element

#  无条件返回False
#  组形状没有文本框，并且本身不能包含文本。这不会影响组包含的形状各自具有自己的文本的能力。
has_text_frame = add_group_shape.has_text_frame

#  读/写。EMU中形状的顶部和底部范围之间的整数距离
add_group_shape.height = 1
height = add_group_shape.height

#  读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)
add_group_shape.left = 1
left = add_group_shape.left

#  形状的名称，例如“图片7”
name = add_group_shape.name

#  包含此形状的包装部件。
#  一个BaseSlidePart在这种情况下，子类。仅当您扩展python-pptx API对象的行为时，才需要访问幻灯片部分。
part = add_group_shape.part

#  读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。
add_group_shape.rotation = -45.0
rotation = add_group_shape.rotation

#  表示此组的阴影效果的阴影格式对象。
#  即使在此组形状上没有显式定义阴影(即当组继承其阴影行为时)，也总是返回ShadowFormat对象。
shadow = add_group_shape.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = add_group_shape.shape_id

#  MSO_SHAPE_TYPE的成员，用于标识此形状的类型。
#  在这种情况下，无条件MSO_SHAPE_TYPE.GROUP
shape_type = add_group_shape.shape_type

#  此组的GroupShapes对象。
#  GroupShapes对象提供对组成员形状的访问，并提供添加新成员形状的方法。
shapes = add_group_shape.shapes

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)
add_group_shape.top = 1
top = add_group_shape.top

#  读/写。EMU中左右形状区段之间的整数距离
add_group_shape.width = 1
width = add_group_shape.width
```
