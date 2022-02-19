# -*- coding: utf-8 -*-
# 时          间 : 2022/2/19 16:27
# 高贵的高级工程师 : 元元学长
import requests
import time

headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
}
base_url = "http://q.qlogo.cn/headimg_dl?bs=qq&dst_uin=qqnum&src_uin=www.feifeiboke.com&fid=blog&spec=640"
print(type(base_url))
url_p = str(input("请输入QQ账号"))
url = base_url.replace('qqnum',url_p)
print("当前的网址是："+url)
img_resp = requests.get(url,headers=headers)
# img_resp.content  #这里拿到的是字节
# print(img_resp.content)
img_name = url_p+".jpg"     #给写入的文件加入拓展名
# print(img_name)
with open("img/"+img_name,mode="wb") as f:
    f.write(img_resp.content)   #图片内容写入到文件
    time.sleep(1)       #sleep里面的参数单位为秒
    print(url_p + '\t\t' +"QQ的头像下载完成")