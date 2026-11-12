
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Task


def home(request):
    context = {}

    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(owner=request.user)

        context = {
            'total_tasks': user_tasks.count(),
            'completed_tasks': user_tasks.filter(is_completed=True).count(),
            'pending_tasks': user_tasks.filter(is_completed=False).count(),
        }

    return render(request, 'tasks/home.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(
        owner=request.user,
        is_completed=False
    ).order_by('-created_at')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks
    })


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(
        owner=request.user,
        is_completed=True
    ).order_by('-created_at')

    return render(request, 'tasks/completed_tasks.html', {
        'tasks': tasks
    })


@login_required
def add_task(request):
    error = None

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date') or None

        if not title:
            error = "Task title is required."

        elif due_date:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                error = "Please enter a valid due date."

        if not error:
            Task.objects.create(
                owner=request.user,
                title=title,
                description=description,
                due_date=due_date
            )

            messages.success(request, "Task added successfully!")
            return redirect('task_list')

    return render(request, 'tasks/add_task.html', {
        'error': error
    })


@login_required
def task_detail(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        owner=request.user
    )

    return render(request, 'tasks/task_detail.html', {
        'task': task
    })


@login_required
def edit_task(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        owner=request.user
    )

    error = None

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date') or None

        if not title:
            error = "Task title is required."

        elif due_date:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                error = "Please enter a valid due date."

        if not error:
            task.title = title
            task.description = description
            task.due_date = due_date
            task.save()

            messages.success(request, "Task updated successfully!")
            return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'error': error
    })


@login_required
@require_POST
def delete_task(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        owner=request.user
    )

    task.delete()
    messages.success(request, "Task deleted successfully!")

    return redirect('task_list')


@login_required
@require_POST
def toggle_task_status(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        owner=request.user
    )

    task.is_completed = not task.is_completed
    task.save()

    if task.is_completed:
        messages.success(request, "Task marked as completed!")
    else:
        messages.success(request, "Task marked as pending!")

    return redirect('task_list' if not task.is_completed else 'completed_tasks')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account was created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/signup.html', {
        'form': form
    })
