from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('our_objects',views.our_objects),
    path('price',views.price)
]