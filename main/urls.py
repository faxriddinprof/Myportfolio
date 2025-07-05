from django.contrib import admin
from django.urls import path
from .views import Homepage, Aboutpage, Resumepage, Portfoliopage, Contactpage

urlpatterns = [
    path('',Homepage,name='home'),
    path('about/',Aboutpage,name='about'),
    path('resume/',Resumepage, name='resume'),
    path('portfolio/',Portfoliopage, name='portfolio'),
    path('contact/',Contactpage, name='contact'),
]