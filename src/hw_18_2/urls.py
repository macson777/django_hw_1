from django.contrib import admin
from django.urls import path
from hw_18_2.views import render_18_2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('render_18_2/', render_18_2),

]

