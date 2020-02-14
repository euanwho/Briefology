from django.db import models
from django.utils import timezone
class Dictionary(models.Model):
    name = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Steno(models.Model):
    steno = models.CharField(max_length=50)
    word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name='combinations', default='', db_index=True)
    source = models.ForeignKey(Dictionary, on_delete=models.SET_NULL, null=True, related_name='entries')

    class Meta():
        ## add logic for if there is a slash in steno and if not?
        ordering = ['steno']

    def __str__(self):
        return self.steno

class Word(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word