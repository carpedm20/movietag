#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import MeCab, re
import json

from func import *

from config import MECAB_KO_DIC_PATH

debug = True

MECAB_OPTION = "-d " + MECAB_KO_DIC_PATH

m = MeCab.Tagger(MECAB_OPTION)

"""
# https://docs.google.com/spreadsheet/ccc?key=0ApcJghR6UMXxdEdURGY2YzIwb3dSZ290RFpSaUkzZ0E&usp=sharing#gid=4
NNG  일반 명사
NNP  고유 명사
NNB  의존 명사 x
NNBC 단위를 나타내는 명사 x
NR   수사 x
NP   대명사 x
VV   동사 ㅅ
VA   형용사 o
VX   보조 용언 x
VCP  긍정 지정사 x
VCN  부정 지정사 x
MM   관형사 ㅅ - 이따위 그깟 요런, 이딴 | 각, 뭔, 새, 온, 제, 내
MAG  부사 o - 너무너무 전혀 살짝 특히 빵빵 정말 진짜 너무 안 잘 그닥 짱
MAJ  접속 부사 x - 그러나 그리고 
IC   감탄사 x - 음 아 어 뭐 오 아우 헐 엇 
SL   외국어
SH   한자
SN   숫자
"""

BASIC_OPTION = ['NNG', 'NNP', 'NR']
COMPACT_OPTION = ['NNP', 'NR']
OPTION1 = ['VV', 'VA', 'VX', 'VCP', 'VCN', ]

debug = True
#debug = False

if len(sys.argv) > 1:
    print "[*] Argv '%s' accepted" % sys.argv[1]
    unique_ids = [sys.argv[1]]
else:
    unique_ids = []

    """unique_ids.append('52548') # 의형제
    unique_ids.append('73344') # 초능력자
    unique_ids.append('44529') # 해바라기
    unique_ids.append('75401') # 헬로우 고스트
    unique_ids.append('17421') # 쇼생크 탈출
    unique_ids.append('72408') # 악마를 보았다
    unique_ids.append('54411') # 우리들의 행복한 시간
    unique_ids.append('58088') # 라디오 스타
    unique_ids.append('69986') # 황해
    unique_ids.append('73318') # 시라노; 연애조작단
    """
    unique_ids.append('73318')

for unique_id in unique_ids:
    file_name = './data/naver_' + unique_id + '.json'

    try:
        f = open(file_name, 'r')
        text = f.read()
        f.close()

        if debug: print "[#] File '%s' exists" % file_name
    except:
        raise Exception("[#] File '%s' not exists" % file_name)

    j=json.loads(text)

    reviews = [i['review'] for i in j['stars']]

    #word_list = get_filtered_list(reviews, is_list=True)
    word_dict = {}

    hangul = re.compile('[^ \.\,\?\!a-zA-Z0-9\u3131-\u3163\uac00-\ud7a3]+')

    for i in reviews:
        node = m.parseToNode(i.encode('utf-8'))
        while node:
            #if node.feature.split(',')[0] in ['NNG', 'NNP', 'NR']
            if node.feature.split(',')[0] in ['VV', 'VA', 'MM', 'MAG']:
            #if node.feature.split(',')[0] in ['VCP', 'VCN', 'MM']:
            #if node.feature.split(',')[0] in ['MAG', 'MAJ', 'IC']:
            #if node.feature.split(',')[0] in ['SL', 'SH', 'SN']:
                try:
                    word = hangul.findall(node.surface)[0]+"-"+node.feature.split(',')[0]

                    try:
                        word_dict[word] += 1
                    except:
                        word_dict[word] = 1
                except:
                    pass
            node=node.next

    word_list = [{'text': i, 'freq': word_dict[i]} for i in word_dict]
    word_list = sorted(word_list, key=lambda k: k['freq'])

    if debug:
        for i in word_list: print "%s(%s)" % (i['text'], i['freq'])
        #for i in word_list: print i
        #for i in word_dict:
        #    print "%s : %s" % (i, word_dict[i])
        pass

    #print "[#] %s (%s)" % (j['info']['title'], len(reviews))
