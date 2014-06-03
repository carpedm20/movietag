from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from utils.func import *

def movie_list(request):
    context = RequestContext(request)
    template = 'movie/movie_list.html'

    movie_list = Movie.objects.all()[:5]

    current_account = get_account_from_user(request.user)

    data = {'form': form,
            'post': post,
            'challenge_id': post.challenge.id,
            'user': request.user}

    return render(request, template, data)
