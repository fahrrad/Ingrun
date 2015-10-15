from django.db import models


class WorkOfArt(models.Model):
    """class to describe general things that have been done and that will be visible on the site"""
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "%s: << %s >>" % (self.__class__.__name__, self.title)


class TheaterPlay(WorkOfArt):

    class Meta():
        verbose_name = "Theater Play"


class Movie(WorkOfArt):

    class Meta():
        verbose_name = "Movie"


class Exhibition(WorkOfArt):

    class Meta():
        verbose_name = "Exhibition"


class PressCoverage(models.Model):
    work_of_art = models.ForeignKey(WorkOfArt, null=True)
    title = models.CharField(max_length=1024)
    text = models.TextField()



