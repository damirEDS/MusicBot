from django.contrib import admin
from .models import Artist, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'website', 'date_created', 'date_modified')
    search_fields = ('name',)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'date_created', 'date_modified')
    list_filter = ('artist',)
    search_fields = ('title', 'artist__name', 'album__title')
