---
title: Python-Python-pptx-Placeholders
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-a2b5b71faa4e923f.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# MasterPlaceholder对象
**Class pptx.shapes.placeholder.MasterPlaceholder**
幻灯片母版上的占位符形状。

- auto_shape_type
> 标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
如果此形状不是自动形状，则引发ValueError。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，
包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
即使未在形状上定义点击行为，也始终返回ActionSetting对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- fill
> 此形状的FillFormat实例，提供对填充属性(如填充颜色)的访问。

- has_text_frame
> 如果此形状可以包含文本，则为true。对于自选图形，始终为True。

- height
> 读/写。此形状的顶部和底部范围之间的整数距离，以英制公制单位(EMU)

- is_placeholder
> 如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- line
> 此形状的LineFormat实例，提供对线属性（如线颜色）的访问。

- name
> 形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
即使在此形状上未明确定义阴影，
也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- text
> 读/写。形状文本的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
分配给文本将替换形状中先前包含的所有文本，
以及应用于该形状的任何段落或字体格式。
分配的文本中的换行符("\n")导致新段落开始。
分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。

- text_frame
> 此形状的TextFrame实例。
包含形状的文本，并提供对文本格式设置属性的访问。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。此形状的左边缘到幻灯片右边缘的整数距离，以英制公制单位(EMU)

# LayoutPlaceholder对象
**Class pptx.shapes.placeholder.LayoutPlaceholder**
幻灯片布局上的占位符形状，为幻灯片布局占位符提供了不同的行为，
特别是当存在匹配的占位符时，从具有相同类型的主占位符继承形状属性。

# ChartPlaceholder对象
**Class pptx.shapes.placeholder.ChartPlaceholder**
只能接受图表的占位符形状。

- adjustments
> 对此实例(AdjustmentCollection)的只读引用

- auto_shape_type
> 标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
如果此形状不是自动形状，则引发ValueError。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，包括跳转到超链接(web页面)
或演示文稿中的另一张幻灯片。即使未在形状上定义点击行为，
也始终返回ActionSetting对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- fill
> 此形状的FillFormat实例，提供对填充属性(如填充颜色)的访问。

- get_or_add_ln()
> 返回<a：ln>元素，其中包含此形状的线格式属性XML。

- height
> 此占位符形状的有效高度；如果有，则为其直接应用的高度，
否则为其父布局占位符的高度。

- insert_chart(chart_type，chart_data )
> 返回一个PlaceholderGraphicFrame对象，
该对象包含一个新的chart_type图表，该图表描述了chart_data，
并且具有与此占位符相同的位置和大小。
chart_type是XL_CHART_TYPE枚举值之一。
chart_data是一个ChartData对象，其中填充了图表的类别和系列值。
请注意，新的Chart对象不会直接返回。
可以使用返回的PlaceholderGraphicFrame对象的chart属性访问该图表对象。

- is_placeholder
> 如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。

- left
> 此占位符形状的有效左边；如果有一个，则直接应用左侧；
否则，其父布局占位符的左侧。

- line
> 此形状的LineFormat实例，提供对线属性（如线颜色）的访问。

- ln
> <a：ln>元素，包含线条格式属性，例如线条颜色和宽度。
如果没有<a：ln>元素，则为None。

- name
> 形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
即使在此形状上未明确定义阴影，
也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> MSO_SHAPE_TYPE的成员，指定此形状的类型。
MSO_SHAPE_TYPE.PLACEHOLDER在这种情况下是无条件的。只读。

- text
> 读/写。形状文本的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
分配给文本将替换形状中先前包含的所有文本，
以及应用于该形状的任何段落或字体格式。
分配的文本中的换行符("\n")导致新段落开始。
分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。

- text_frame
> 此形状的TextFrame实例。
包含形状的文本，并提供对文本格式设置属性的访问。

- top
> 此占位符形状的有效顶部；如果有，则直接应用其顶部，
否则为其父布局占位符的顶部。

