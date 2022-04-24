from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/', views.index, name='index'),
    path('<int:year>/<int:month>/', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
]