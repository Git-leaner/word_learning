# get_song()
import requests
import re
import json
def get_music_ids(e):
    print(e)

def download(url, data=None):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    try:
        res=requests.get(url=url, params=data, headers=header)
        return res
    except Exception as e:
        print(e)

def get_song(song_id):
    url='http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery172032066627119787605_1530874288967&songid='+song_id
    # url='http://music.taihe.com/song/'+song_id
    data=download(url).text
    data=re.findall(r'\((.*)\)', data)[0]
    print('type',data)
    data=json.loads(data)
    return data

def get_music_ids_by_name(song_name):
    # api='http://music.baidu.com/search'
    api='http://music.taihe.com/search'
    data ={
        'key': song_name
    }
    response=download(api, data=data)
    response.encoding='utf-8'
    html=response.text
    ul=re.findall(r'<ul.*</ul>',html, re.S)[0]
    sids=re.findall(r'sid&quot;:(\d+),', ul, re.S)
    print('sids',sids)
    return  sids

def get_music_info_by_name(name):
    sids=get_music_ids_by_name(name)
    music_info=[]
    for sid in sids:
        # temp=json.loads(get_song(sid))
        temp=get_song(sid)
        music_info.append(temp);
    return  music_info

if __name__ == '__main__':
    music_info=get_music_info_by_name('陈奕迅');
    print('if',music_info)