from django.shortcuts import render

def Enquetes(request):
    return render(request, "enquetes/enquetes.html")
