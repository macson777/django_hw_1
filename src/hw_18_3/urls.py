from django.contrib import admin
from django.urls import path
from hw_18_3.views import render_18_3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('render_18_3/', render_18_3),
]

