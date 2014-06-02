#-*- coding: utf-8 -*-
import uuid
import base64

from django.db import models

from Account.models import Account

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_aka = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    title_url = models.SlugField(max_length=50)

    main_genre = models.CharField(max_length=30, blank=True)
    sub_genre = models.CharField(max_length=30, blank=True)

    year = models.IntegerField(default=-1)
    running_time = models.IntegerField(default=-1)
    released_at = models.DateField(null=True)
    re_released_at = models.DateField(null=True)

    raiting = models.FloatField(default=0)
    other_raiting = models.FloatField(default=0)

    poster_big = models.URLField(blank=True)
    stillcut_big = models.URLField(blank=True)

    youtube_id = models.CharField(max_length=30, blank=True)

    unique_id = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            while True:
                unique_id = base64.b64encode(str(uuid.uuid4()))[:10]
                group = StudyGroup.objects.filter(unique_id=unique_id)

                if len(group) is 0:
                    self.unique_id = unique_id
                    break

        super(StudyGroup, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.title_eng)

class Tag(models.Model):
    text = models.CharField(max_length=30)

    movie_set = models.ManyToManyField(Movie)
    like_user = models.ManyToManyField(Account)

    def __unicode__(self):
        return "%s" % (self.title)

class Frequency(models.Model):
    tag = models.ForiegnKey(Tag)
    movie = models.ForiegnKey(Movie)

    freq = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s - %s" % (tag.title, self.freq)
