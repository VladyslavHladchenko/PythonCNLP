
import os
import subprocess


class NLPtools:
    def __init__(self, files, nlpdir):
        self.files = files
        self.nlpdir = nlpdir

    # attr1: between what the messase in file?
    # return number of processed files

    def alterto_crf_trainfile(self, envi, sep, fpath, out_name):
        # think about variants
        i = 0
        with open(self.files + out_name, 'wb') as write_file:

            for root, dirs, files in os.walk(self.files + fpath):
                for name in files:
                    if name.endswith(".txt"):
                        file_path = os.path.join(root, name)
                        with open(file_path, 'rb') as text_file:
                            i += 1
                            write_file.write(text_file.read().split(envi.encode())[1])
                            write_file.write(sep.encode()) #last iteration?
        return i

    def usemodel(self, file, model, script_out):
        f = open(self.files + script_out, "w")
        subprocess.call([self.nlpdir + "ner.sh", model, self.files + file], stdout=f)
