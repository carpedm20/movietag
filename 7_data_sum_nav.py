#!/usr/bin/python
import requests
import json
import sys
from os import listdir
from config import *
from random import shuffle

from func import *

debug = True

dir_name = './data/'
review_list = listdir(dir_name)

movie_list = []

count = 0
for file_name in review_list:
    if 'nav' in file_name:
        print count
        count += 1

        if count > 50000:
            break
            #continue

        f = open(dir_name + file_name, 'r')
        try:
            j = json.loads(f.read())
            print len(j)
        except:
            print "ERROR"
            continue
        f.close()

        movie_list.append(j)

f = open('movie_review_nav_1.json','w')
#f = open('movie_review_nav_2.json','w')

json.dump(movie_list, f)
f.close()
