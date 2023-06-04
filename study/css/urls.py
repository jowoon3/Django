from django.urls import path
from . import views

app_name = 'css'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('css/tut11.html', views.main_view),
    path('css/tut12.html', views.tut12_view, name='tut12'),
    path('css/tut13.html', views.tut13_view, name='tut13'),
    path('css/tut14.html', views.tut14_view, name='tut14'),
    path('css/tut15.html', views.tut15_view, name='tut15'),
    path('css/tut16.html', views.tut16_view, name='tut16'),
    path('css/tut17.html', views.tut17_view, name='tut17'),
    path('css/tut18.html', views.tut18_view, name='tut18'),
    path('css/tut19.html', views.tut19_view, name='tut19'),
    path('css/tut20.html', views.tut20_view, name='tut20'),
    path('css/tut21.html', views.tut21_view, name='tut21'),
    path('css/tut22.html', views.tut22_view, name='tut22'),
    path('css/tut23.html', views.tut23_view, name='tut23'),
    path('css/tut24.html', views.tut24_view, name='tut24'),
    path('css/tut25.html', views.tut25_view, name='tut25'),
    path('css/tut26.html', views.tut26_view, name='tut26'),
    path('css/tut27.html', views.tut27_view, name='tut27'),
    path('css/tut28.html', views.tut28_view, name='tut28'),
    path('css/tut29.html', views.tut29_view, name='tut29'),
    path('css/tut30.html', views.tut30_view, name='tut30'),
    path('css/tut31.html', views.tut31_view, name='tut31'),
]
