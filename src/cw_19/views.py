from django.shortcuts import render
from django.http import HttpResponse
from cw_19.forms import PostForm

# Create your views here.


def show_form(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'cw_19_task_1.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.data
            firstname = data.get('name')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            print(f'{firstname} {lastname} {age} {comment}')
            context = {'form': PostForm()}
            return render(request, 'cw_19_task_1.html', context)
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
