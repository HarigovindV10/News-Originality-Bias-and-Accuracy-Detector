import newspaper
cnn_paper=newspaper.build('http://cnn.com')
for article in cnn_paper.articles:
    print(article.url)
for category in cnn_paper.category_urls():
	print(category)

