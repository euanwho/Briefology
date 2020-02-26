from django.shortcuts import render, redirect
from .forms import DictionaryUploadForm
from .dictionary_analysis import Dictionary

def dictionaryanalysis(request):
    form = DictionaryUploadForm()
    return render(request, 'dictionaryanalysis.html', {'form': form})

def analysisresults(request):
    if request.method == 'POST':
        form = DictionaryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('success')
        return render(request, 'analysisresults.html', {'var': 'hey'})