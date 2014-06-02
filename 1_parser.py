#!/usr/bin/python
import requests
import json
import sys
from os import listdir
from config import *
from random import shuffle

debug = True

proxies={'http':'http://127.0.0.1:9666'}

if len(sys.argv) > 1:
    print "[*] Argv '%s' accepted" % sys.argv[1]
    unique_ids = [sys.argv[1]]
else:
    f=open('new_ids.json','r')
    j=json.loads(f.read())
    f.close()

    unique_ids=j['ids']

    """
    f=open('total.json','r')
    j=json.loads(f.read())
    f.close()

    unique_ids=[i['id'] for i in j]

    already_parsed_list = listdir('./data/')
    already_parsed_ids = [i[:-4] for i in already_parsed_list]

    unique_ids = [i for i in unique_ids if i not in already_parsed_ids]
    """

shuffle(unique_ids)

count = 0
for unique_id in unique_ids:
    print "[*] Current : %s" % count
    count += 1

    file_name = './data/' + unique_id + '.txt'

    try:
        f = open(file_name, 'r')
        text = f.read()
        f.close()

        if debug: print "[#] File '%s' is exist" % file_name
    except:
        for i in range(10):
            try:
                movie_dict = {}
                movie_dict['reviews'] = []

                try:
                    r=requests.get(DETAIL_URL % unique_id, proxies=proxies)
                except:
                    raise Exception("[!!!] requests error [!!!]")

                j=json.loads(r.text)

                title = j['data']['movie']['title']
                comment_count = j['data']['movie']['comment_count']
                movie_dict['info'] = j['data']['movie']

                print " ==> %s - comment_count : %s" % (title, comment_count)

                if comment_count != 0:
                    """
                    if comment_count > 1000:
                        len_for_each_count = 50
                        current_count = 
                    """

                    data = {'unique_id': unique_id,
                            'start_index': 0,
                            'count': comment_count,
                            'type': 'like'}

                    try:
                        r=requests.get(REVIEW_URL, params=data, proxies=proxies)
                    except:
                        raise Exception("[!!!] requests error [!!!]")

                    j=json.loads(r.text)

                    if debug: print "[*] length of data : %s" % len(j['data'])

                    for i in j['data']:
                        movie_dict['reviews'].append(i['text'].encode('utf-8'))

                f = open(file_name, 'w')
                json.dump(movie_dict, f)
                f.close()
                break
            except:
                continue
