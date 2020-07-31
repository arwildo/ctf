#!/usr/bin/env python3
import os
import filetype

def main():
    try:
        fl = os.listdir("./room")
        fl_path = "./room/%s" % "".join(map(str, fl))

        kind = filetype.guess(fl_path)
        print(kind.extension)
        if kind.extension == "gz":
            os.system("./gzip.sh %s" % fl_path)
        elif kind.extension == "bz2":
            os.system("./bzip2.sh %s" % fl_path)
        elif kind.extension == "zip":
            os.system("./zip.sh %s" % fl_path)
        elif kind.extension == "xz":
            os.system("./xz.sh %s" % fl_path)
        else:
            print("Not found!")
    except:
        print("Error!!!")
    

if __name__ == '__main__':
    while True:
        main()
