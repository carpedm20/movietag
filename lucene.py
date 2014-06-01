import requests
import json
from korean import get_word_list
from config import *

debug = True

unique_ids = []

"""unique_ids.append('mevucc') # inception
unique_ids.append('mu4tyb') # constantine
unique_ids.append('mq867z') # classic
unique_ids.append('mvzdp0') # Sen and chihiro
unique_ids.append('m2vxj4') # The Thieves
unique_ids.append('m5tttv') # The Matrix
unique_ids.append('m8ncrz') # Finding Gimjongug
"""
unique_ids.append('mvzdp0') # Sen and chihiro

for unique_id in unique_ids:
    file_name = './data/' + unique_id + '.txt'

    try:
        f = open(file_name, 'r')
        text = f.read()
        f.close()

        if debug: print "[#] File '%s' exists" % file_name
    except:
        raise Exception("[#] File '%s' not exists" % file_name)

    word_list = get_word_list(text)

    max_count = 0

    word_list = sorted(word_list, key=lambda k: k['freq']) 
    text_list = [i['text'] for i in word_list]

    word_dict = {}

    for i in word_list:
        word_dict[i['text']] = i['freq']

    # word in word delete filter
    delete_list = []

    for i in word_list:
        text, freq = i['text'], i['freq']

        for t in text_list:
            if text == t:
                continue
            if text in t:
                #print " [*] %s(%s) vs %s(%s)" %(text, word_dict[text], t, word_dict[t])
                if word_dict[text] == word_dict[t]:
                    delete_list.append(text)
                elif word_dict[text] > word_dict[t]:
                    delete_list.append(t)
                else:
                    delete_list.append(text)

    new_word_list = [w for w in word_list if w['text'] not in delete_list]

    if debug:
        for i in new_word_list: print i['text'] + " : " + str(i['freq'])
        #for i in word_list: print i['text'] + " : " + str(i['freq'])
