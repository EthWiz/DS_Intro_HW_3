

from lib2to3.pgen2.pgen import DFAState

from sympy import re


def read_line(n, file):
    text= []
    if type(n)!= int:
        return "invalid input detected"
    else:
        try:
            fhand = open(file)
            for line in fhand:
                text.append(line)
            if n>len(text):
                return "line, {}, dosen't exist".format(n)
            else:
                return text[n-1]
        except:
            return "file not found"


