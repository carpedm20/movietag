#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from endless_pagination.decorators import page_template

from .models import Movie, Genre, Tag, Frequency

from utils.func import *

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

@page_template('movie/movie_item.html')
def movie_search(request,
                 text=None,
                 template='movie/movie_list.html',
                 extra_context=None):
    template = template
    page_template = 'movie/movie_item.html'

    #tag = Tag.objects.get(text=text)
    freqs = Frequency.objects.filter(tag__text=text)

    movie_list = []

    for freq in freqs:
        if freq.freq == 1:
           continue

        movie_list.append(freq.movie)

    """
    for movie in tag.movie_set.all():
        try:
            freq = Frequency.objects.get(movie=movie, tag=tag)
        except:
            freq = Frequency.objects.filter(movie=movie, tag=tag)[0]

        if freq.freq == 1:
            continue

        movie_list.append(movie)
    """

    #movie_list = add_freq_to_movie_list(movie_list)
    movie_list = movie_list[:100]

    current_account = get_account_from_user(request.user)

    data = {'movie_list': movie_list,
            'page_template': template, }

    return render_to_response(
        template, data, context_instance=RequestContext(request))

    return render(request, template, data)

def movie_list(request):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    movie_list = Movie.objects.all()[30000:30090]

    movie_list = add_freq_to_movie_list(movie_list)

    current_account = get_account_from_user(request.user)

    data = {'movie_list' : movie_list, }

    return render(request, template, data)
