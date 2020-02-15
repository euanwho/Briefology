from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

PUB_PRIV = {
    ('P', 'Public'),
    ('R', 'Private')
}

class BriefList(models.Model):
    name = models.CharField(max_length=30, default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='P', choices=PUB_PRIV)

    def __str__(self):
        return self.status

class Dictionary(models.Model):
    name = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='P', choices=PUB_PRIV)

    def __str__(self):
        return self.name

class Steno(models.Model):
    steno = models.CharField(max_length=50)
    word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name='combinations', default='', db_index=True)
    source = models.ForeignKey(Dictionary, on_delete=models.SET_NULL, null=True, related_name='entries')
    brief_list = models.ManyToManyField(BriefList)
    dictionary = models.ManyToManyField(Dictionary)

    class Meta():
        ordering = ['steno']
    
    def __str__(self):
        return self.steno

    def __len__(self):
        return len(self.steno)

class Word(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word