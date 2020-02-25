from django.shortcuts import render
from .forms import DictionaryUploadForm
## from dictionaryanalysis import 

def dictionaryanalysis(request):
    if request.method == 'POST':
        form = DictionaryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            ## handle form
            print(form)
    else:
        return render(request, 'dictionaryanalysis.html')