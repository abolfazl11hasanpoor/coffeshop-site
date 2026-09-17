from django.urls import path
from . import views


urlpatterns=[
    path('list',views.category_list,name='category_list')
]