- width
> 此占位符形状的有效宽度；如果具有一个宽度，则为直接应用的宽度；
否则为其父布局占位符的宽度。

# PicturePlaceholder对象
**Class pptx.shapes.placeholder.PicturePlaceholder**
只能接受图片的占位符形状。

- adjustments
> 对此实例(AdjustmentCollection)的只读引用

- auto_shape_type
> 标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
如果此形状不是自动形状，则引发ValueError。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，
包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
即使未在形状上定义点击行为，也始终返回ActionSetting对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- fill
> 此形状的FillFormat实例，提供对填充属性(如填充颜色)的访问。

- get_or_add_ln()
> 返回<a：ln>元素，其中包含此形状的线格式属性XML。

- height
> 此占位符形状的有效高度；如果有，则为其直接应用的高度，
否则为其父布局占位符的高度。

- insert_picture(image_file )
> 返回一个在Image_file中描述图像的PlaceholderPicture对象，
> 该对象可以是路径（字符串）或类似文件的对象。
图像被裁剪以填充占位符的整个空间。
PlaceholderPicture对象具有Picture形状的所有属性和方法，
只是其shape_type属性的值为MSO_SHAPE_TYPE.PLACEHOLDER
而不是MSO_SHAPE_TYPE.PICTURE。

- is_placeholder
> 如果此形状是占位符，则为true。
如果形状具有<p：ph>元素，则它是一个占位符。

- left
> 此占位符形状的有效左边；如果有一个，则直接应用左侧；
否则，其父布局占位符的左侧。

- line
> 此形状的LineFormat实例，提供对线属性（如线颜色）的访问。

- ln
> <a：ln>元素，包含线条格式属性，例如线条颜色和宽度。
如果没有<a：ln>元素，则为None。

- name
> 形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
> 即使在此形状上未明确定义阴影，
也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> MSO_SHAPE_TYPE的成员，指定此形状的类型。
MSO_SHAPE_TYPE.PLACEHOLDER在这种情况下是无条件的。只读。

- text
> 读/写。形状文本的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
分配给文本将替换形状中先前包含的所有文本，
以及应用于该形状的任何段落或字体格式。
分配的文本中的换行符("\n")导致新段落开始。
分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
> 假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。

- text_frame
> 此形状的TextFrame实例。包含形状的文本，
并提供对文本格式设置属性的访问。

- top
> 此占位符形状的有效顶部；如果有，则直接应用其顶部，
否则为其父布局占位符的顶部。

- width
> 此占位符形状的有效宽度；如果具有一个宽度，则为直接应用的宽度；
否则为其父布局占位符的宽度。

# TablePlaceholder对象
**Class pptx.shapes.placeholder.TablePlaceholder**
> 只能接受图片的占位符形状。

- adjustments
> 对此实例(AdjustmentCollection)的只读引用

- auto_shape_type
> 标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
如果此形状不是自动形状，则引发ValueError。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，
包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
即使未在形状上定义点击行为，也始终返回ActionSetting对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- fill
> FillFormat 此形状的实例，提供对填充属性(例如填充颜色)的访问。

- get_or_add_ln()
> 返回<a：ln>元素，其中包含此形状的线格式属性XML。

- height
> 此占位符形状的有效高度；如果有，则为其直接应用的高度，
否则为其父布局占位符的高度。


- insert_table(rows，cols )
> 返回一个PlaceholderGraphicFrame对象，其中包含一个由行，行和列组成的表。 
表格的位置和宽度与占位符的位置和宽度相同，其高度与行数成正比。
PlaceholderGraphicFrame对象具有GraphicFrame形状的所有属性和方法，
但其shape_type属性的值无条件地为MSO_SHAPE_TYPE.PLACEHOLDER。
请注意，返回值不是新表，而是包含新表。 
可以使用返回的PlaceholderGraphicFrame对象的table属性访问该表。

- left
> 此占位符形状的有效左边；如果有一个，则直接应用左侧；
否则，其父布局占位符的左侧。

- line
> 此形状的LineFormat实例，提供对线属性（如线颜色）的访问。

