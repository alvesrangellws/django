from django.shortcuts import render

def Core(request):
    return render (request, "core/core-index.html")
