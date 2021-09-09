from django.contrib import admin
from django.urls import path,include
from .import views
from .views  import LinkDeleteView

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<pk>/',LinkDeleteView.as_view(),name="linkdelete"),
    path('update',views.updateprice,name="updateprice"),
    
]