#!/usr/bin/python
import requests
import json
import sys
from os import listdir
from config import *
from random import shuffle

from func import *

debug = True

f = open('movie_review.json', 'r')
j = json.loads(f.read())
f.close()

movie_dict = {}

movie_dict['data'] = []

count = 0
for i in j['data']:
    print count
    count += 1

    new_j = {}

    info = i['info']
    reviews = i['reviews']

    print len(reviews)

    new_j['info'] = info

    word_list = get_filtered_list(reviews, is_list=True)
    word_dict = {}

    for w in word_list:
        try:
            word_dict[w] += 1
        except:
            word_dict[w] = 1

    word_list = [{'text': i, 'freq': word_dict[i]} for i in word_dict]
    word_list = sorted(word_list, key=lambda k: k['freq'])

    new_j['tags'] = word_list

    movie_dict['data'].append(new_j)

f = open('movie_tag.json','w')
json.dump(movie_dict, f)
f.close()
