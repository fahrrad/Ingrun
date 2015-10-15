from django.contrib import admin

# Register your models here.
from website.models import TheaterPlay, Movie, Exhibition, PressCoverage


@admin.register(TheaterPlay)
class TheaterPlayAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    pass


@admin.register(PressCoverage)
class PressCoverageAdmin(admin.ModelAdmin):
    fields = ('work_of_art', 'title', 'text')