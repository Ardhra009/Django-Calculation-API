"""
URL configuration for djcalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from Dapp.views import AdditionView,SubstractionView,MultiplicationView,DivisionView,FloordivisionView,PercentageView,BMIView,RectangleView,Age_calculatorView,PrincipleinterestView,ElectricityBillView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/',AdditionView.as_view(),name='addition'),
    path('sub/',SubstractionView.as_view(),name='sub'),
    path('mul/',MultiplicationView.as_view(),name='mul'),
    path('div/',DivisionView.as_view(),name='div'),
    path('fdiv/',FloordivisionView.as_view(),name='fdiv'),
    path('percentage/',PercentageView.as_view(),name='percentage'),
    path('bmi/',BMIView.as_view(),name='bmi'),
    path('area/',RectangleView.as_view(),name='area'),
    path('age/',Age_calculatorView.as_view(),name='age'),
    path('simpleintrest/',PrincipleinterestView.as_view(),name='simpleintrest'),
    path('bill/',ElectricityBillView.as_view(),name='bill')
]
