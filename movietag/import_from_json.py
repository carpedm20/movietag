from movie.models import *
import json

f = open('movie_tag.json','r')
j=json.loads(f.read())
f.close()

for i in j['data']:
    info = i['info']
    tag_list = i['tags']

    m = Movie(title = info['title'],
              title_aka = info['title_aka'],
              title_eng = info['title_eng'],
              title_url = info['title_url'],
              main_genre = info['main_genre'],
              sub_genre = info['sub_genre'],
              year = info['year'],
              running_time = info['running_time'],
              released_at = info['released_at'],
              re_released_at = info['re_released_at'],
              other_raiting = info['raiting'],
              poster_big = info['poster_big'],
              stillcut_big = info['poster_big'],
              youtube_id = info['youtube_id'])

    m.save()

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

