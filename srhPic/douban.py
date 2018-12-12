#Python主方法
import requests,re
from bs4 import BeautifulSoup
if( __name__=='__main__'):
    print('正在抓取豆瓣电影TOP 250的数据....')

for page in range(10):
    print("==========正在抓取第"+str(page+1)+"页================")
    url="https://movie.douban.com/top250?start="+str(page*25)+"&filter="
    html=requests.get(url) #获取页面源代码
    soup=BeautifulSoup(html.text,'html.parser') #通过网页解析库来实现网页信息抓取
    soup=str(soup);
    title=re.compile(r'<span class="title">(.*)</span>')
    names=re.findall(title,soup)
    for name in names:
        if name.find('/')==-1:
            print(name)