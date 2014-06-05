#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.core.management import setup_environ
from movietag import settings
setup_environ(settings)

import json
import sys
from datetime import datetime

from movie.models import *

if len(sys.argv) >= 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
else:
    print "Need more arguments"
    sys.exit(1)

print "[#] %s to %s start!" % (start, end)

def sub_genre_to_normal(sub_genre):
    genre_list = sub_genre.split('_')
    new_list = []
    for g in genre_list:
        g = g.strip()

        if g in [u'로맨스/멜로', u'로맨틱', u'멜로', u'멜로/로맨스', u'멜로/애정/로맨스']:
            new_list.append(u'로맨스')
        elif g in [u'서스펜스']:
            new_list.append(u'스릴러')
        elif g in [u'코메디']:
            new_list.append(u'코미디')

    return new_list

def main_genre_to_normal(main_genre):
    try:
        main_genre = main_genre.strip()
    except:
        return main_genre

    if main_genre == u'로맨스/멜로':
        return u'로맨스'

    return main_genre

f = open('movie_tag.json','r')
j=json.loads(f.read())
f.close()

count = start

for i in j['data'][start:end]:
    info = i['info']
    tag_list = i['tags']

    count += 1
    print "[%s] %s" % (count, info['title'])

    try:
        m = Movie.objects.get(title = info['title'])
        print " [==>] skip"
        continue

        for tag in tag_list:
            text = tag['text']
            freq = tag['freq']
            print " => [%s] %s : %s" % (count, text, freq)

            try:
                t = Tag.objects.get(text = text)
            except:
                t = Tag(text = text)
                t.save()

            t.movie_set.add(m)
            t.save()

            f = Frequency(freq=freq)
            f.tag = t
            f.movie = m
            f.save()
    except:
        pass

    main_genre = main_genre_to_normal(info['main_genre'])
    sub_genre = sub_genre_to_normal(info['sub_genre'])

    try:
        main_genre = Genre.objects.get(text=main_genre)
    except:
        if main_genre:
            main_genre = Genre(text=main_genre)
            main_genre.save()

    sub_genre_list = []
    for sub in sub_genre:
        try:
            sub_obj = Genre.objects.get(text=sub)
        except:
            if sub:
                sub_obj = Genre(text=sub)
                sub_obj.save()

        sub_genre_list.append(sub_obj)

    try:
        released_at = datetime.strptime(info['released_at'][:10], "%Y-%m-%d")
    except:
        released_at = None
    try:
        re_released_at = datetime.strptime(info['re_released_at'][:10], "%Y-%m-%d")
    except:
        re_released_at = None

    title_url = info['title_url']

    if title_url > 50:
        title_url = title_url[:50]

    m = Movie(title = info['title'],
              title_aka = info['title_aka'],
              title_eng = info['title_eng'],
              title_url = title_url,
              year = info['year'],
              running_time = info['running_time'],
              released_at = released_at,
              re_released_at = re_released_at,
              other_rating = info['watcha_rating'],
              poster_big = info['poster']['big'],
              stillcut_big = info['stillcut']['big'],
              youtube_id = info['youtube_id'])
    m.main_genre = main_genre

    m.save()

    for sub in sub_genre_list:
        m.sub_genre_set.add(sub)

    for tag in tag_list:
        text = tag['text']
        freq = tag['freq']
        print " => [%s] %s : %s" % (count, text, freq)

        try:
            t = Tag.objects.get(text = text)
        except:
            t = Tag(text = text)
            t.save()

        t.movie_set.add(m)
        t.save()

        f = Frequency(freq=freq)
        f.tag = t
        f.movie = m
        f.save()
