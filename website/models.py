from django.db import models


class WorkOfArt(models.Model):
    """class to describe general things that have been done and that will be visible on the site"""
    description = models.TextField()


class TheaterPlay(WorkOfArt):

    class Meta():
        verbose_name = "Theater Play"


class Movie(WorkOfArt):

    class Meta():
        verbose_name = "Movie"


class Exhibition(WorkOfArt):

    class Meta():
        verbose_name = "Exhibition"


