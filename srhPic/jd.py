#!/usr/bin/python linux使用哪种解释器
#-*- coding:utf-8-*-
# filename:baidu.py
#Author: levi
#date:2017/7/14
from urllib import request #获取网页源代码

url="http://www.jd.com"
resource =request.urlopen(url);
resource2 =request.urlretrieve(url);
html=resource.read() #把网页对象转成字符串

print(html)

fn=open('jd.html','w+b');   #b二进制
fn.write(html) #写到匹配的字符串
fn.close()

#python主方法
if __name__ == '__main__':
    print("hello python!");
