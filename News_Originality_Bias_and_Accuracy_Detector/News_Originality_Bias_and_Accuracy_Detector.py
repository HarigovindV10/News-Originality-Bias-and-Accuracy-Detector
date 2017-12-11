# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
import getopt
import cPickle
import csv
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold, train_test_split
from textblob import TextBlob
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def main():
    news = ""
    for character in sys.argv[1:]:
        news = news + character + " "
    originality = str(detector(news))
    sentiment = str(sentimental(news))
    result = originality + sentiment

    os.system("python3 Output_Window.py " + result)


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


def create_word_features(words):
	useful_words = [word for word in words if word not in stopwords.words("english")]
	my_dict = dict([(word, True) for word in useful_words])
	return my_dict


def sentimental(news):
    words = word_tokenize(news)
    neg_reviews = []
    for fileid in movie_reviews.fileids('neg'):
    	words_ = movie_reviews.words(fileid)
        neg_reviews.append((create_word_features(words_), "negative"))
    pos_reviews = []
    for fileid in movie_reviews.fileids('pos'):
    	words_ = movie_reviews.words(fileid)
    	pos_reviews.append((create_word_features(words_), "positive"))
    train_set = neg_reviews[:750] + pos_reviews[:750]
    test_set = neg_reviews[750:] + pos_reviews[750:]
    classifier = NaiveBayesClassifier.train(train_set)
    words=create_word_features(words)
    return classifier.classify(words)


def tokens(news):
    news = unicode(news, 'utf8')
    return TextBlob(news).words


def lemmas(news):
    news = unicode(news, 'utf8').lower()
    words = TextBlob(news).words
    return [word.lemma for word in words]


def train_multinomial_nb(newss):
    msg_train, msg_test, label_train, label_test = train_test_split(newss['news'], newss['label'], test_size=0.2)
    pipeline = Pipeline([('bow', CountVectorizer(analyzer=lemmas)), ('tfidf', TfidfTransformer()), ('classifier', MultinomialNB())])
    params = {
    'tfidf__use_idf': (True, False),
    'bow__analyzer': (lemmas, tokens),
    }
    grid = GridSearchCV(
        pipeline,
        params,
        refit=True,
        n_jobs=-1,
        scoring='accuracy',
        cv=StratifiedKFold(label_train, n_splits=3),
        )

    nb_detector = grid.fit(msg_train, label_train)
    predictions = nb_detector.predict(msg_test)
    file_name = 'newsmodel1.txt'
    with open(file_name, 'wb') as fout:
        cPickle.dump(nb_detector, fout)


def predict(news):
  nb_detector = cPickle.load(open('newsmodel1.txt'))
  nb_predict = nb_detector.predict([news])[0]
  return nb_predict


def detector(news):
    newsS = pd.read_csv('news.txt', sep='\t', quoting=csv.QUOTE_NONE, names=["label", "news"])
    if(os.path.isfile('newsmodel1.txt') is False):
        train_multinomial_nb(newsS)
    prediction = predict(news)
    return prediction


if __name__ == '__main__':
    main()
