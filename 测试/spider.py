# -*- coding: utf-8 -*-
# 时          间 : 2021/10/28 19:23
# 高贵的高级工程师 : 元元学长



#爬取网页
import urllib.request


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # saveData(savepath)
    askURL("https://movie.douban.com/top250?start=21")

def getData(baseurl):
    datalist = []
    #逐一解析数据
    return datalist


#得到指定的一个URL网页内容

def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 93.0.4577.63 Safari / 537.36"
    }
# 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器(本质上是告诉浏览器，我们可以接收什么水平的文件内容)
    request = urllib.request.Request(url,headers=head)

    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    # return html;


#保存数据
def saveData(davepath):
    print("save....")

main()