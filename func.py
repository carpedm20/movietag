#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import MeCab, re
import json

from config import MECAB_KO_DIC_PATH

debug = True

MECAB_OPTION = "-d " + MECAB_KO_DIC_PATH

m = MeCab.Tagger(MECAB_OPTION)

"""
NNG  일반 명사
NNP  고유 명사
NNB  의존 명사
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

def get_filtered_list(words, is_list = False, options = BASIC_OPTION):
    global m

    text = ""
    if is_list:
        for i in words:
            text += i + "\n"

    filtered_list = []
    node = m.parseToNode(text.encode('utf-8'))

    while node:
        #filtered_list.append(node.feature.split(",")[0])

        #print node.surface + '\t' + node.feature
        #if node.feature.split(",")[0] in options:
        #    replace_node = re.sub(re.compile("[!-/:-@[-`{-~]"), "", node.surface)
        #    if replace_node != "" and replace_node != " ":
                #filtered_list.append("%s : %s" % (replace_node, node.feature))
        word = node.surface.strip()
        print word

        if word != '':
            filtered_list.append(word)

        node = node.next

    return filtered_list

