from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50)

class Collection(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, related_name='collections', on_delete=models.CASCADE, blank=True)
    created_by = models.ForeignKey(User, related_name='collections')

class Combination(models.Model):
    english = models.CharField(max_length=30)
    steno = models.ManyToManyField(Steno, related_name='combinations')
    collection = models.ForeignKey(Collection, related_name='combinations', on_delete=models.CASCADE, blank=True)
    created_by = models.ForeignKey(User, related_name='combinations')

class Steno(models.Model):
    steno = models.CharField(max_length=30)

    class Meta:
        ordering = ['steno']

    def __str__(self):
        return self.steno