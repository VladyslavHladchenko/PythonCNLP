import os

from NLPtools import NLPtools

nlp = NLPtools("/home/vlad/Documents/CoreNLP/", "/home/vlad/Documents/stanford-ner-2017-06-09/")

#nlp.alterto_crf_textfile("\n\n","\n","DATA/","mata.txt","matatest.txt")
#nlp.usemodel("mata.txt","english.all.3class.distsim.crf.ser.gz","mata_entities.txt")
#nlp.nerouttocolumns("mata_entities.txt","mata_formated.txt")

with open("/home/vlad/Documents/CoreNLP/mata_entities.txt") as ff:
    print(    ff.read().split("\n").__len__())