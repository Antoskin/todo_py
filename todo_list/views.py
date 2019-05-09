from django.shortcuts import render
from .models import List
from .forms import ListForm

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ListForm(req.POST or None)

        if form.is_valid():
            form.save()
            list = List.objects.all
            return render(req, 'home.html', {'all_items': list})

    else:
        list = List.objects.all
        return render(req, 'home.html', {'all_items': list})

def about(req):
    name = 'Antikarat'
    return render(req, 'about.html', {'name': name})