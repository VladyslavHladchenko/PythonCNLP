from NLPtools import NLPtools

nlp = NLPtools("/home/vlad/Documents/CoreNLP/", "/home/vlad/Documents/stanford-ner-2017-06-09/")

nlp.alterto_crf_trainfile("\n\n","\n","DATA/","sentences.txt")
nlp.usemodel("sentences.txt","english.all.3class.distsim.crf.ser.gz","blah.txt")

