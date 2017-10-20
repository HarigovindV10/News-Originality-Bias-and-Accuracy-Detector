from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vectorizer_cosine(b):
    global document
    tfidf_vectorizer = TfidfVectorizer()
    similar_news = (b,)
    documents = document + similar_news
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    if cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1]) > 0.50:
        print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1]))
        return 1
    else:
        return 0


news = input("Enter news : ")
document = (news,)
file = open("news.txt", "r")
for line in file:
    a = vectorizer_cosine(line)
    if a == 1:
        print(line)
file.close()
