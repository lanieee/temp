from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.blogList, name='list'),
    path('detail/<int:article_id>', views.blogDetail, name='detail'),
    path('me/', views.me, name='me'),
    path('tome/', views.tome, name='tome'),
    path("tomeAjax/", views.tomeAjax, name="tomeAjax"),
]