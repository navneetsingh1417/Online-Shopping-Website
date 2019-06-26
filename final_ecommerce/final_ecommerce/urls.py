"""final_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include 

import accounts
import deals.views
import men.views
import women.views
import kids.views
import electronics.views
import sports.views
from django.conf import settings
from django.conf.urls.static import static
from templates import checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',deals.views.home, name = 'home'),
    path('men/',men.views.men, name ='men'),
    path('women/',women.views.women, name = 'women'),
    path('kids/',kids.views.kids, name = 'kids'),
    path('electronics',electronics.views.electronics, name = 'electronics'),
    path('sports',sports.views.sports, name='sports'),
    path('accounts/',include('accounts.urls')),
    path('checkout/',deals.views.checkout)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
