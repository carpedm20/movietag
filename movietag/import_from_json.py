#-*- coding: utf-8 -*-
from movie.models import *
import json

def sub_genre_to_normal(sub_genre):
    genre_list = sub_genre.split('_')
    new_list = []
    for g in genre_list:
        g = g.strip()

        if g in ['로맨스/멜로', '로맨틱', '멜로', '멜로/로맨스', '멜로/애정/로맨스']:
            new_list.append('로맨스')
        elif g in ['서스펜스']:
            new_list.append('스릴러')
        elif g in ['코메디']:
            new_list.append('코미디')

    return new_list

def main_genre_to_normal(main_genre):
    main_genre = main_genre.strip()

    if main_genre == '로맨스/멜로':
        return '로맨스'

    return main_genre

f = open('movie_tag.json','r')
j=json.loads(f.read())
f.close()

count = 0
for i in j['data']:
    info = i['info']
    tag_list = i['tags']

    count += 1
    print "[%s] %s" % (count, info['title'])

    main_genre = main_genre_to_normal(info['main_genre'])
    sub_genre = sub_genre_to_normal(info['sub_genre'])

    try:
        main_genre = Genre.objects.get(text=main_genre)
    except:
        main_genre = Genre(text=main_genre)

    sub_genre_list = []
    for sub in sub_genre:
        try:
            sub_obj = Genre.objects.get(text=sub)
        except:
            sub_obj = Genre(text=sub)

        sub_genre_list.append(sub_obj)

    m = Movie(title = info['title'],
              title_aka = info['title_aka'],
              title_eng = info['title_eng'],
              title_url = info['title_url'],
              year = info['year'],
              running_time = info['running_time'],
              released_at = info['released_at'],
              re_released_at = info['re_released_at'],
              other_rating = info['watcha_rating'],
              poster_big = info['poster']['big'],
              stillcut_big = info['stillcut']['big'],
              youtube_id = info['youtube_id'])
    m.save()

    m.main_genre = main_genre

    for sub in sub_genre_list:
        m.sub_genre_set.add(sub)

    for tag in tag_list:
        text = tag['text']
        freq = tag['freq']

        try:
            t = Tag.objects.get(text = text)
        except:
            t = Tag(text = text)
            t.save()

        t.movie_set.add(m)
        t.save()

        f = Frequency(freq=freq)
        f.save()

        f.tag = t
        f.movie = m
        f.save()

