# -*- coding: utf-8 -*-
import newspaper
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
cnn_paper = newspaper.build('https://cnn.com/')
bbc_paper = newspaper.build('https://bbc.com/')
foxnews_paper = newspaper.build('https://foxnews.com/')
file = open("NewFile.txt", "w")
for article in foxnews_paper.articles:
    article.download()
    article.parse()
    file.write(article.text.encode('utf8'))
file.close()
def create_word_features(words):
	useful_words=[word for word in words if word not in stopwords.words("english")]
	my_dict=dict([(word, True) for word in useful_words])
	return my_dict

file=open("NewFile.txt","r")
for line in file:
    words=word_tokenize(line)
    neg_reviews = []
    for fileid in movie_reviews.fileids('neg'):
    	words_=movie_reviews.words(fileid)
    	neg_reviews.append((create_word_features(words_), "negative"))


    pos_reviews = []
    for fileid in movie_reviews.fileids('pos'):
    	words_=movie_reviews.words(fileid)
    	pos_reviews.append((create_word_features(words_), "positive"))
    train_set = neg_reviews[:750] + pos_reviews[:750]
    test_set = neg_reviews[750:] + pos_reviews[750:]
    classifier = NaiveBayesClassifier.train(train_set)
    words=create_word_features(words)
    print(classifier.classify(words))
