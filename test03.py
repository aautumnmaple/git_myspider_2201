import urllib.request

r = urllib.request.urlopen("http://httpbin.org/get")
print(r.status)
print(r.msg)
print(r.read().decode())