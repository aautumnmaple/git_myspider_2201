import requests
from bs4 import BeautifulSoup
import pymysql.cursors
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="spider2201_douban",
    cursorclass=pymysql.cursors.DictCursor
)


#伪装头信息
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
#伪装IP
proxies={
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890',
}
r=requests.get("https://movie.douban.com/top250",headers=headers,proxies=proxies)


base_url="https://movie.douban.com/top250"

num = eval(input("请输入要爬取的页数："))
with connection:
    for i in range(num):
        url = f"{base_url}?start={i * 25}"#25为一页，递增
        # url = "https://movie.douban.com/top250?start={i*25}"
        r = requests.get(url,headers=headers,proxies=proxies)
        soup = BeautifulSoup(r.text,"html.parser")
        items = soup.find_all("div", class_="item")  # 找出所有div标签属性为item并赋值给变量items
        for item in items:  # for循环一个一个取出items里的每一个元素
            pic_div = item.find("div", class_="pic")
            top = pic_div.em.string
            img = pic_div.a.img
            movie_name = (img["alt"])  # 海报名字
            movie_url = (img["src"])  # 海报地址
            piv_hd = item.find("div", class_="hd")
            china_name = piv_hd.find("span", class_="title").string  # 中文名
            English = piv_hd.find_all('span')[1].get_text().split("/")[1]#英文名
            actor = item.find("p").get_text().split("\n")[1].split("\xa0")[0].replace("\n", "").replace(" ", "")#主演
            # if语句判断切割字段，是否为空
            if not item.find("p").get_text().split("\n")[1].split("\xa0")[-1].replace("\n", "").replace(" ", ""):
                actor_zhu = "暂时还无该数据"
            else:
                actor_zhu = item.find("p").get_text().split("\n")[1].split("\xa0")[-1].replace("\n", "").replace(" ",
                                                                                                                 "")#主演
            # join = item.p.next_element.split("\xa0")[0].replace("\n","")  # p的后节点
            guo = item.p.get_text().split('/')[-2]#上映国家
            # time=item.p.get_text().split("/")[0].replice
            time = item.find("p").get_text().split("\n")[2].split("/")[0].replace("\n", "").replace(" ", "")#出版时间
            type = item.p.get_text().split('\n')[2].split('/')[-1]#类型
            pingfen = item.find("div", class_="star").get_text().split('\n')[2]#评分
            pingfen_num = item.find("div", class_="star").get_text().split('\n')[4]#评价人数
            if not item.find("p", class_="quote"):
                que = "暂时还无简介"
            else:
                que = item.find("p", class_="quote").get_text().replace("\n", "")

            print(top,movie_name, movie_url, china_name, English, guo, time, actor, actor_zhu, type, pingfen, pingfen_num, que)




            with connection.cursor() as cursor:
                sql = "INSERT INTO movie_info1(movie_name, movie_url, china_name, English, actor, actor_zhu, guo, time, type, pingfen, pingfen_num, que) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (movie_name, movie_url, china_name, English, actor, actor_zhu, guo, time, type, pingfen, pingfen_num, que))
        connection.commit()
