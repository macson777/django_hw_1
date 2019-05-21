from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def render_18_2(request):
    if request.method == 'GET':
        template = loader.get_template('hw_18_2_form.html')
        return HttpResponse(template.render({}, request))
    if request.method == 'POST':
        file = open('text.txt', 'a')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        file.write(f'You are {name} {lastname}, {age} years old')
        file.close()
        return redirect('http://127.0.0.1:8000/hw_18_2/render_18_2/')
