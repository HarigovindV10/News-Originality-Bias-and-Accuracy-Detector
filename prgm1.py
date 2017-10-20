#program for fetching news
import newspaper
cnn_paper=newspaper.build('https://cnn.com/')
bbc_paper=newspaper.build('https://bbc.com/')
foxnews_paper=newspaper.build('https://foxnews.com/')
for article in bbc_paper.articles:
    article.download()
    article.parse()
    print(article.text)