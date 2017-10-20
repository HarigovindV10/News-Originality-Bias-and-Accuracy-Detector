import newspaper
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from newspaper import news_pool
from difflib import SequenceMatcher
from textblob import TextBlob as tb


document = ("Moscow",)
cnn_paper=newspaper.build('https://cnn.com/')
bbc_paper=newspaper.build('https://bbc.com/')
foxnews_paper=newspaper.build('https://foxnews.com/')
papers=[cnn_paper,bbc_paper,foxnews_paper]
#news_pool.set(papers, threads_per_source=2)
#news_pool.join()
i=0
def vectorizer_cosine(b):
    tfidf_vectorizer = TfidfVectorizer()
    a = (b,)
    documents = document + a
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    if cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1]) > 0.12:
        return 1
    else:
        return 0
while(i<20):
    for article in bbc_paper.articles:
        article.download()
        article.parse()
        print(article.text)
    i=i+1
""""   words=article.text.split("\n")
a=vectorizer_cosine(article.text)
    if a==1:
        print(article.text)
    else:
        print("Not FOUND {}".format(i))

    i=i+1"""

#print(words)
f=open("NewFile.txt","r")
for line in f:
    a=vectorizer_cosine(line)
    if a==1:
        print(line)

f.close()
