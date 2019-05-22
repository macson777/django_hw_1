"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include("myapp.urls")),
    path('index2/', include("task2.urls")),
    path('index3/', include("django_task2.urls")),
    path('render_name/', include("hw_18_1.urls")),
    path('hw_18_2/', include("hw_18_2.urls")),
    path('hw_18_3/', include("hw_18_3.urls")),
    path('cw_19/', include("cw_19.urls")),
    path('hw_19/', include("hw_19.urls")),

]
