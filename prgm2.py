#program to compare similarity between two sentences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents=("this is a big big big big big big big big big big big big big big big big big big big big big big big big sentence one","this is a big big big big big big big big big big big big big big big big big big big big big big big big sentence two")
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1])[0][0])