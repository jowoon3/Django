from django.urls import path
from . import views

app_name = 'javascript'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('javascript/j01.html', views.main_view),
    path('javascript/j02.html', views.j02_view, name='j02'),
    path('javascript/j03.html', views.j03_view, name='j03'),
    path('javascript/j04.html', views.j04_view, name='j04'),
    path('javascript/j05.html', views.j05_view, name='j05'),
    path('javascript/j06.html', views.j06_view, name='j06'),
    path('javascript/j07.html', views.j07_view, name='j07'),
    path('javascript/j08.html', views.j08_view, name='j08'),
    path('javascript/j09.html', views.j09_view, name='j09'),
    path('javascript/j10.html', views.j10_view, name='j10'),
    path('javascript/j11.html', views.j11_view, name='j11'),
    path('javascript/j12.html', views.j12_view, name='j12'),
    path('javascript/j13.html', views.j13_view, name='j13'),
    path('javascript/j14.html', views.j14_view, name='j14'),
    path('javascript/j15.html', views.j15_view, name='j15'),
    path('javascript/j16.html', views.j16_view, name='j16'),
    path('javascript/j17.html', views.j17_view, name='j17'),
    path('javascript/notice.html', views.notice_view, name='notice'),
    path('javascript/tut40.html', views.tut40_view, name='tut40'),
]
