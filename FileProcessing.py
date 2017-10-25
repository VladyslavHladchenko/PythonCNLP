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
# print( nlp.alterto_crf_textfile("\n\n","\n","DATA/","data.txt","datatest.txt"))

#nlp.usemodel("mata.txt",all,"mata_entities.txt")

# entity/TYPE[ ]... -> entity[TAB]TYPE[\n]
# nlp.nerouttocolumns("mata_entities.txt","mata_formated.txt")

# nlp.combine_models("dt.txt","combined_models_test.txt")
# nlp.test_combined_model("mucall.crf.ser.gz", "dt.txt")

nlp.conlltocolumns('Conlltrain/raw/conll2003.train.txt', 'Conlltrain/formatted/conll2003.train_formatted.txt')

new = "conll.train.crf.ser.gz"

conllold = "conll.distsim.iob2.crf.ser.gz"
conllold2 = "conll.closed.iob2.crf.ser.gz"

#nlp.trainmodel('conll.prop')
#nlp.trainmodel('conll1.prop')
#nlp.trainmodel('conll2.prop')


# nlp.testmodel("conll.train_testab_p_t_n.crf.ser.gz","ner.out","d/lexis1part.txt",custom=True)



# nytimes = "nytimes"
# pehub = "pehub"
# techcrunch  = "techcrunch"
#
# with open(files + "d/" + techcrunch + ".txt", 'w') as ann:
#     for root, dirs, files in os.walk(files + "DATA/" + techcrunch):
#         for name in files:
#             if name.endswith(".an"):
#                 file_path = os.path.join(root, name)
#                 with open(file_path, 'r') as text_file:
#                     ann.write(text_file.read())







