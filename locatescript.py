'''
Date: 02-06-2016
Name: diegosenco
Program: locatescript.py
'''

import os
import datetime


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def condition(name):
    '''
    Condition that the file needs to satisfy. In this case, the
    condition is that the modification date should be between lim1
    and lim2, and the file type is a python script.
    '''
    m = modification_date(name)
    lim1 = datetime.datetime(2015, 1, 1)
    lim2 = datetime.datetime(2016, 1, 1)
    return lim1 < m and m < lim2 and name.endswith('.py')


Folders = os.walk('./')
for files in Folders:
    for f in files[2]:
        filename = files[0] + '/' + f
        if os.path.islink(filename):
            continue
        if condition(filename):
            print filename

