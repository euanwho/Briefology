from django.shortcuts import render
from .models import Dictation
from .filters import DictationFilter

def dictation_list_view(request):
    dictations = Dictation.objects.all()
    return render(request, 'dictations.html', {'dictations': dictations})

def dictation_detail_view(request, slug):
    dictation = Dictation.objects.get(slug=slug)
    return render(request, 'dictation.html', {'dictation':dictation})

def search(request):
    dictation_list = Dictation.objects.all()
    dictation_filter = DictationFilter(request.GET, queryset=dictation_list)
    return render(request, 'search.html', {'filter': dictation_filter})
