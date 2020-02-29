from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from .models import Notes


def home(request):
    all_items = Notes.objects.all()
    return render(request, 'notes/home.html',
      {'all_items':all_items})

def add(request):
    new_item = Notes(description = request.POST['description'])
    new_item.save()
    return HttpResponseRedirect('/home/')

def delete(request, todoapp_id):
    del_item = Notes.objects.get(id=todoapp_id)
    del_item.delete()
    return HttpResponseRedirect('/home/')

def update(request, todoapp_id):
    try:
        sel_item = Notes.objects.get(id=todoapp_id)
    except Notes.DoesNotExist:
        return HttpResponseRedirect('/home/')
    Notes_form = NotesCreate(request.POST or None, instance = sel_item)
    if Notes_form.is_valid():
        Notes_form.save()
        return HttpResponseRedirect('/home/')
    return render(request, '/update.html', {'sel_item':sel_item})
