'''
simple module for getting a concordances of a certain word.

'''
import nltk
import sys

# first we open the corpus which is in the same directory as the module 
corp = open('corpus.txt', 'r')
raw = corp.read()

# tokenizer is needed to proccess the file
tokens = nltk.wordpunct_tokenize(raw)
corpus = nltk.Text(tokens)

# we will get the concordances
corpus.concordance("word") # put the word in ""

# we write the result in a text file
fileconcord = open('ccord-result.txt', 'w')
fileconcord.writelines(corpus)
fileconcord.close()
