from django.urls import path
from cw_19.views import show_form


urlpatterns = [
    path('show_form/', show_form, name='show_form'),
]