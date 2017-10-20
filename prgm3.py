# program to fetch similar news
import newspaper
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vectorizer_cosine(b):
    global document
    tfidf_vectorizer = TfidfVectorizer()
    similar_news = (b,)
    documents = document + similar_news
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1]))
    if cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1]) > 0.12:
        return 1
    else:
        return 0


news = input('Enter news : ')
document = (news,)
cnn_paper = newspaper.build('https://cnn.com/')
bbc_paper = newspaper.build('https://bbc.com/')
foxnews_paper = newspaper.build('https://foxnews.com/')
for article in bbc_paper.articles:
    article.download()
    article.parse()
    file = open("NewFile.txt", "w")
    file.write(article.text)
    file.close()
file = open("NewFile.txt", "r")
for line in file:
    a = vectorizer_cosine(line)
    if a == 1:
        print(line)

file.close()
