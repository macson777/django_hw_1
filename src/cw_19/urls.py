from django.contrib import admin
from django.urls import path
from cw_19.views import show_form


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_form/', show_form),
]