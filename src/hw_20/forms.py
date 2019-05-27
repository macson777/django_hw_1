from django import forms


class CarForm(forms.Form):
    brand = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    color = forms.CharField(max_length=255)
    weight = forms.IntegerField()
    full_name_owner = forms.CharField(max_length=255)
    year_of_issue = forms.DateField(widget=forms.SelectDateWidget())
