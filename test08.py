import requests
from bs4 import BeautifulSoup
import ddddocr

s = requests.Session()
# 伪装头信息
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9",
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
           }

#伪装ip     站大爷找免费代理
proxies = {
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890',
}
for item in s.cookies.iteritems():
    print(item[0],":",item[1])
print("================================")

# 请求登录页面
login = s.get('https://www.nowapi.com/?app=account.login',headers=headers,proxies=proxies)
print(login.text)
print(s.cookies.keys())

for item in s.cookies.iteritems():
    print(item[0],":",item[1])


# 使用bs4解析页面获取验证码的地址
soup = BeautifulSoup(login.text, 'html.parser')
image_url = soup.find_all(id='authCodeImg')[0]['src']


# 把url地址转换为图片
response = s.get(image_url,headers=headers,proxies=proxies)
# 确保请求成功
if response.status_code == 200:
    # 以二进制写入模式打开文件
    with open("wy.jpg",'wb') as file:
        # 写入图片内容
        file.write(response.content)
else:
    print(f"下载失败，状态码：{response.status_code}")

# 破解验证码  图片url
# 识别图片 ====> ocr
ocr = ddddocr.DdddOcr()
image = open("wy.jpg", "rb").read()
result = ocr.classification(image)
print(result)


# 登录请求：传递表单数据
data = {
    'usernm': 'wy123456',
    'passwd': 'wy123456',
    'authcode':'result',
    'toUrl':'',
    'app':'accountr.aja_login'

}

r = s.post('https://www.nowapi.com/index.php?ajax=1', headers=headers,proxies=proxies,data=data)

print(r.text)
