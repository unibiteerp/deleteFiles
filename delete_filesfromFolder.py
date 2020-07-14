# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:08:47 2020

@author: Preeti
"""

import os
path = "C:\\Users\\Preeti\\Codes\\dataset\\tapir"
os.chdir(path)
flist = open('todelete.txt')
for f in flist:
    fname = f.rstrip() # or depending on situation: f.rstrip('\n')
    # or, if you get rid of os.chdir(path) above,
    # fname = os.path.join(path, f.rstrip())
    if os.path.isfile(fname): # this makes the code more robust
        os.remove(fname)

# also, don't forget to close the text file:
flist.close()