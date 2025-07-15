from django.shortcuts import HttpResponse, render

def index_view(request):
    return render(request, 'votar/index.html')