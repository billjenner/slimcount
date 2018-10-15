from .forms import ListForm
from django.contrib import messages
from .models import List
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# def todo_list(request):
#    return render(request, 'todo_list.html', {})

def todo_list(request):

    if request.method == 'POST':

        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Ben Added to List!'))
            return render(request, 'todo_list.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todo_list.html', {'all_items': all_items})

def about(request):
    context =  {'name': "Tom Brady", 'age': 4}
    return render(request, 'about.html', context)
    
def about2(request):
    my_name = "Tom Brady"
    return render(request, 'about2.html', {'name': my_name, 'age': 4})
    
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Ben Deleted from List!'))
    return redirect('todo_list')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo_list')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo_list')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Ben Edited!'))
        return redirect('todo_list')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})