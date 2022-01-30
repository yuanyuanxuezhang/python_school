# -*- coding: utf-8 -*-
# 时          间 : 2022/1/28 22:23
# 高贵的高级工程师 : 元元学长
import re

#findall: 匹配字符创中所有的符合正则的类容
s = re.findall(r"\d+","我的电话号是：10086。你的电话是：10010")
print(s)

#finditer: 匹配字符串中所有的类容[返回的是迭代器],从迭代器中拿到的内容需要.group()
#迭代器的效率要高于列表的效率
it = re.finditer(r"\d+","我的电话号是：10086。你的电话是：10010")
for i in it:
    print("finditer遍历的结果为",i.group())

#search：返回的结果是match对象。拿到数据需要.group()，
#search：找到一个结果立刻返回
se = re.search(r"\d+","我的电话是：10086，你的电话是10000")
print("search的结果为:",end="")
print(se.group())

# match是从头开始匹配,开头的第一个不是正则表达式中的值则返回为未找到，不继续往下匹配
ma = re.match(r"\d+","1000,hello world!")
print(ma.group())

#预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号是：10086。你的电话是：10010")
for it in ret:
    print("正则表达式的预加载算法：",it.group())
print()

s = """
<div class="yyxuezhang"><span id="1">元元学长</span></div>
<div class="zhangkang"><span id="2">张康</span></div>
<div class="suhuilong"><span id="3">苏慧龙</span></div>
<div class="huning"><span id="4">胡教授</span></div>
<div class=""><span id=""></span></div>
"""
# re.S: 让.能匹配换行符，正常情况下.只能匹配除换行符的任意字符

#(?P<分组名字>正则) 可以单独从正则匹配的类容中进一步提取类容
obj = re.compile(r'<div class=".*?"><span id="\d+">(?P<html_text>.*?)</span></div>',re.S)

result = obj.finditer(s)
for it in result:
    print(it.group())
result = obj.finditer(s)
for it in result:
    print(it.group("html_text"))