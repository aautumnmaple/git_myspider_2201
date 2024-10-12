import urllib.request

# 创建一个Request,等于一个url,request需要放headers
h = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
req = urllib.request.Request("https://movie.douban.com/top250",headers=h)

# 参数可以是一个url地址，也可以是一个request
r = urllib.request.urlopen(req)
print(r.status)
print(r.read().decode())


# 使用bs4或者是re正则表达式进行数据提取