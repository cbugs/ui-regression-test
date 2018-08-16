import os
import shutil

def remove_files(dir):
    path = os.getcwd() + '\\' + dir + '\\'

    shutil.rmtree(path)
    os.mkdir(path)