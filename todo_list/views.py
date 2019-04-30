from django.shortcuts import render
from .models import List

# Create your views here.
def home(req):
    list = List.objects.all
    return render(req, 'home.html', {'all_items': list})

def about(req):
    name = 'Antikarat'
    return render(req, 'about.html', {'name': name})