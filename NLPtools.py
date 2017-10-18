
import os
import subprocess
from collections import OrderedDict

class NLPtools:
    def __init__(self, files, nlpdir):
        self.files = files
        self.nlpdir = nlpdir

    # attr1: between what the text in file?
    # return number of processed files
    # makes testfile too
    def alterto_crf_textfile(self, envi, sep, fpath, out_name,testname):
        # think about variants
        count = 0
        with open(self.files + out_name, 'w') as write_file, open(self.files + testname,"w") as wt_f:

            for root, dirs, files in os.walk(self.files + fpath):
                for name in files:
                    if name.endswith(".txt"):
                        file_path = os.path.join(root, name)
                        with open(file_path, 'r') as text_file, open(file_path[:-3] + "an") as ann:
                            content = text_file.read().split(envi)[1]

                            if count:
                                wt_f.write(sep[1:])
                                write_file.write(sep)
                            count += 1
                            wt_f.write(ann.read())
                            write_file.write(content)

        return count

    def usemodel(self, file, model, script_out):
        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + "ner.sh", model, self.files + file,self.files + "matatest.txt"], stdout=f)

    def testmodel(self, file, model, script_out,test):
        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + "nertest.sh", model, self.files + test], stdout=f)

    def nerouttocolumns(self,inname,outname):
        with open(self.files  +  inname,'r') as in_file, open(self.files  + outname, 'w') as out_file:
            for line in in_file.read().split(' '):
                if line and not line.endswith('\n'):

                    if line.startswith('\n'):
                        line = line[1:]     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                    out_file.write(line.split('/')[0] + "\t" + line.split('/')[1] )
                    out_file.write('\n')


    def binaryClassification(self, testfile, formattedout):
        count =0
        with open(self.files + testfile,'r') as test, open(self.files + formattedout,'r') as nerout, open(
                        self.files +"differencies.txt", 'w') as diff:
            testentities = test.read().split('\n*')
            nerentities = nerout.read().split('\n*\tO\n')
            for test, ner in zip(testentities,nerentities):
                if test.split('\n').__len__() != ner.split('\n').__len__():

                    count +=1
                    diff.write('\n\t\t\t\t\tTEST \t\t\t' + str( test.split('\n').__len__() - ner.split('\n').__len__() )+'\n')
                    diff.write(test)
                    diff.write('\n\t\t\t\t\tNER\n')
                    diff.write(ner)
                    diff.write('\n------------------------------------------------------------------\n')
        #print(count)
