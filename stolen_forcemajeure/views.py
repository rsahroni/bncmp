from django.shortcuts import render

# Create your views here.
title = "Stolen & Force Majeure"
def index(request):
    context = {
        "title": title,
        "page": "Stolen & Force Majeure",
    }
    return render(request, 'bncmp/under_construction.html', context)

def dashboard(request):
    context = {
        "title": title,
        "page": "Dashboard",
    }
    return render(request, 'bncmp/under_construction.html', context)

def tracker(request):
    context = {
        "title": title,
        "page": "Tracker",
    }
    return render(request, 'bncmp/under_construction.html', context)

def sites(request):
    context = {
        "title": title,
        "page": "Sites",
    }
    return render(request, 'cmiis/sites.html', context)