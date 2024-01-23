from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def welcome(request):
    current_year = datetime.now().year
    return render(request, "website/welcome.html", {'year': current_year})