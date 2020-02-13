from django.shortcuts import render

def lookup(request):
    return render(request, 'lookup.html')