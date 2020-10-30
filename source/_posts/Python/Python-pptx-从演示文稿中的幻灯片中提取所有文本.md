---
title: Python-pptx-从演示文稿中的幻灯片中提取所有文本
categories: Python
---
![060210341567_0∂‡¿≤a√Œ_0.png](https://upload-images.jianshu.io/upload_images/15325592-75202deac3245d68.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 代码

```
import json

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

def ppt_catch_format_text(filename):
    """
    抓取PPT的内容，按段落返回
    其中 filename 是PPT文件的路径
    """
    prs = Presentation(filename)
    txt_oa = {}
    for x in range(len(prs.slides)):
        txt_oa[x] = []
        #  ---Only on text-boxes outside group elements---
        for shape in prs.slides[x].shapes:
            if hasattr(shape, "text"):
                row_text = shape.text.encode('utf-8').strip().decode()
                txt_oa[x].append(row_text)
        #  ---Only operate on group shapes---
        group_shapes = [shp for shp in prs.slides[x].shapes 
                        if shp.shape_type ==MSO_SHAPE_TYPE.GROUP]
        for group_shape in group_shapes:
            for shape in group_shape.shapes:
                if shape.has_text_frame:
                    row_text = shape.text.encode('utf-8').strip().decode()
                    txt_oa[x].append(row_text)
    return txt_oa

text_list = ppt_catch_format_text('Doraemon.pptx')
text_list = json.dumps(text_list, ensure_ascii=False, indent=4).replace("\\n","")
print(text_list)
```

- PPT 文件

![060210594077.png](https://upload-images.jianshu.io/upload_images/15325592-29e0b61b77b32397.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 这里的 PPT 有3页，注意 PPT 文件的后缀一定要是 `.pptx`

- 提取内容

```
{
    "0": [
        "我之所以到现在还怎么没用，是因为我不想离开哆啦A梦"
    ],
    "1": [
        "你看，不倒翁站起来了，大雄也可以自己站起来啊!"
    ],
    "2": [
        "你受伤的时候，我永远都在。"
    ]
}
```

> 这里把从 PPT 中取出的内容转 JSON 并格式化输出
