# -*- coding: utf-8 -*-
# 时          间 : 2021/10/23 14:27
# 高贵的高级工程师 : 元元学长
from PIL import Image
from PIL import ImageFilter
im=Image.open("123.jpg")
om=im.filter(ImageFilter.CONTOUR)
om.save('123.jpg')