from django.urls import path

from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("add_author/", views.add_author, name="add_author"),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('tag/<slug:tag_name>/', views.tag_quotes, name='tag_quotes'),

]
