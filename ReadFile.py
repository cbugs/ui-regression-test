import os

def read_file_name(dir):
    path = os.getcwd() + '\\' + dir + '\\'
    file_name = []
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            # print(f)
            fullpath = os.path.join(path, f)
            log = open(fullpath, 'r')
            # print(fullpath)
            file_name.append(fullpath)
    return file_name

# one = read_file_name("temp0")
# print(one)