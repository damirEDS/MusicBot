from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    track_url = models.URLField()
    thumb = models.ImageField(upload_to='track_thumbnails/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
