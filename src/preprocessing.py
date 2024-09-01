# import the necessary packages
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def check_and_download_stopwords():
    try:
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        # If not found, download stopwords
        nltk.download('stopwords')
        nltk.download('wordnet')

class Preprocess :
    def __init__(self) -> None:
        check_and_download_stopwords()
        self.stemmer = PorterStemmer()

    def pre_processing(self, messages):
        corpus = []
        for document in messages:
            review = re.sub('[^a-zA-Z]',' ', document)
            review = review.lower()
            review = review.split()
            review = [self.stemmer.stem(word) for word in review if word not in stopwords.words('english')]
            review =' '.join(review)
            corpus.append(review)
        return corpus