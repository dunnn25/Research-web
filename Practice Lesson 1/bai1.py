import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

PorterStemmer = PorterStemmer()

word = "running","runner","ran","easily","fairly"

for w in word:
    print(f"{w} --> {PorterStemmer.stem(w)}")
    
