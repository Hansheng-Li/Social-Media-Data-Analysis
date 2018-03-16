from numpy import average
from time import time
import numpy as np
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import json
from utils import w2v_load_model, txt2words

# source venv2.7/bin/activate

class DeepTextAnalyzer(object):
    def __init__(self, word2vec_model):
        """
        Construct a DeepTextAnalyzer using the input Word2Vec model
        :param word2vec_model: a trained Word2Vec model
        """
        self._model = word2vec_model

    def txt2vectors(self,txt, is_html):
        """
        Convert input text into an iterator that returns the corresponding vector representation of each
        word in the text, if it exists in the Word2Vec model
        :param txt: input text
        :param is_html: if True, then extract the text from the input HTML
        :return: iterator of vectors created from the words in the text using the Word2Vec model.
        """
        words = txt2words(txt)
        words = [w for w in words if w in self._model]
        if len(words) != 0:
            for w in words:
                yield self._model[w]


    def txt2avg_vector(self, txt, is_html):
        """
        Calculate the average vector representation of the input text
        :param txt: input text
        :param is_html: is the text is a HTML
        :return the average vector of the vector representations of the words in the text
        """
        vectors = self.txt2vectors(txt,is_html=is_html)
        vectors_sum = next(vectors, None)
        if vectors_sum is None:
            return None
        count =1.0
        for v in vectors:
            count += 1
            vectors_sum = np.add(vectors_sum,v)

        #calculate the average vector and replace +infy and -inf with numeric values
        avg_vector = np.nan_to_num(vectors_sum/count)
        return avg_vector

def load_tweets(fname):
    tweets = []
    i = 0

    for line in open(fname):
        diclin = json.loads(line)
        id_str, label, text = diclin['id_str'], diclin['label'], diclin['text']
        tweets.append([id_str, label, text])
    return tweets

def generate_arff_header(f):
    f.write('@relation SentimentsInW2V\n\n')
    for i in range(301):
        f.write('@attribute feature%s numeric\n' % i)
    f.write('@attribute class { relevant, irrelevant }\n\n')

def w2v_vector(dta, text):
    vector = dta.txt2avg_vector(text, is_html=False)
    if vector is None:
        return None
    return [str(v) for v in vector]

def generate_arff_data(f, tweets):
    t0 = time()
    model = w2v_load_model('GoogleNews-vectors-negative300.bin')
    print 'loading model: %s' % (time() - t0)

    dta = DeepTextAnalyzer(model)
    f.write('@data\n')
    for id_str, label, text in tweets:
        vector = w2v_vector(dta, text)
        if vector is None:
            print 'Could not generate Word2Vec vector for %s' % text
        else:
            f.write('%s,%s,%s\n' % (id_str, ','.join(vector), label))

if __name__ == '__main__':
    import platform

    platform.architecture()
    tweets = load_tweets('eval.txt')
    with open('p3eval.arff', 'w') as f:
        generate_arff_header(f)
        generate_arff_data(f, tweets)
