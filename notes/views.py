from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from .models import Notes
from .forms import NotesCreate

def home(request):
    all_items = Notes.objects.all()
    print('----------> all items :', all_items)
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

def edit(request, todoapp_id):
    sel_item = Notes.objects.get(id=todoapp_id)
    return render(request,'notes/update.html', {'sel_item':sel_item})

def update(request, todoapp_id):
    try:
        sel_item = Notes.objects.get(id=todoapp_id)
    except Notes.DoesNotExist:
        return HttpResponseRedirect('/home/')
    Notes_form = NotesCreate(request.POST, instance = sel_item)
    if Notes_form.is_valid():
        Notes_form.save()
        return redirect("/home")
        # return HttpResponseRedirect('/home/')
    return render(request, 'notes/update.html', {'sel_item':sel_item})
