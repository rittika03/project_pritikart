from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home2/',views.home2, name='home2'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('my_profile/',views.my_profile, name='my_profile'),
    path('billing/',views.billing, name='billing'),
    path('skincare/',views.skincare, name='skincare'),
    path('makeup/',views.makeup, name='makeup'),
    path('clothes/',views.clothes, name='clothes'),
    path('accessories/',views.accessories, name='accessories'),

]
