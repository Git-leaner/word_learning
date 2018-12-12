#!/usr/bin/python linux使用哪种解释器
#-*- coding:utf-8-*-
# filename:pic.py
#Author: levi
#date:2017/7/14
import requests #python http客户端，编写爬虫和测试服务器响应数据
import re #导入正则表达式模块，用于提取所需的内容
import random,os
from baidu.mkdir import mkdirFun

def spiderPic(html,keyword):
    print("正在查找："+keyword+"对应的图片，正在从百度图库中下载文件，请稍等...")
    for addr in re.findall('"objURL":"(.*?)"',html,re.S):
        print('正在爬取URL地址:' + str(addr)[0:50] + "...")
        try:
            pics=requests.get(addr,timeout=20) #请求图像url地址(最大时间20s)
        except requests.exceptions.ConnectionError:
            print("您当前地址请求错误")
            continue
        fn=open("./img/"+keyword+"/"+(str(random.randrange(0,1000,4))+'.jpg'),'wb+');
        fn.write(pics.content)
        fn.close();

if __name__=='__main__':
    print("欢迎使用百度图片爬取工具!")
    word=input('请输入想要爬取的关键词: ')
    result = requests.get(
        "https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=" + word)
    # 定义要创建的目录
    mkpath = "./img/" + word
    # 调用函数
    bool = mkdirFun(mkpath)
    if (bool):
        spiderPic(result.text,word)
    else:
        print("文件夹已创建")