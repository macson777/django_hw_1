from django.urls import path
from hw_20.views import home_page, add_car, remove_car, edit_car

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('add_car/', add_car, name='add_car_form'),
    path('remove/<int:car_id>', remove_car, name='remove_car'),
    path('edit/<int:car_id>', edit_car, name='edit_car'),
]
