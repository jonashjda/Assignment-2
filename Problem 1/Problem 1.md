# Assignment 2 - Problem 1
Firstly, the 'pandas', 'operator', and 'numpy' modules are imported
```python
import pandas as pd
import operator
from numpy import dot
from numpy.linalg import norm
```

## Loading the file
The file is loaded using the CSV module and the values of the 'horoscope-clean', i.e. the horoscopes column are assigned to the variable 'texts'
```python
df = pd.read_csv('horoscopes.csv')
texts = df['horoscope-clean'].values
```

## Stopwords
Next, a 'stopwords' function is used to return a list of stopwords to be used for stopword-filtering
```python

def stopwords():
    """ Stopword list for American English
    """
    return ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "something", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


```

## Tokenizer
Then the entire document has to be tokenized using a tokenizer function, which turns the document into a list of all the words:
```python
def tokenizer(text, lower=True, stopword=True):

    if stopword:
        stopwordlist = stopwords()
        tokens = [token for token in text.lower().split(' ') if token not in stopwordlist]

    elif lower:
        tokens = text.lower().split()

    else:
        tokens = text.split()

    return tokens
```

## Word counter
Next, the 'word_count' function is used to create a dictionary and iterate over all the words in the file, adding 1 to the count for a specific word each time the word is mentioned. It then returns the counter-dictionary:
```python
def word_count(text, sort = True, stopword=True):

    counter = dict()
    for word in tokenizer(text, stopword=stopword):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1

    if sort:
        counter = dict(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))

    return counter
```

## List to dtm
Then, the 'list_to_dtm' function turns the list into a DTM, which can be used for cosine similarity later on
```python
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
```

## Finding the intersections and differences between the signs
The 'intersection function is defined, which returns the words that appear in both lists
```python
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
```

The 'difference' function is defined, which returns the assymetric difference between the lists, i.e. the words that appear in 'lst1' but not in 'lst2' and 'lst3':
```python
def difference(lst1, lst2, lst3):
    return list(set(lst1).difference(set(lst2)).difference(set(lst3)))
```

## Cosine similarity
The 'cosine_similarity' function returns the degree of overlap between the two lists
```python
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))
```

## Word counts for each list
Then, the 'word_count' function is called on a sign to make a word count for that specific sign. Afterwards, a list is created in order to be able to only get the 100 most frequent words, since it would otherwise be a dictionary which are unordered:
```python
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
```

## Printing the overlap, intersections, and differences
Lastly, the three functions from previous steps are used to print the overlap, the intersections, and the differences
```python
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
```

## Conclusion
As can be seen from running the script, 63 of the 100 most frequent words in all horoscopes are stoplist.