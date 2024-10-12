import urllib.request

# 创建一个Request,等于一个url,request需要放headers
h = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
req = urllib.request.Request("http://httpbin.org/get",headers=h)


# r = urllib.request.urlopen(req)
# proxies = {
#    "http" : "127.0.0.1:7890"
# }

proxies = {
    "http": "183.234.215.11:8443"
}
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy_handler)
r = opener.open(req)


# 参数可以是一个url地址，也可以是一个request
r = urllib.request.urlopen(req)
print(r.status)
print(r.read().decode())