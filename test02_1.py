import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors

# Connet to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='spider2201_douban',
                             cursorclass=pymysql.cursors.DictCursor)


# 创建一个Request,等于一个url,request需要放headers
h = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
req = urllib.request.Request("https://movie.douban.com/top250",headers=h)

# 参数可以是一个url地址，也可以是一个request
r = urllib.request.urlopen(req)
# print(r.status)
# print(r.read().decode())

html_doc = r.read().decode()

# 使用bs4或者是re正则表达式进行数据提取
soup = BeautifulSoup(html_doc, 'html.parser')

items = soup.find_all("div", class_="item")

# print(items)

with connection:
    for item in items:
        img = item.find("div", class_="pic").a.img
        name = img['alt']
        url = img['src']




        # 把提取出来的数据存储到MySQL
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `movie_info` (`movie_name`, `movie_url`) VALUES (%s, %s)"
            cursor.execute(sql, (name, url))

        # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()
