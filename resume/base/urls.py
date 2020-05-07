from django.urls import path
from . import views

urlpatterns = [
    path('',views.base_page,name='base-page'),
    path('search',views.get_values,name='get-values')
]
