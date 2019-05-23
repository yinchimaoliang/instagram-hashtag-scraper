from bs4 import BeautifulSoup
import requests

class main():

url_base = 'https://top-hashtags.com/hashtag/'
web_data = requests.get(url_base)
soup = BeautifulSoup(web_data.text,'lxml')
# hashtags = soup.select('ul > li > div > ul > li > div > div > a')
# hashtags = soup.select('ul > li > div')
# print(hashtags)
# t = soup.select('div.entry-content > ul.tht.no-bullet > li > div.row.align-top > div > a')
t = soup.select('div.entry-content > ul.tht.no-bullet ')
t2 = t[0].select('li > div.row.align-top > div.tht-tag.small-7.medium-9.columns')
for i in t2:
    print(i.text)


# print(soup)
# titles = soup.select('//*[@id="post-69"]/div[1]/ul[1]/li[1]/div/div[2]/a)
#print(titles)
# contents = soup.select('div.short-content')
# print(contents)
# for i,j in zip(titles,contents):
    # data = {
        # 'title':i.get_text(),
        # 'content':j.get_text()
    # }
# print(data)
# //*[@id="post-69"]/div[1]/ul[1]/li[1]/div/div[2]