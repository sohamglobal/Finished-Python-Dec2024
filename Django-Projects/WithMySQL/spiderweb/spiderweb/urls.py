"""
URL configuration for spiderweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('newfilm/',views.newfilm),
    path('addfilm/',views.addfilm),
    path('filmreport/',views.filmreport),
    path('searchgen/',views.genresearch),
    path('langsearch/',views.langsearch),
    path('searchonlang/<str:lang>/',views.searchonlang),
    path('genresearch/',views.linkgenresearch),
    path('login/',views.login),
    path('del/',views.delete),
    path('delfilm/',views.delfilm),
    path('ajaxgenresearch/',views.ajaxgenresearch),
    path('ajaxgen/<str:gen>/',views.ajaxgen),



    
]
