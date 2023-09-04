"""IT_Bootcamp_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name = 'home'),
    path('', views.home_page),
    path('all_authors/', views.author_list, name= 'all_authors'),
    path('add_author/', views.add_author, name = 'add_author'),
    path('all_books/', views.book_list, name = 'all_books'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('note/', views.note, name = 'note'),
]