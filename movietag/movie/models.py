#-*- coding: utf-8 -*-
import uuid
import base64

from django.db import models
from djangotoolbox.fields import ListField

from account.models import Account

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_aka = models.CharField(max_length=100, null=True, blank=True)
    title_eng = models.CharField(max_length=100, null=True, blank=True)
    title_url = models.SlugField(max_length=50)

    year = models.IntegerField(default=-1, null=True)
    running_time = models.IntegerField(default=-1, null=True)
    released_at = models.DateField(null=True)
    re_released_at = models.DateField(null=True)

    rating = models.FloatField(default=0)
    other_rating = models.FloatField(default=0)

    poster_big = models.URLField(null=True, blank=True)
    stillcut_big = models.URLField(null=True, blank=True)

    youtube_id = models.CharField(max_length=30, null=True, blank=True)

    unique_id = models.CharField(max_length=10)

    main_genre = models.ForeignKey('Genre', null=True)
    sub_genre_set = models.ManyToManyField('Genre', related_name='sub_genre')
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            while True:
                unique_id = base64.b64encode(str(uuid.uuid4()))[:10]
                m = Movie.objects.filter(unique_id=unique_id)

                if len(m) is 0:
                    self.unique_id = unique_id
                    break

        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.title_eng)

class Genre(models.Model):
    text = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % (self.text)

class Tag(models.Model):
    text = models.CharField(max_length=30)

    movie_set = models.ManyToManyField(Movie)

    def __unicode__(self):
        return "%s" % (self.text)

class Frequency(models.Model):
    tag = models.ForeignKey(Tag)
    movie = models.ForeignKey(Movie, null=True)

    freq = models.IntegerField(default=0)
    like_user = models.ManyToManyField(Account)

    def __unicode__(self):
        return "%s - %s" % (self.tag.text, self.freq)