- ln
> <a：ln>元素，包含线条格式属性，例如线条颜色和宽度。
如果没有<a：ln>元素，则为None。

- name
> 形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
即使在此形状上未明确定义阴影，
> 也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> MSO_SHAPE_TYPE的成员，指定此形状的类型。
MSO_SHAPE_TYPE.PLACEHOLDER在这种情况下是无条件的。只读。

- text
> 读/写。形状文本的Unicode(在Python 3中为str)表示形式。
返回的字符串将包含换行符("\n")，分隔每个段落，
并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
> 分配给文本将替换形状中先前包含的所有文本，
以及应用于该形状的任何段落或字体格式。
分配的文本中的换行符("\n")导致新段落开始。
分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
(垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
可以分配字节(Python 2 str)或unicode(Python 3 str)。
字节可以是7位ASCII或UTF-8编码的8位字节。
假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。

- text_frame
> 此形状的TextFrame实例。
包含形状的文本，并提供对文本格式设置属性的访问。

- top
> 此占位符形状的有效顶部；如果有，则直接应用其顶部，
否则为其父布局占位符的顶部。

- width
> 此占位符形状的有效宽度；如果具有一个宽度，则为直接应用的宽度；
> 否则为其父布局占位符的宽度。

# PlaceholderGraphicFrame对象
**Class pptx.shapes.placeholder.PlaceholderGraphicFrame**
占位符形状填充有表格，图表或智能艺术品。

- chart
> Chart在此图形框架中包含图表的对象。
如果此图形框架不包含图表，则引发ValueError 。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，
包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
即使未在形状上定义点击行为，也始终返回ActionSetting对象。

- element
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- has_chart
> True如果此图形框架包含图表对象。False 除此以外。如果为True，则可以使用.chart属性访问图表对象 。

- has_table
> True如果此图形框架包含表格对象。False 除此以外。如果为True，则可以使用.table属性访问表对象 。

- height
> 读/写。EMU中形状的顶部和底部范围之间的整数距离

- left
> 读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位(EMU)

- name
> 形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
即使在此形状上未明确定义阴影，
也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
> MSO_SHAPE_TYPE的成员，指定此形状的类型。

- table
> Table此图形框中包含的对象。ValueError如果此图形框架不包含表格，
则引发 。

- top
> 读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位(EMU)

- width
> 读/写。动车组中左右形状范围之间的整数距离

# PlaceholderPicture对象
**Class pptx.shapes.placeholder.PlaceholderPicture**
占位符形状填充图片。

- auto_shape_type
> MSO_SHAPE的成员，指示遮罩形状。
PowerPoint中可用的任何所谓的“自动形状”(例如椭圆形或三角形)都可以掩盖图片。
当图片被形状遮盖时，该形状采用与图片相同的尺寸，
并且不会出现图片超出形状边界的部分。
请注意，新插入图片的默认值为MSO_AUTO_SHAPE_TYPE.RECTANGLE，
由于矩形的范围与图片的范围完全对应，
因此不会进行裁剪。可用的形状对应于MSO_AUTO_SHAPE_TYPE的成员 。
> 返回值也可以是None，                                                                                   
表示图片没有几何形状(不期望)或具有自定义几何形状(如自​​由形状)。
尽管没有几何图形，但是可以选择，但幻灯片上没有可见的图像。
这是因为没有几何形状，就不会出现“内部形状”。

- click_action
> 提供访问点击行为的ActionSetting实例。
单击行为是类似于超链接的行为，
包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
即使未在形状上定义点击行为，也始终返回ActionSetting对象。

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
> 此形状的lxml元素，例如 一个CT_Shape实例。
注意，不正确地操作这个元素可能会生成无效的演示文稿文件。
如果要使用它更改底层XML，请确保您知道自己在做什么。

- height
> 此占位符形状的有效高度；如果有，则为其直接应用的高度，
否则为其父布局占位符的高度。

- image
> 一个Image对象，可以访问此图片形状中的图像的属性和字节。

- is_placeholder
> 如果此形状是占位符，则为true。如果形状具有<p：ph>元素，
则它是一个占位符。

- left
> 此占位符形状的有效左边；如果有一个，则直接应用左侧；
否则，其父布局占位符的左侧。

- line
> 此形状的LineFormat实例，提供对线属性（如线颜色）的访问。

- name
形状的名称，例如“图片7”

- placeholder_format
> _PlaceholderFormat对象，提供对占位符特定属性（例如占位符类型）的访问。
如果形状不是占位符，则在访问时引发ValueError。

- rotation
> 读/写浮点数。顺时针旋转的度数。
可以指定负值以指示逆时针旋转，例如 分配-45.0会将设置更改为315.0。

- shadow
> ShadowFormat对象，可以访问此形状的阴影。
即使在此形状上未明确定义阴影，
也始终返回ShadowFormat对象（即，它继承了其阴影行为）。

- shape_id
> 标识此形状的只读正整数。
形状的ID在幻灯片上的所有形状中都是唯一的。

- shape_type
>MSO_SHAPE_TYPE的成员，指定此形状的类型。
MSO_SHAPE_TYPE.PLACEHOLDER在这种情况下是无条件的。只读。

- top
> 此占位符形状的有效顶部；如果有，则直接应用其顶部，
否则为其父布局占位符的顶部。

- width
> 此占位符形状的有效宽度；如果具有一个宽度，则为直接应用的宽度；
否则为其父布局占位符的宽度。

# _PlaceholderFormat对象
**Class pptx.shapes.base._PlaceholderFormat**
通过placeholder_format占位符形状的属性访问，提供占位符特定的属性，
例如占位符类型。

- element
> 此对象代理的p：ph元素。

- idx
> 整数占位符“ idx”属性。

- type
> 占位符类型，PP_PLACEHOLDER_TYPE 枚举的成员，
例如PP_PLACEHOLDER.CHART

# Note
```
# !/usr/bin/python
# coding:utf-8
from pptx import Presentation

#  加载一个ppt文件
prs = Presentation('pptx/zf.pptx')

#  此幻灯片版式将从其继承属性的幻灯片母版。
slide_master = prs.slide_master

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide_master.shapes

#  返回通过索引shapes中的第二个对象
shape = shapes[1]

#  标识此自动形状类型的枚举值，例如 MSO_SHAPE.ROUNDED_RECTANGLE。
#  如果此形状不是自动形状，则引发ValueError。
auto_shape_type = shape.auto_shape_type

#  提供对单击行为的访问的actionset实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
#  单击操作是在整个形状上定义的，而不是在形状内的文本运行。
#  即使在形状上没有定义单击行为，也总是返回actionset对象。
click_action = shape.click_action

#  此形状的lxml元素，例如CT_Shape实例。
#  注意，不正确地操作这个元素可能会产生无效的表示文件。如果要使用它更改底层XML，请确保您知道自己在做什么。
element = shape.element

#  此形状的FillFormat实例，提供对填充属性(如填充颜色)的访问。
fill = shape.fill

#  如果此形状可以包含文本，则为True。对于自动生成总是正确的。
has_text_frame = shape.has_text_frame

#  读/写。此形状的顶部和底部范围之间的整数距离，以英制公制单位（EMU）
shape.height = 2743100
height = shape.height

#  如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。
is_placeholder = shape.is_placeholder

#  读/写。此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位（EMU）
shape.left = 4571000
left = shape.left

#  此形状的LineFormat实例，提供对线属性(如线颜色)的访问。
line = shape.line

#  形状的名称，例如“图片7”
name = shape.name

#  一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。
#  如果形状不是占位符，则在访问时引发ValueError。
placeholder_format = shape.placeholder_format

#  读/写浮点数。顺时针旋转的度数。
#  可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。
shape.rotation = -45.0
rotation = shape.rotation

#  ShadowFormat 提供访问此形状阴影的对象。
#  总是返回一个ShadowFormat对象，即使没有影子明确对这种形状定义（即它继承了它的身影行为）。
shadow = shape.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = shape.shape_id

#  读/写。形状文本的Unicode(在Python 3中为str)表示形式。
#  返回的字符串将包含换行符("\n")，分隔每个段落，
#  并在图形的文本中为每个换行符(软回车)提供一个竖向制表符("\v")。
#  分配给文本将替换形状中先前包含的所有文本，
#  以及应用于该形状的任何段落或字体格式。
#  分配的文本中的换行符("\n")导致新段落开始。
#  分配的文本中的竖线("\v")字符会导致插入换行符(软回车)。
#  (垂直制表符显示在从PowerPoint复制的剪贴板文本中，作为其换行符的编码。)
#  可以分配字节(Python 2 str)或unicode(Python 3 str)。
#  字节可以是7位ASCII或UTF-8编码的8位字节。
#  假定采用UTF-8编码(也适用于ASCII)，则将字节值转换为unicode。
shape.text = 'HaI\'s text'
text = shape.text

#  此形状的TextFrame实例。
#  包含形状的文本，并提供对文本格式设置属性的访问。
text_frame = shape.text_frame

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位（EMU）
shape.top = 914300
top = shape.top

#  读/写。此形状左右范围之间的整数距离，以英制公制单位（EMU）
shape.width = 3657500
width = shape.width

#  加载一个ppt文件
prs = Presentation('pptx/zf-02.pptx')

#  使用Presentation的slides属性访问slides对象
slides = prs.slides

#  返回通过索引slides中的第三个对象
slide = slides[3]

#  返回包含出现在此幻灯片上的形状对象序列的幻灯片幻灯片实例。
shapes = slide.shapes

#  返回通过索引shapes中的第一个对象
shape = shapes[0]

#  Chart在此图形框架中包含图表的对象。如果此图形框架不包含图表，则引发ValueError。
chart = shape.chart

#  提供对单击行为的访问的actionset实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
#  单击操作是在整个形状上定义的，而不是在形状内的文本运行。
#  即使在形状上没有定义单击行为，也总是返回actionset对象。
click_action = shape.click_action

#  此形状的lxml元素，例如CT_Shape实例。
#  注意，不正确地操作这个元素可能会产生无效的表示文件。
#  如果要使用它更改底层XML，请确保您知道自己在做什么。
element = shape.element

#  如果此图形框架包含一个图表对象，则为True。否则False。
#  如果为True，则可以使用.chart属性访问图表对象。
has_chart = shape.has_chart

#  如果此图形框架包含表对象，则为True。否则False。
#  为True时，可以使用.table属性访问表对象。
has_table = shape.has_table

#  此形状的左边缘到幻灯片左边缘的整数距离，以英制公制单位（EMU）
shape.height = 2743000
height = shape.height

#  形状的名称，例如“图片7”
name = shape.name

#  一个_PlaceholderFormat对象，提供对特定于占位符的属性(如占位符类型)的访问。
#  如果形状不是占位符，则在访问时引发ValueError。
#  placeholder_format = shape.placeholder_format

#  读/写浮点数。顺时针旋转的度数。可以分配负值以指示逆时针旋转，例如，分配-45.0会将设置更改为315.0。
shape.rotation = -45.0
rotation = shape.rotation

#  无条件地引发了NotImplementedError。
#  图形框架对象对阴影效果的访问是特定于内容的（即，对于图表，表格等而言是不同的），并且尚未实现。
#  shadow = shape.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = shape.shape_id

#  标识此形状类型的唯一整数，例如 MSO_SHAPE_TYPE.TABLE。
shape_type = shape.shape_type

#  Table此图形框中包含的对象。
#  如果此图形框架不包含表格，则引发ValueError。
#  table = shape.table

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位（EMU）
shape.top = 914200
top = shape.top

#  读/写。此形状的顶部边缘到幻灯片顶部边缘的整数距离，以英制公制单位（EMU）
shape.width = 3657400
width = shape.width

#  返回通过索引shapes中的第五个对象
shape = shapes[4]

#  MSO_SHAPE的成员，指示遮罩形状。
#  PowerPoint中可用的任何所谓的“自动形状”（例如椭圆形或三角形）都可以掩盖图片。
#  当图片被形状遮盖时，该形状采用与图片相同的尺寸，并且不会出现图片超出形状边界的部分。
#  请注意，新插入图片的默认值为MSO_AUTO_SHAPE_TYPE.RECTANGLE，由于矩形的范围与图片的范围完全对应，因此不会进行裁剪。
#  可用的形状对应于MSO_AUTO_SHAPE_TYPE的成员。
#  返回值也可以是None，表示图片没有几何形状（不期望）或具有自定义几何形状（如自​​由形状）。
#  尽管没有几何图形，但是可以选择，但幻灯片上没有可见的图像。这是因为没有几何形状，就不会出现“内部形状”。
auto_shape_type = shape.auto_shape_type

#  提供对单击行为的访问的actionset实例。
#  单击行为是类似于超链接的行为，包括跳转到超链接(web页面)或演示文稿中的另一张幻灯片。
#  单击操作是在整个形状上定义的，而不是在形状内的文本运行。
#  即使在形状上没有定义单击行为，也总是返回actionset对象。
click_action = shape.click_action

#  float 表示从形状底部裁剪的相对部分。
#  读/写。1.0代表100％。例如，25％用0.25表示。
#  负值和大于1.0的值都是有效的。
shape.crop_bottom = 0.25
crop_bottom = shape.crop_bottom

#  float 表示从形状底部裁剪的相对部分。
#  读/写。1.0代表100％。
#  负值将边延伸到图像边界之外。
shape.crop_left = 0.25
crop_left = shape.crop_left

#  float 表示从形状底部裁剪的相对部分。
#  读/写。1.0代表100％。
shape.crop_right = 0.25
crop_right = shape.crop_right

#  float 表示从形状底部裁剪的相对部分。
#  读/写。1.0代表100％。
shape.crop_top = 0.25
crop_top = shape.crop_top

#  此形状的lxml元素，例如CT_Shape实例。
#  注意，不正确地操作这个元素可能会产生无效的表示文件。
#  如果要使用它更改底层XML，请确保您知道自己在做什么。
element = shape.element

#  此占位符形状的有效高度；如果有，则为其直接应用的高度，否则为其父布局占位符的高度。
shape.height = 2743000
height = shape.height

#  一个Image对象，可以访问此图片形状中的图像的属性和字节。
image = shape.image

#  如果此形状是占位符，则为true。如果形状具有<p：ph>元素，则它是一个占位符。
is_placeholder = shape.is_placeholder

#  此占位符形状的有效左边；如果有一个，则直接应用左侧；否则，其父布局占位符的左侧。
shape.left = 457000
left = shape.left

#  LineFormat的一个实例，提供对与此形状相邻的轮廓的属性(如颜色和宽度)的访问。
line = shape.line

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
#  总是返回一个ShadowFormat对象，即使没有影子明确对这种形状定义（即它继承了它的身影行为）。
shadow = shape.shadow

#  标识此形状的只读正整数。
#  形状的ID在幻灯片上的所有形状中都是唯一的。
shape_id = shape.shape_id

#  MSO_SHAPE_TYPE的成员，指定此形状的类型。
#  MSO_SHAPE_TYPE.PLACEHOLDER在这种情况下是无条件的。只读。
shape_type = shape.shape_type

#  此占位符形状的有效顶部；如果有，则直接应用其顶部，否则为其父布局占位符的顶部。
top = shape.top

#  此占位符形状的有效宽度；如果具有一个宽度，则为直接应用的宽度；否则为其父布局占位符的宽度。
width = shape.width

#  此对象代理的p：ph元素。
element = placeholder_format.element

#  整数占位符“ idx”属性。
idx = placeholder_format.idx

#  占位符类型，PP_PLACEHOLDER_TYPE 枚举的成员，例如PP_PLACEHOLDER.CHART
type = placeholder_format.type

```
