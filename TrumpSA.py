import csv
from textblob import TextBlob

infile = 'C:\cnn_twitter_output.csv'

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        print sentence
        print blob.sentiment.polarity, blob.sentiment.subjectivity