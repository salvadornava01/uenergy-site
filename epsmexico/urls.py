"""epsmexico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from homepage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('clientes/', clientes_view, name='clientes_view'),
    path('instalaciones/', instalaciones_view, name='instalaciones_view'),
    path('plantas/', plantas_view, name='plantas_view'),
    path('aire/', aire_view, name='aire_view'),
    path('ups/', upss_view, name='upss_view'),
    path('reguladores/', reguladores_view, name='reguladores_view'),
    path('contacform/', contact_form_view, name='contact_form_view'),
    path('cotizform/', cotiz_form_view, name='cotiz_form_view'),
    path('thankyou/<str:id>/', thankyoupage_view, name='thankyoupage_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
