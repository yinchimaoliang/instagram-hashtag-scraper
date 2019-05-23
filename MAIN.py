from bs4 import BeautifulSoup
import requests


URL_BASE = 'https://top-hashtags.com/instagram/'
PAGE_NUM = 10


class main():
    def __init__(self,url_base):
        self.url_base = url_base
        self.hashtags = []
        self.urls = [url_base]
        for i in range(PAGE_NUM):
            self.urls.append(self.url_base + str((i + 1) * 100 + 1) + '/')

        print(self.urls)

        # print(self.urls)
    def getOnePage(self,url):
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text,'lxml')
        t = soup.find_all(name='ul', attrs={'class': 'tht no-bullet'})
        # t2 = t[0].select('li > div.row.align-top > div.tht-tag.small-7.medium-9.columns')
        t2 = t[0].select('li > div.row.align-top > div.tht-tag.small-7.medium-9.columns')
        for i in t2:
            self.hashtags.append(i.text[1:])

    def getAllHashtags(self):
        for url in self.urls:
            self.getOnePage(url)




    def mainFunc(self):
        self.getAllHashtags()



if __name__ == '__main__':
    t = main(URL_BASE)
    t.mainFunc()

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