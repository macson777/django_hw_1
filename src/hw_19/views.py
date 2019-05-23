from django.shortcuts import render, loader
from django.http import HttpResponse
from hw_19.forms import PostForm

# Create your views here.


def show_form(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'hw_19_task_1.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            number_of_flights = data.get('number_of_flights')
            if number_of_flights != 1:
                price = number_of_flights * 100 * 2
            else:
                price = 100
            context = {'price': price, 'data': data}

            return render(request, 'display_flight.html', context)
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
