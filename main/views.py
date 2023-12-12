from django.shortcuts import render

from main.models import Task


# Create your views here.
# сырой вариант не используя библеотеки

def task_list(request):
    tasks = Task.objects.all()
    # print(tasks, '!!!!!!')
    ls =[]
    for task in tasks:
        dict_ = {
            'id': task.id, 'title': task.title,
            'deadline': str(task.deadline)}
        ls.append(dict_)
