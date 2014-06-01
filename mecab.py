#-*- coding: utf-8 -*-
import sys
import MeCab, re

from config import MECAB_KO_DIC_PATH

debug = True

MECAB_OPTION = "-d " + MECAB_KO_DIC_PATH

m = MeCab.Tagger(MECAB_OPTION)

unique_ids = []

"""unique_ids.append('mevucc') # inception
unique_ids.append('mu4tyb') # constantine
unique_ids.append('mq867z') # classic
unique_ids.append('mvzdp0') # Sen and chihiro
unique_ids.append('m2vxj4') # The Thieves
unique_ids.append('m5tttv') # The Matrix
unique_ids.append('m8ncrz') # Finding Gimjongug
"""
unique_ids.append('m8ncrz') # Finding Gimjongug

"""
NNG  일반 명사
NNP  고유 명사
NNB  의존 명ì¬
NNBC 단위를 나타내는 명사
NR   수사
NP   대명사
VV   동사
VA   형용사
VX   보조 용언
VCP  긍정 지정사
VCN  부정 지정사
"""

BASIC_OPTION = ['NNG', 'NNP', 'NR']
COMPACT_OPTION = ['NNP', 'NR']
OPTION1 = ['VV', 'VA', 'VX', 'VCP', 'VCN', ]

def get_filtered_list(words, options = BASIC_OPTION):
    global m

    filtered_list = []
    node = m.parseToNode(words)

    while node:
        #print node.surface + '\t' + node.feature
        if node.feature.split(",")[0] in options:
            replace_node = re.sub(re.compile("[!-/:-@[-`{-~]"), "", node.surface)
            if replace_node != "" and replace_node != " ":
                #filtered_list.append("%s : %s" % (replace_node, node.feature))
                filtered_list.append(replace_node)

        node = node.next

    return filtered_list

for unique_id in unique_ids:
    file_name = './data/' + unique_id + '.txt'

    try:
        f = open(file_name, 'r')
        text = f.read()
        f.close()

        if debug: print "[#] File '%s' exists" % file_name
    except:
        raise Exception("[#] File '%s' not exists" % file_name)

    word_list = get_filtered_list(text)
    word_dict = {}

    for w in word_list:
        try:
            word_dict[w] += 1
        except:
            word_dict[w] = 1

    word_list = [{'text': i, 'freq': word_dict[i]} for i in word_dict]
    word_list = sorted(word_list, key=lambda k: k['freq'])

    if debug:
        for i in word_list: print i['text'] + " : " + str(i['freq'])
        #for i in word_list: print i
        #for i in word_dict:
        #    print "%s : %s" % (i, word_dict[i])
        pass

