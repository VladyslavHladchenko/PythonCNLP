import os
from NLPtools import NLPtools

all = "english.all.3class.distsim.crf.ser.gz"
conll = "english.conll.4class.distsim.crf.ser.gz"
muc = "english.muc.7class.distsim.crf.ser.gz"

nlp = NLPtools("/home/vlad/Documents/CoreNLP/", "/home/vlad/Documents/stanford-ner-2017-06-09/")

# collect all sentences to one file and
# separate sentences from different documents by '\n*' because '…' sign  cause problems
print( nlp.alterto_crf_textfile("\n\n","\n","MATA/","MA/mata.txt"))

nlp.usemodel("MA/mata.txt",all,"MA/mata_entities.txt")

# entity/TYPE[ ]... -> entity[TAB]TYPE[\n]
nlp.nerouttocolumns("MA/mata_entities.txt","MA/mata_formated.txt")