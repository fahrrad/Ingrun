from django.contrib import admin

# Register your models here.
from website.models import TheaterPlay, Movie, Exhibition, PressCoverage


class WorkOfArtAdmin(admin.ModelAdmin):
    fields = ('title', 'description')


@admin.register(TheaterPlay)
class TheaterPlayAdmin(WorkOfArtAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(WorkOfArtAdmin):
    pass


@admin.register(Exhibition)
class ExhibitionAdmin(WorkOfArtAdmin):
    pass


@admin.register(PressCoverage)
class PressCoverageAdmin(admin.ModelAdmin):
    fields = ('work_of_art', 'title', 'text')