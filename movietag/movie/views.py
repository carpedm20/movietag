#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Movie, Genre, Tag, Frequency

from utils.func import *

def add_freq_to_movie_list(movie_list):
    for movie in movie_list:
        movie.top_freqs = []

        tag_set = movie.tag_set.all()

        try:
            for tag in tag_set[len(tag_set)-9:len(tag_set)]:
                freqs = Frequency.objects.filter(movie=movie, tag=tag)
                for f in freqs:
                    if f.tag.text != u"영화":
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

def movie_search(request, text):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    try:
        tag = Tag.objects.get(text=text)
    except:
        tag = Tag.objects.filter(text=text)[0]

    movie_list = []
    for movie in tag.movie_set.all():
        try:
            freq = Frequency.objects.get(movie=movie, tag=tag)
        except:
            freq = Frequency.objects.filter(movie=movie, tag=tag)[0]

        if freq.freq == 1:
            continue

        movie_list.append(movie)

    movie_list = add_freq_to_movie_list(movie_list[:20])

    current_account = get_account_from_user(request.user)

    data = {'movie_list' : movie_list, }

    return render(request, template, data)

def movie_list(request):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    movie_list = Movie.objects.all()[30000:30090]

    movie_list = add_freq_to_movie_list(movie_list)

    current_account = get_account_from_user(request.user)

    data = {'movie_list' : movie_list, }

    return render(request, template, data)
