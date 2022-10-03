# Assignment 2 - Problem 2
Firstly, the 'operator' and 'panda' moduldes are imported, and 'itemgetter' is imported from 'operator'

```python
import operator
import pandas as pd
from operator import itemgetter
```
## Loading the horoscopes
Then, the file is imported by using the CSV module, and the horoscopes from three selected signs are set as variables named according to said sign
```python
df = pd.read_csv('assignments\Assignment 2\Task 2\horoscopes.csv')

signs = list(set(df['sign'].values))

virgo_sign = df['sign'] == 'virgo'
virgo_texts = df['horoscope-clean'].loc[virgo_sign].values

cancer_sign = df['sign'] == 'cancer'
cancer_texts = df['horoscope-clean'].loc[cancer_sign].values

pisces_sign = df['sign'] == 'pisces'
pisces_texts = df['horoscope-clean'].loc[pisces_sign].values

```

## Stopwords
Next, a 'stopwords' function is used to return a list of stopwords to be used for stopword-filtering
```python

def stopwords():
    """ Stopword list for American English
    """
    return ["","a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]

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

## Counting words within the specific signs
Then, the 'word_count' function is called on a sign to make a word count for that specific sign. Afterwards, a list is created in order to be able to only get the 200 most frequent words, since it would otherwise be a dictionary which are unordered:
```python
wc_virgo = word_count(' '.join(virgo_texts))
virgo_items = wc_virgo.items()
virgo_list = list(virgo_items)[:200]
print("The 200 most frequent words in virgo are:")
print(virgo_list)
print()

wc_cancer = word_count(' '.join(cancer_texts))
cancer_items = wc_cancer.items()
cancer_list = list(cancer_items)[:200]
print("The 200 most frequent words in cancer are:")
print(cancer_list)
print()

wc_pisces = word_count(' '.join(pisces_texts))
pisces_items = wc_pisces.items()
pisces_list = list(pisces_items)[:200]
print("The 200 most frequent words in pisces are:")
print(pisces_list)
print()
```

## Finding the differences between the signs
Next, the 'difference' function is defined, which returns the assymetric difference between the lists, i.e. the words that appear in 'lst1' but not in 'lst2' and 'lst3':
```python
def difference(lst1, lst2, lst3):
    return list(set(lst1).difference(set(lst2)).difference(set(lst3)))
```

Then, a variable is created for each of the signs and the 'difference' function is called with the corresponding sign as 'lst1' and the two others as 'lst2' and 'lst3'. 'Itemgetter' is used to make sure the 'difference' function is based on only the word in each sublist rather than the sublist itself.
```python
virgo_only = sorted(difference(list(map(itemgetter(0), virgo_list)), list(map(itemgetter(0), cancer_list)), list(map(itemgetter(0), pisces_list))))
cancer_only = sorted(difference(list(map(itemgetter(0), cancer_list)), list(map(itemgetter(0), virgo_list)), list(map(itemgetter(0), pisces_list))))
pisces_only = sorted(difference(list(map(itemgetter(0), pisces_list)), list(map(itemgetter(0), virgo_list)), list(map(itemgetter(0), cancer_list))))
```

Lastly, the variables from the step before are printed along with an f-string that contains the number of words in the list:
```python
print(f'These {len(virgo_only)} items appear in virgo but not in the others:')
print(virgo_only)
print()

print(f'These {len(cancer_only)} items appear in cancer but not in the others:')
print(cancer_only)
print()

print(f'These {len(pisces_only)} items appear in pisces but not in the others:')
print(pisces_only)
print()
``` 