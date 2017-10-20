
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
    def alterto_crf_textfile(self, envi, sep, fpath, out_name, test_name):
        # think about variants
        count = 0
        with open(self.files + out_name, 'w') as write_file,  open(self.files + test_name,"w") as testfile:

            for root, dirs, files in os.walk(self.files + fpath):
                for name in files:
                    if name.endswith(".txt"):
                        file_path = os.path.join(root, name)
                        with open(file_path, 'r') as text_file, open(file_path[:-3] + "an") as ann:

                            content = text_file.read().split(envi)[1]

                            if count:
                                write_file.write(sep)
                            count += 1
                            testfile.write(ann.read())
                            write_file.write(content)

        return count

    def usemodel(self, file, model, script_out):
        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + "ner.sh", model, self.files + file,self.files + "matatest.txt"], stdout=f)

    def testmodel(self, model, script_out,test,custom = False):
        script = "nertest.sh"
        if custom:
            script = "nertestcustom.sh"

        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + script, model, self.files + test], stdout=f)

    def trainmodel(self):
        subprocess.call([self.nlpdir + "nertrain.sh"])

    def conlltocolumns(self,inname,outname):
        with open(self.files + inname, 'r') as in_file, open(self.files + outname, 'w') as out_file:
            for line in in_file.readlines():
                splitted = line.split(' ')
                if splitted.__len__() == 4:
                    type = 'O'
                    if splitted[3].__contains__('I-ORG'):
                        type = "ORGANIZATION"
                    elif splitted[3].__contains__('I-PER'):
                        type = "PERSON"

                    out_file.write(splitted[0] + '\t' + type +'\n')

    def combine_models(self):
        subprocess.call([self.nlpdir + "nercombine.sh"])

    def test_combined_model(self,model,test):
        subprocess.call([self.nlpdir + "testcombined.sh", self.nlpdir + "customclassifiers/" + model, self.files + test])


    def nerouttocolumns(self, inname, outname):
        with open(self.files  +  inname,'r') as in_file, open(self.files  + outname, 'w') as out_file:
            for line in in_file.read().split(' '):
                if line and not line.endswith('\n'):

                    if line.startswith('\n'):
                        line = line[1:]     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    splitted = line.split('/')
                    if splitted.__len__() > 2 :
                        out_file.write('/'.join(splitted[:-1]) + '\t' + splitted[-1])
                    else:
                        out_file.write(line.split('/')[0] + "\t" + line.split('/')[1] )

                    out_file.write('\n')