import os
from NLPtools import NLPtools

# distributed models names
all_3class = "english.all.3class.distsim.crf.ser.gz"
conll_4class = "english.conll.4class.distsim.crf.ser.gz"
muc_7class = "english.muc.7class.distsim.crf.ser.gz"

nlp = NLPtools("/home/vlad/Documents/CoreNLP/", "/home/vlad/Documents/stanford-ner-2017-06-09/")

# collect all sentences to one file and
# separate sentences from different documents by '\n*' because '…' sign  cause problems
# print( nlp.alterto_crf_textfile("\n\n","\n","DATA/","data.txt","datatest.txt"))

#nlp.usemodel("mata.txt",all,"mata_entities.txt")

# entity/TYPE[ ]... -> entity[TAB]TYPE[\n]
# nlp.nerouttocolumns("mata_entities.txt","mata_formated.txt")

# nlp.testmodel(all_3class, "new.log", 'Conlltrain/formatted/conll2003.testab_formatted.txt')
# nlp.testmodel(conll_4class, "new.log", 'Conlltrain/formatted/conll2003.train_formatted.txt')

#with open("/home/vlad/Documents/CoreNLP/datatest.txt") as norm, open("/home/vlad/Documents/CoreNLP/dt.txt", 'w') as fake:
 #   for line in norm.readlines():
  #      fake.write(line.split('\t')[0] +"\tNT\t" + line.split('\t')[1])

# nlp.combine_models("dt.txt","combined_models_test.txt")
# nlp.test_combined_model("mucall.crf.ser.gz", "dt.txt")

# nlp.conlltocolumns('Conlltrain/raw/conll2003.train.txt', 'Conlltrain/formatted/conll2003.train_formatted.txt')
# nlp.trainmodel()

new = "conll.train.crf.ser.gz"

conllold = "conll.distsim.iob2.crf.ser.gz"
conllold2 = "conll.closed.iob2.crf.ser.gz"