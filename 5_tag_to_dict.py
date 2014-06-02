#!/usr/bin/python
import json

f = open('movie_tag.json','r')
j = json.loads(f.read())
f.close()

tag_dict = {}

new_j = {}
new_j['data'] = []

for i in j['data']:
    for t in i['tags']:
        text = t['text']
        freq = t['freq']

        try:
            tag_dict[text] += freq
        except:
            tag_dict[text] = freq

for i in tag_dict:
    new_j['data'].append({'text':i, 'freq':tag_dict[i]})

f = open('tag_dict.json','w')
json.dump(new_j, f)
f.close()
