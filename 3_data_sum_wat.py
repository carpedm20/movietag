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

movie_dict = {}

movie_dict['data'] = []

count = 0
for file_name in review_list:
    if 'wat' in file_name:
        print count
        count += 1

        f = open(dir_name + file_name, 'r')
        j = json.loads(f.read())
        f.close()

        movie_dict['data'].append(j)

f = open('movie_review_nav.json','w')
json.dump(movie_dict, f)
f.close()
