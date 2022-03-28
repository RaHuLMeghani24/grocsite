from django.urls import path
from . import views

app_name = 'myApp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail/<int:type_no>', views.detail, name='detail'),
    path('items/', views.items, name='items'),
    path('placeorder/', views.placeorder, name='placeorder'),
]
