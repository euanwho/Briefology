from django.db import models

class Steno(models.Model):
    steno = models.CharField(max_length=50)
    word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name='combinations', default='')

    def __str__(self):
        return self.steno

class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word