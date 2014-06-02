from movie.models import *
import json

f = open('movie_tag.json','r')
j=json.loads(f.read())

for i in j['data']:
    info = i['info']
    tag_list = i['tags']


