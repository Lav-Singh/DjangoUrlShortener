from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
    path('link/<slug:slug>/', views.redirect_view, name='redirect_view'),
]
