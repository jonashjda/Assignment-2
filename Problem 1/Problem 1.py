import pandas as pd
import operator
from numpy import dot
from numpy.linalg import norm

df = pd.read_csv('horoscopes.csv')
texts = df['horoscope-clean'].values

def stopwords():
    """ Stopword list for American English
    """
    return ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "something", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def tokenizer(text, lower=True, stopword=True):

    if stopword:
        stopwordlist = stopwords()
        tokens = [token for token in text.lower().split(' ') if token not in stopwordlist]

    elif lower:
        tokens = text.lower().split()

    else:
        tokens = text.split()

    return tokens

def word_count(text, sort = True, stopword=True):

    counter = dict()
    for word in tokenizer(text, stopword=stopword):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1

    if sort:
        counter = dict(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))

    return counter


def list_to_dtm(corpus, stopword=True):
    wc = word_count(' '.join(corpus), stopword=stopword)
    lexicon = list(wc.keys())

    dtm = []
    for content in corpus:
        document = [0 for _ in lexicon]
        wc = word_count(content, stopword=stopword)
        for (i, word) in enumerate(lexicon):
            if word in wc:
                document[i] = wc[word]

        dtm.append(document)

    return dtm, lexicon

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def difference(lst1, lst2):
    return list(set(lst1).difference(set(lst2)))

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

wc_filtered = word_count(' '.join(texts))
wc_items = wc_filtered.items()
lst2 = list(wc_items)[:100]
print('Word counts with stopword filtering:')
print(lst2)
print()

wc_unfiltered = word_count(' '.join(texts),stopword=False)
wc_items = wc_unfiltered.items()
lst1 = list(wc_items)[:100]
print('Word counts without stopword filtering:')
print(lst1)
print()

print("The overlap between the two lists:")
(dtm,  lexicon) = list_to_dtm(texts, stopword=False)
v1 = dtm[0]
v2 = dtm[1]
print(cosine_similarity(v1, v2))
print()

print(f"These {len(intersection(lst1, lst2))} words appear in both lists:")
print(intersection(lst1, lst2))
print()

print(f"These {len(difference(lst1, lst2))} words appear in the list without stopword filtering, but not in the one with stopword filtering:")
print(difference(lst1, lst2))
print()