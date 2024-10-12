import requests

# 伪装头信息
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9",
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
           }

#伪装ip
proxies = {
    'http':'http://47.93.121.200:80',
    'https':'http://47.93.121.200:80',
}

# 传递数据表单
data = {
    'usernm': 'xiaoxiao',
    'passwd': 'xiao123456',
    'authcode':'NFR2',
    'toUrl':'NFR2',
    'app':'accountr.aja_login'

}

r = requests.post('http://httpbin.org/get', headers=headers,proxies=proxies)

print(r.text)



