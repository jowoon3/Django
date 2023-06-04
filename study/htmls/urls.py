from django.urls import path
from . import views

app_name = 'htmls'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('htmls/tut1.html', views.main_view),
    path('htmls/tut2.html', views.tut2_view, name='tut2'),
    path('htmls/tut3.html', views.tut3_view, name='tut3'),
    path('htmls/tut4.html', views.tut4_view, name='tut4'),
    path('htmls/tut5.html', views.tut5_view, name='tut5'),
    path('htmls/tut6.html', views.tut6_view, name='tut6'),
    path('htmls/tut7.html', views.tut7_view, name='tut7'),
    path('htmls/tut8.html', views.tut8_view, name='tut8'),
    path('htmls/tut9.html', views.tut9_view, name='tut9'),
    path('htmls/tut10.html', views.tut10_view, name='tut10'),
    path('htmls/html_CSS.html', views.html_CSS_view, name='html_CSS'),
    path('htmls/html_Emmet.html', views.html_Emmet_view, name='html_Emmet'),
    path('htmls/html_tags.html', views.html_tags_view, name='html_tags'),
]
