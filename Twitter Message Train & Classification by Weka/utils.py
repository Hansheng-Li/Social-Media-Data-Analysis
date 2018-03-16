def txt2words(inputString):
    from re import findall
    return findall(r'(?u)\w+', inputString)

def w2v_load_model(fname):
    from gensim.models.keyedvectors import KeyedVectors
    return KeyedVectors.load_word2vec_format(fname, binary=True)
