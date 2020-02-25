from django.shortcuts import render, redirect
from .forms import DictionaryUploadForm
from .dictionaryanalysis import Dictionary, WordList, Analyser
## from dictionaryanalysis import 

def dictionaryanalysis(request):
    if request.method == 'POST':
        form = DictionaryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Success')
        return redirect('analysisresults')
    else:
        form = DictionaryUploadForm()
        return render(request, 'dictionaryanalysis.html', {'form': form})

def analysisresults(request):
    return render(request, 'analysisresults.html')