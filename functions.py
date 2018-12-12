__author__ ='levi'
import requests,js2py

def spider_word_by_name(name):
    if name.isalpha():
        # js = js2py.eval_js('./sign.js')
        # url='http://fanyi.baidu.com/v2transapi'
        url='http://fanyi.baidu.com/basetrans'
        data={
            'from':'en',
            'to':'zh',
            'query':name,
            # 'transtype':'translang',
            # 'simple_means_flag': 3,
            # 'sign': sign,
            # 'token': token
        }
        cookies="BAIDUID=7D7BC16BB3DF11F602437E806C9174F7:FG=1; BIDUPSID=7D7BC16BB3DF11F602437E806C9174F7; PSTM=1514103194; __cfduid=d6dc7d78514ff9d540e9e6bd0e12066df1524492250; H_WISE_SIDS=114551_123252_123799_120763_120219_118895_118873_118841_118836_118793_123619_107319_122034_117328_122788_124128_124074_123985_124109_123814_124061_123809_123853_123980_124030_124078_110085_123289_100460; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=Np8sJeCCxG37qXv789wXqO-TaiMazl7OiRsn3J; H_BDCLCKID_SF=tR4f_C_2JDP3jtbNhDTVMDCShUFs355r-2Q-5hOy3KONEfK6jP5xBUDqLtjiy-btHC6w0-QYWx5DhpFuDjRHMDCV-frb-C62aKDs2tty-hcqEpO9QT-bKqkBjNA8-hvDB-jn3RTzK4cSMp7Y0Rb_DUTh-p52f6_ttbCj3J; BDUSS=05Hb3U1U1RlNjh6QWViWnRDUzdjZkRoT3lOVnZTNmxOTjVIeGNJMWtKOGxibXBiQUFBQUFBJCQAAAAAAAAAAAEAAACwrlJ2bGV22Lx4bAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACXhQlsl4UJbM; PSINO=1; H_PS_PSSID=26524_1465_21096_26350_20928; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531187496; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531187496; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D"
        header = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        }
        cookies=''
        response=requests.post(url, data=data,headers=header)
        print('baidu',response);
        data=response.json()
        print(data)
        # print(data.decode('unicode - escape'))

        try:
            means=''
            # for item in data['dict_result']['simple_means']['symbols'][0]['parts']:
            #     means+=item['part']+' '+str(item['means'])+'/'
            #     ph=data['dict_result']['simple_means']['symbols'][0]['ph_am']+'/'+\
            #        data['dict_result']['simple_means']['symbols'][0]['ph_en']
            print(data['dict']['symbols']);
            for item in data['dict']['symbols'][0]['parts']:
                means+=item['part']+' '+str(item['means'])+'/'
                ph=data['dict']['symbols'][0]['ph_am']+'/'+\
                   data['dict']['symbols'][0]['ph_en']
            return means, ph
        except Exception as e:
            print(e)