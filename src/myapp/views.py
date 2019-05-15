from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    form1 = request.POST.get('form1')
    form2 = request.POST.get('form2')
    form3 = request.POST.get('form3')
    max_len_form = form1
    if len(form2) > len(form1) and len(form2) > len(form3):
        max_len_form = form2
    elif len(form3) > len(form1):
        max_len_form = form3
    return HttpResponse(max_len_form)

