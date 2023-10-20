"""
URL configuration for CASHBOX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cash_register import views

urlpatterns = [
    path('', views.index, name='Cashbox'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('inventory/', views.inventory, name="inventory"),
    path('statistics/', views.statistics, name="statistics"),
    path('customers/', views.customers, name="customers"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('settings/', views.settings, name="settings"),
    path('admin/', admin.site.urls),
]
