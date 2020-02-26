from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
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
    update_item = Notes.objects.get(id=todoapp_id)
    update_item = Notes(description = request.POST['description'])
    update_item.save()
    return HttpResponseRedirect('/home/')
