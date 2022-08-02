from django.urls import path
from .views import home_page,login_page


urlpatterns =[

#landing page
path('',home_page,name='home'),
path('home',home_page,name='index'),
path('login',login_page,name='login')

]