
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
                            count += 1
                            wt_f.write(ann.read())
                            write_file.write(content)
                            write_file.write(sep) # last iteration?
        return count

    def usemodel(self, file, model, script_out):
        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + "ner.sh", model, self.files + file], stdout=f)

    def nerouttocolumns(self,inname,outname):
        with open(self.files  +  inname,'r') as in_file, open(self.files  + outname, 'w') as out_file:
            for line in in_file.read().split(' '):
                if line and not line.endswith('\n'):

                    if line.startswith('\n'):
                        line = line[1:]     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                    out_file.write(line.split('/')[0] + "\t" + line.split('/')[1] )
                    out_file.write('\n')

