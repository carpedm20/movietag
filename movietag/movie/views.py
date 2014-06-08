#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Movie, Genre, Tag, Frequency

from utils.func import *

#######################
# mongo-engine
#######################

from mongoengine import connect, Document, DictField, ListField

connect('carpedm20')

class Movie(Document):
    info = DictField()
    tags = ListField(DictField())

# Django version
def add_freq_to_movie_list(movie_list):
    for movie in movie_list:
        movie.top_freqs = []

        tag_set = movie.tag_set.all()

        try:
            for tag in tag_set[len(tag_set)-9:len(tag_set)]:
                if tag.text == u'영화':
                    continue

                freqs = Frequency.objects.filter(movie=movie, tag=tag)

                for f in freqs:
                    movie.top_freqs.append(f)
        except:
            pass

        if 'default' in movie.poster_big:
            pass
            #movie.poster_big = "http://www.seenth.at/img/st_default_poster_chatter.png"
    return movie_list

def index(request):
    template = 'index.html'

    return render(request, template)

def movie_search(request, text=None):
    """
    Version 3 (MongoDB)
    """
    template = 'movie/movie_list_mongo.html'
    page_template = 'movie/movie_item_mongo.html'

    movie_list = Movie.objects(__raw__={"tags.%s" %text:{"$gt":0}})

    movie_list = movie_list[:40]

    new_movie_list = []

    for movie in movie_list:
        m = {}
        m['title'] = movie.info['title']
        m['other_rating'] = movie.info['watcha_rating']
        m['poster'] = movie.info['poster']['big']

        m['tags'] = []

        for tag in movie.tags[-10:]:
            key = tag.keys()[0]
            if key == u'영화':
                continue
            value = tag.values()[0]

            t = {'key':key, 'value':value}
            m['tags'].append(t)

        new_movie_list.append(m)

    """
    Version 2

    template = 'movie/movie_list.html'
    page_template = 'movie/movie_item.html'

    #tag = Tag.objects.get(text=text)
    freqs = Frequency.objects.filter(tag__text=text)

    movie_list = []

    for freq in freqs:
        if freq.freq == 1:
           continue

        movie_list.append(freq.movie)

    movie_list = add_freq_to_movie_list(movie_list[:20])

    """

    """
    Version 1

    for movie in tag.movie_set.all():
        try:
            freq = Frequency.objects.get(movie=movie, tag=tag)
        except:
            freq = Frequency.objects.filter(movie=movie, tag=tag)[0]

        if freq.freq == 1:
            continue

        movie_list.append(movie)

    #movie_list = movie_list[:100]
    """

    current_account = get_account_from_user(request.user)

    data = {'movie_list': new_movie_list, }

    return render(request, template, data)

def movie_list(request):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    movie_list = Movie.objects.all()[30000:30090]

    movie_list = add_freq_to_movie_list(movie_list)

    current_account = get_account_from_user(request.user)

    data = {'movie_list' : movie_list, }

    return render(request, template, data)
