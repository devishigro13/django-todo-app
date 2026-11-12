from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'tasks/home.html')


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context)

def add_task(request):

    error = None

    if request.method == 'POST':

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date') or None

        if not title:
            error = "Task title is required."

        else:
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date
            )

            return redirect('task_list')

    return render(request, 'tasks/add_task.html', {'error': error})


def edit_task(request, id):

    task = get_object_or_404(Task, id=id)

    error = None

    if request.method == 'POST':

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date') or None

        if not title:
            error = "Task title is required."

        else:
            task.title = title
            task.description = description
            task.due_date = due_date

            task.save()

            return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'error': error
    })
