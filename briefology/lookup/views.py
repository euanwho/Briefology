from django.shortcuts import render
from .models import Steno, Word

def lookup(request):
    word = 'Euan'
    word = Word.objects.get(word=word)
    combinations = word.combinations.all()
    return render(request, 'lookup.html', {'combinations': combinations})