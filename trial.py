from bs4 import BeautifulSoup
import urllib2
import os


url_list = []
url = "https://www.snopes.com/category/facts/"
fake_news = ""


def initialize(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()
    soup = BeautifulSoup(data)
    return soup


soup = initialize(url)


if os.path.isfile('f.txt') is False:
    news_file = open('f.txt', 'w')
    for item in soup.find_all('div', {'class': 'article-link-image'}):
        sub_url = item.parent['href']
        sub_url = str(sub_url)
        news_file.write(sub_url)
        news_file.write('\n')
    news_file.close


news_file = open('f.txt', 'r')


for urls in news_file:
    url_list.append(urls)


news_file.close()


for urls in url_list:
    url = str(urls)
    soup = initialize(url)
    rating = soup.find('div', {'class': 'claim false'})
    status = str(rating)
    fake_news = ""
    if(status != 'None'):
        heading = soup.find('h1', {'class': 'article-title'})
        for character in heading:
            if(character == '<'):
                while(character != '>'):
                    continue
            else:
                fake_news = fake_news+character
    if (fake_news != ""):
        print("\n", fake_news)
