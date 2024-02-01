from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('expense/', views.ExpenseView.as_view(), name="expense"),
    path('record/', views.RecordView.as_view(), name="record"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('home/', views.Home.as_view(), name="home"),
    path('api/', views.APiV.as_view(), name="api")
]