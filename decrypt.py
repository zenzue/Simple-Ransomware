#-*- coding: utf-8 -*-

import os
import sys
import pyaes
import base64

key = base64.b64decode(raw_input("Sifre cozme anahtari(base64): "))

fileNames = []

userPath = os.path.expanduser('~') + os.sep

docsPath   = userPath + "Documents"
docsPath2  = userPath + "Belgeler"

deskPath   = userPath + "Masaüstü"
deskPath2  = userPath + "Desktop"

musicPath  = userPath + "Müzik"
musicPath2 = userPath + "Music"

#paths = [docsPath, deskPath, musicPath, docsPath2, deskPath2, musicPath2]
paths = [userPath + "TESTPATH"]

def scan(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            fileName = os.path.basename(file)
            filePath = os.path.join(root, file)
            
            if filePath.split(".")[-1] == "vkng":
                fileNames.append(filePath)

def decrypt(fileName, key):
    aes = pyaes.AESModeOfOperationCTR(key)

    try:
        fb = open(fileName, "rb").read()
        nb = aes.decrypt(fb)

        nf = open(fileName[:-5], "wb")
        nf.write(nb)
        nf.flush()
        nf.close()

        os.remove(fileName)
    except Exception:
        pass

def main():
    for path in paths:
        try:
            scan(path)
        except:
            pass
        
    if len(fileNames) != 0:
        for file in fileNames:
            decrypt(file, key)

        print "[*] Sifreler cozuldu.!"

if __name__ == "__main__":
    main()
