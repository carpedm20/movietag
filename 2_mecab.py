#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import MeCab, re
import json

from func import *

debug = True

if len(sys.argv) > 1:
    print "[*] Argv '%s' accepted" % sys.argv[1]
    unique_ids = [sys.argv[1]]
else:
    unique_ids = []

    """unique_ids.append('mevucc') # inception
    unique_ids.append('mu4tyb') # constantine
    unique_ids.append('mq867z') # classic
    unique_ids.append('mvzdp0') # Sen and chihiro
    unique_ids.append('m2vxj4') # The Thieves
    unique_ids.append('m5tttv') # The Matrix
    unique_ids.append('m8ncrz') # Finding Gimjongug
    unique_ids.append('mjtna0') # Shame
    unique_ids.append('mupzvq') # Little children
    unique_ids.append('mi2x6x') # Architecture 101
    """
    unique_ids.append('m2vxj4')

for unique_id in unique_ids:
    file_name = './data/' + unique_id + '.txt'

    try:
        f = open(file_name, 'r')
        text = f.read()
        f.close()

        if debug: print "[#] File '%s' exists" % file_name
    except:
        raise Exception("[#] File '%s' not exists" % file_name)

    j=json.loads(text)

    reviews = j['reviews']

    word_list = get_filtered_list(reviews, is_list=True)
    word_dict = {}

    for w in word_list:
        try:
            word_dict[w] += 1
        except:
            word_dict[w] = 1

    word_list = [{'text': i, 'freq': word_dict[i]} for i in word_dict]
    word_list = sorted(word_list, key=lambda k: k['freq'])

    if debug:
        for i in word_list: print "%s(%s)" % (i['text'], i['freq'])
        #for i in word_list: print i
        #for i in word_dict:
        #    print "%s : %s" % (i, word_dict[i])
        pass

    print "[#] %s (%s)" % (j['info']['title'], len(reviews))
