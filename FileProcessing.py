import os
from NLPtools import NLPtools

# distributed models names
files = "/home/vlad/Documents/CoreNLP/"
all_3class = "english.all.3class.distsim.crf.ser.gz"
conll_4class = "english.conll.4class.distsim.crf.ser.gz"
muc_7class = "english.muc.7class.distsim.crf.ser.gz"

nlp = NLPtools(files, "/home/vlad/Documents/stanford-ner-2017-06-09/")

# collect all sentences to one file and
# separate sentences from different documents by '\n*' because '…' sign  cause problems
nlp.alterto_crf_textfile("\n\n","\n","DATA/","data.txt","datatest.txt")


with open("/home/vlad/Documents/CoreNLP/datatest.txt", "r") as read_file:
    with open("/home/vlad/Documents/Tensorflow/sequence_tagging-master/data/brat/datatest_OP.txt", "w") as write_file:
        for line in read_file.readlines():
            if line.__len__() > 1:
                if line.__contains__("MONEY"):
                    line = line.split("\t")[0] + "\tO\n"
                line = line.split("\t")[0] + " " + line.split("\t")[1]
            write_file.write(line)

