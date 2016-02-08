#How to use NLTK with there built-in Twitter_Samples

1. Clone this repository: https://github.com/japerk/nltk-trainer

2. Run python from bash "python"
import nltk
nltk.download
Downloader> d
Identifier> movie_reviews
Downloader> d
Identifier> twitter_samples

3. go to nltk_data/corpora/movie_reviews/ directory

4. rm pos/*

5. rm neg/*

6. copy positive_tweets.json and negative_tweets.json from twitter_samples corpora into movie_reviews/pos and movie_reviews/neg respectively 

7. put translatePos.py and translateNeg.py into movie_reviews/pos and movie_reviews/neg respectively 

8. Run python translatePos.py and python translateNeg.py

9. go to nltk-trainer/ directory

10. Run "python train_classifier.py movie_reviews --instances paras --classifier NaiveBayes"

11. go to nltk_data/classifiers/

12. Run "mv movie_reviews_NaiveBayes.pickle twitter_NaiveBayes.pickle"

13. To use in python:
classifier = nltk.data.load("classifiers/twitter_NaiveBayes.pickle")

//tweet.tweet_text.encode('utf-8') is text of tweet to be analyzed
feats = dict([(word, True) for word in tweet.tweet_text.encode('utf-8')])

//print the sentiment
print classifier.classify(feats)
