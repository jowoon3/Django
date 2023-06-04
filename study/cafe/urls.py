from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('cafe/index.html', views.main_view),
    path('cafe/about.html', views.about_view, name='about'), # about.html URL 패턴 추가   
    path('cafe/coffees.html', views.coffees_view, name='coffees'),
    path('cafe/shop.html', views.shop_view, name='shop'),
    path('cafe/blog.html', views.blog_view, name='blog'),
    path('cafe/contact.html', views.contact_view, name='contact'),  
    # path('cafe/study.html/', views.study_view, name='study'),  
    path('cafe/study.html', views.study_view, name='study'),

]