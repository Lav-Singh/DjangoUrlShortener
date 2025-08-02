from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_view, name='shorten'),
    path('link/<slug:slug>/', views.result_view, name='result_view'),
    path('<slug:slug>/', views.redirect_view, name='redirect_view'),
    path('api/stats/<slug:slug>/', views.api_stats, name='api_stats')
]
