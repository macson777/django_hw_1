from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def show_form(request):
    if request.method == 'GET':
        return render(request, 'cw_19_task_1.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        print(f'{name} {lastname} {age} {comment}')
        return render(request, 'cw_19_task_1.html')
    return HttpResponse('Wrong request method')
