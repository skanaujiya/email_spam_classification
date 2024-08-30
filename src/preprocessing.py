# import the necessary packages
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('wordnet')
stemmer = PorterStemmer()


def pre_processing(messages):
    corpus = []
    for document in messages:
        review = re.sub('[^a-zA-Z]',' ', document)
        review = review.lower()
        review = review.split()
        review = [stemmer.stem(word) for word in review if word not in stopwords.words('english')]
        review =' '.join(review)
        corpus.append(review)
    return corpus