# See https://data-flair.training/blogs/nltk-python-tutorial/

import nltk
# nltk.download()

from nltk.tokenize import sent_tokenize

# NLTK Sentence Tokenizer
text = "Today is a great day. It is even better than yesterday. And yesterday was the best day ever. Last night, " \
       "I went to Mrs. Martinez’s housewarming.”, ‘It was a disaster." \
       "Hi, how are you? I'm good, you? Great!"
sent_tokenize(text)

# NLTK Word Tokenizer
nltk.word_tokenize(text)

# Find Synonyms From NLTK WordNet
from nltk.corpus import wordnet

syn = wordnet.synsets('love')
syn[0].definition()
syn[0].examples()
# To get the list of synonyms:
synonims = []
for s in syn:
    for lemma in s.lemmas():
        synonims.append(lemma.name())

# Find Antonyms From NLTK WordNet
antonyms = []
for syn in wordnet.synsets('beautiful'):
    for lem in syn.lemmas():
        if lem.antonyms():
            antonyms.append(lem.antonyms()[0].name())

# Stemming NLTK
from nltk.stem.porter import *
stemmer = PorterStemmer()
# print(stemmer.stem('loving'), stemmer.stem('corpora'), stemmer.stem('writer'))

# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('this'), lemmatizer.lemmatize('believes', pos='v'), lemmatizer.lemmatize('crossing', pos='n'))

# Stop words
from nltk.corpus import stopwords
text = "Today is a great day. It is even better than yesterday. And yesterday was the best day ever!"
stopwords = set(stopwords.words('english'))
words = nltk.word_tokenize(text)
filteredWords = []
for word in words:
    if word not in stopwords:
        filteredWords.append(word)

# Speech Tagging
from nltk.tokenize import PunktSentenceTokenizer
text = 'I am a human being, capable of doing terrible things'
sentences = nltk.sent_tokenize(text)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))

