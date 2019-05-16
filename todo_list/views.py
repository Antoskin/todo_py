from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ListForm(req.POST or None)

        if form.is_valid():
            form.save()
            list = List.objects.all
            messages.success(req, ('it was added!'))
            return render(req, 'home.html', {'all_items': list})

    else:
        list = List.objects.all
        return render(req, 'home.html', {'all_items': list})

def about(req):
    name = 'Antikarat'
    return render(req, 'about.html', {'name': name})

def delete(req, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(req, ('it was removed!'))
    return redirect('home')

def switch_off(req, list_id):
    item = List.objects.get(pk=list_id)

    if item.checked == False:
        item.checked = True
    else:
        item.checked = False
    #item.checked = True
    item.save()
    return redirect('home')

def edit(req, list_id):
    if req.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(req.POST or None, instance=item)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(req, 'edit.html', {'item': item})


