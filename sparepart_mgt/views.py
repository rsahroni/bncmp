from django.shortcuts import render
from django.http import HttpResponse

title = "Sparepart Mgt"
def index(request):
    context = {
        "title": title,
        "page": "Sparepart Mgt",
    }
    return render(request, 'cmiis/sparepart_mgt.html', context)

def dimensioning(request):
    context = {
        "title": title,
        "page": "Dimensioning",
    }
    return render(request, 'bncmp/under_construction.html', context)

def inventory(request):
    context = {
        "title": title,
        "page": "Inventory",
    }
    return render(request, 'bncmp/under_construction.html', context)