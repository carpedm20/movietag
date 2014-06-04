#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Movie, Genre, Tag, Frequency

from utils.func import *

def index(request):
    template = 'index.html'

    return render(request, template)

def movie_list(request):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    movie_list = Movie.objects.all()[:70]

    for movie in movie_list:
        movie.top_freqs = []

        tag_set = movie.tag_set.all()

        try:
            for tag in tag_set[len(tag_set)-5:len(tag_set)]:
                freqs = Frequency.objects.filter(movie=movie, tag=tag)
                for f in freqs:
                    if f.tag.text != u"영화":
                        movie.top_freqs.append(f)
        except:
            pass

        if 'default' in movie.poster_big:
            pass
            #movie.poster_big = "http://www.seenth.at/img/st_default_poster_chatter.png"

    current_account = get_account_from_user(request.user)

    data = {'movie_list' : movie_list, }

    return render(request, template, data)
