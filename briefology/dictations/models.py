from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

DIFFICULTIES = ( 
    ("E", "Easy"), 
    ("M", "Medium"), 
    ("H", "Hard"), 
    ("A", "Advanced"),
) 

class Dictation(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)
    audio = models.FileField()
    transcript = models.TextField()
    words = models.TextField()
    difficulty = models.CharField( 
        max_length = 1, 
        choices = DIFFICULTIES, 
        default = 'M'
    ) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    tags = TaggableManager()
    length = models.DurationField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('dictation_detail_view', args=[str(self.slug)])

    def display_length(self):
        secs = self.length.total_seconds()
        minutes, seconds = divmod(secs, 60)
        minutes, seconds = int(minutes), int(seconds)
        return f"{minutes:02}:{seconds:02}"