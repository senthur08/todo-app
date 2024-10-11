from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def lists(request):
    tasks= Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context={
        'tasks':tasks,
        'form':form
    }
    return render(request, 'tasks/lists.html',context)

def updateTask(request, pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    context={
        'form':form
    }
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')
    return render(request, 'tasks/update_task.html', context)

def delete(request, pk):
    task=Task.objects.get(id=pk)
    context={'task':task}

    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)