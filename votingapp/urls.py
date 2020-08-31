"""votingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from reg import views as views1
from poll import views 


app_name="poll"

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views1.index),
   path('login/', views1.login),
   path('home/', views1.home),
    path('poll/', include(('poll.urls', 'poll'), namespace='poll')),
]
