from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "title": "Home",
        "page": "Home",
    }
    return render(request, 'cmiis/index.html', context)