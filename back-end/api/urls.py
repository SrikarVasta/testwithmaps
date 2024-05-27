from django.urls import path
from .views import getData,addShape

urlpatterns = [
    path('shape/', getData, name='get_data'),
    path('shape/add', addShape, name='create_shape'),
]
