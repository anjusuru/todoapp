from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class taskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:listView')

class taskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('todoapp:taskDetailView',kwargs={'pk':self.object.id})

class taskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class tasklistView(ListView):
    model= Task
    template_name= 'home.html'
    context_object_name = 'task'



# Create your views here.
def add(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('txtname', '')
        priority = request.POST.get('txtpriority', '')
        date = request.POST.get('dtdate', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task': tasks})


def delete(request, task_id):
    task_del = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task_del.delete()
        return redirect('/')
    return render(request, 'delete.html')


# def details(request):
#     task = Task.objects.all()
#     return render(request, 'details.html', {'tasks': tasks})
def update(request, id):
    task = Task.objects.get(id=id)
    form = todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})

