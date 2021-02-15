

import os, sys
from os import read, write

nextCharIndex = 0
ibuf = 0

def getChar():
        global nextCharIndex 
        global ibuf
       
        if nextCharIndex == ibuf:
                nextCharIndex = 0;
                ibuf = read(0, 100)
        
                if ibuf == 0:
                        return "EOF"
                
        if nextCharIndex < len(ibuf) - 1:
                sbuf = ibuf.decode()
                char = sbuf[nextCharIndex]
                nextCharIndex += 1
                return char
        else:
                return "EOF"


def myReadlines():
        global nextCharIndex
        global ibuf
        char = getChar()
        line = ""

        while (char != '' and char != "EOF"):
                line += char
                char = getChar()
                
        nextCharIndex = 0
        ibuf = 0
        
        return line
