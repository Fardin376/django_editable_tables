from django.urls import path
from . import views

urlpatterns = [
    path('stock_project/', views.home, name="home"),
    path('showTable/', views.showTable, name="showTable"),
    path('update_data/', views.update_data, name='update_data'),
]