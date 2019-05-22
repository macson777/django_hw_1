from django import forms
import datetime


class PostForm(forms.Form):
   name = forms.CharField(max_length=20)
   from_ = forms.CharField(max_length=20)
   to_ = forms.CharField(max_length=20)
   number_of_flights = forms.IntegerField(min_value=1, max_value=200)
   date = forms.DateField(initial=datetime.date.today)
