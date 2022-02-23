# -*- coding: utf-8 -*-
# 时          间 : 2022/2/19 20:58
# 高贵的高级工程师 : 元元学长
from lxml import etree
etree.XML().xpath()
xml = ""
tree = etree.XML(xml)
tree.xpath("/book")     # /表示层级关系。 第一个/是根节点
