from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexServerProject, name='indexServerProject'),
    path('new/', views.newServerProject, name='newServerProject'),
    path('detail/<int:pk>/', views.detailServerProject, name='detailServerProject'),
    path('update/<int:pk>/', views.updateServerProject, name='updateServerProject'),
    path('buy/<int:pk>/', views.buyServerProject, name="buyServerProject"),
]