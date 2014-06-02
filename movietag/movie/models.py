from django.db import models

# Create your models here.
def Movie(models.Model):
    title = models.CharField(max_length = 100)
    title_aka = models.CharField(max_length = 100)
    title_eng = models.CharField(max_length = 100)
    title_url = models.SlugField(max_length = 50)

    unique_id = models.CharField(max_length = 10)

    main_genre = models.CharField(max_length = 30, blank=True)
    sub_genre = models.CharField(max_length = 30, blank=True)

    year = models.IntegerField()
    running_time = models.IntegerField()
    released_at = models.DateField(null=True)
    re_released_at = models.DateField(null=True)

    raiting = models.FloatField()

    poster_big = models.URLField(blank=True)
    stillcut_big = models.URLField(blank=True)

    youtube_id = models.CharField(max_length = 30, blank=True)
