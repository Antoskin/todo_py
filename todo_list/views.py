from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    name = 'Antikarat'
    return render(req, 'about.html', {'name': name})