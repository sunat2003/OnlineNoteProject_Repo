"""OnlineLibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('book/', views.book_view),
    path('magagin/', views.magagin_view),
    path('news/', views.news_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('bookform/', views.bookform_view),
    path('deletebook/<int:id>', views.bookdelete_view),
    path('bookupdate/<int:id>', views.bookupdate_view),
    path('magaginform/', views.magaginform_view),
    path('deletemagagin/<int:id>', views.magagindelete_view),
    path('updatemagagin/<int:id>', views.magaginupdate_view),
    path('newsform/', views.newsform_view),
    path('deletenews/<int:id>', views.newsdelete_view),
    path('updatenews/<int:id>', views.newsupdate_view),
]
