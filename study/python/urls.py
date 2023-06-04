from django.urls import path
from . import views

app_name = 'python'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('python/p01.html', views.main_view),
    path('python/p02.html', views.p02_view, name='p02'),
    path('python/p03.html', views.p03_view, name='p03'),
    path('python/p04.html', views.p04_view, name='p04'),
    path('python/p05.html', views.p05_view, name='p05'),
    path('python/p06.html', views.p06_view, name='p06'),
    path('python/p07.html', views.p07_view, name='p07'),
    path('python/p08.html', views.p08_view, name='p08'),
    path('python/p09.html', views.p09_view, name='p09'),
    path('python/p10.html', views.p10_view, name='p10'),
    path('python/p11.html', views.p11_view, name='p11'),
    path('python/p12.html', views.p12_view, name='p12'),
    path('python/p13.html', views.p13_view, name='p13'),
    path('python/p14.html', views.p14_view, name='p14'),
    path('python/p15.html', views.p15_view, name='p15'),
    path('python/p16.html', views.p16_view, name='p16'),
    path('python/p17.html', views.p17_view, name='p17'),
    path('python/p18.html', views.p18_view, name='p18'),
    path('python/p19.html', views.p19_view, name='p19'),
    path('python/p20.html', views.p20_view, name='p20'),
    path('python/p21.html', views.p21_view, name='p21'),
    path('python/p22.html', views.p22_view, name='p22'),
]
