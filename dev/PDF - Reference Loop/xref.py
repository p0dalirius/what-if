#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    for e in data:
        f.write(e)
    f.close()
    return data

class XREF_Maker(object):
    """docstring for XREF_Maker."""

    def __init__(self, pdffile):
        super(XREF_Maker, self).__init__()
        self.pdffile = pdffile
        self.rawdata = []
        self.load()
        self.remove_xref()

    def load(self):
        """Documentation for load"""
        f = open(self.pdffile, "rb")
        self.rawdata = f.readlines()
        f.close()
        return

    def remove_xref(self):
        """Documentation for remove_xref"""
        for k in range(len(self.rawdata)):
            line = self.rawdata[k]
            if b'startxref' in line : xref_in = k
        self.rawdata = self.rawdata[:xref_in] + [b'%%EOF\n']
        for e in self.rawdata : print(e)
        return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" pdffile")
    else :
        pdffile = sys.argv[1]
        xm = XREF_Maker(pdffile)


# startxref
# 111945
# xref
# 0 3
# 0000000000 65535 f
# 0000000024 00000 n
# 0000000103 00000 n
# 0000000202 00000 n
# 0000000106 00000 n
# 0000000153 00000 n
# 00000001A3 00000 n
# %%EOF
