"""wholphinplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import Payment, main, index, Read, Rea, Read1, Allnews, Event, Navbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal/', include('portal.urls')),
    path('account/', include('account.urls')),
    path('student/', include('student_info.urls')),
    path('programmes/', include('programmes.urls')),
    path('main/', include('main.urls')),
    path('quick/', include('quick_link.urls')),
    path('pay', Payment.as_view(), name='pay'),
    path('', main, name='main'),
    path('index', index, name='in'),
    path('read', Read.as_view(), name='read'),
    path('red', Rea.as_view(), name='rea'),
    path('news', Allnews.as_view(), name='news'),
    path('read1', Read1.as_view(), name='read1'),
    path('event', Event.as_view(), name='event'),
    path('navbar', Navbar.as_view(), name='navbar'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

