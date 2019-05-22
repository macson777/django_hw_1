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
            data = form.data
            name = data.get('name')
            from_ = data.get('from')
            to_ = data.get('to')
            date = data.get('date')
            number_of_flights = data.get('number of flights')
            if number_of_flights != 1:
                price = 100 * 2
            else:
                price = 100
            template = loader.get_template('display_flight.html')

            return HttpResponse(template.render({'price': price}, request))
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
