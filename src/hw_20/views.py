from django.http import HttpResponse
from django.shortcuts import render, redirect
from hw_20.models import Car
from hw_20.forms import CarForm

# Create your views here.


def home_page(request):
    cars = Car.objects.all()
    context = {'cars': cars}

    return render(request, 'home.html', context)


def add_car(request):
    if request.method == 'GET':
        context = {'form': CarForm()}
        return render(request, 'add_car.html', context)
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand')
            model = data.get('model')
            color = data.get('color')
            weight = data.get('weight')
            full_name_owner = data.get('full_name_owner')
            year_of_issue = data.get('year_of_issue')
            Car.objects.create(
                brand=brand,
                model=model,
                color=color,
                weight=weight,
                full_name_owner=full_name_owner,
                year_of_issue=year_of_issue,
            )
            return redirect('home_page')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'GET':
        context = {
            'car_id': car_id,
            'form': CarForm(
                initial={
                    'brand': car.brand,
                    'model': car.model,
                    'color': car.color,
                    'weight': car.weight,
                    'full_name_owner': car.full_name_owner,
                    'year_of_issue': car.year_of_issue,
                },
            ),
        }
        return render(request, 'edit.html', context)
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand')
            model = data.get('model')
            color = data.get('color')
            weight = data.get('weight')
            full_name_owner = data.get('full_name_owner')
            year_of_issue = data.get('year_of_issue')
            Car.objects.filter(id=car_id).update(
                brand=brand,
                model=model,
                color=color,
                weight=weight,
                full_name_owner=full_name_owner,
                year_of_issue=year_of_issue,
            )
            return redirect('home_page')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')




def remove_car(request, car_id):
    car = Car.objects.get(id=car_id)
    print(f'{car.brand} has been removed')
    car.delete()
    return redirect('home_page')

