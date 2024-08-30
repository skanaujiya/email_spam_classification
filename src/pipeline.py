import gensim
import numpy as np
import gensim.downloader as api
from gensim.models import Word2Vec

word2vec = api.load('word2vec-google-news-300')

## here we find the average wordToVector
def avg_word2vec(corpus):

    embeded_corpus = []
    for doc in corpus:
        vector = []
        for word in doc:
            if word in word2vec.key_to_index:
                vector.append(word2vec[word])
                
        if len(vector) == 0:
            vector = np.zeros((300,))
        else:
            vector = np.mean(vector,axis=0)
        embeded_corpus.append(vector)
    return np.array(embeded_corpus)