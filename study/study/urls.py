"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path  
from django.views.generic import RedirectView
from cafe import views as cafe_views 
# from htmls import views as html_views
# from css import views as css_views
# from javascript import views as javascript_views
# from python import views as python_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('run_script/', cafe_views.run_script), 
    # path('cafe/', cafe_views.main_view),
    # path('htmls/', html_views.main_view),
    # path('css/', css_views.main_view),
    # path('javascript/', javascript_views.main_view),
    # path('python/', python_views.main_view),     
    path('cafe/', include('cafe.urls')),
    path('htmls/', include('htmls.urls')),
    path('css/', include('css.urls')),
    path('javascript/', include('javascript.urls')),
    path('python/', include('python.urls')),
    path('', RedirectView.as_view(url='/cafe/', permanent=True)),
    path('', RedirectView.as_view(url='/htmls/', permanent=True)),
    path('', RedirectView.as_view(url='/css/', permanent=True)),
    path('', RedirectView.as_view(url='/javascript/', permanent=True)),
    path('', RedirectView.as_view(url='/python/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

