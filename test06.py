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
    'username': 'xiaoxioa',
    'age': '20'

}

r = requests.post('http://httpbin.org/get', headers=headers,proxies=proxies)

print(r.text)

# 1、get请求---post登录
# 2、post 传递表单数据  验证码
# 3、动态代理：程序爬取免费代理Ip  校验代理是否正常  使用：请一次换一次IP  代理不能用，要换代理，重新发起请求
# 4、UA动态
# 5、登录状态保持？  模拟cookie的功能

