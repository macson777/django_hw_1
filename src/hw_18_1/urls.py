from django.contrib import admin
from django.urls import path
from hw_18_1.views import render_name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('render_name/', render_name),
]

