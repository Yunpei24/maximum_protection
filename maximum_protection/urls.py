"""
URL configuration for maximum_protection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('', include('maximum_protection.core.urls')),
#     path('chatbot/', include('maximum_protection.chatbot.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from .core.views import HomeView, ServicesView, ProductsView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Route pour la vue Home
    path('services/', ServicesView.as_view(), name='services'),  # Route pour la vue Services
    path('products/', ProductsView.as_view(), name='products'),  # Route pour la vue Products
    path('about/', AboutView.as_view(), name='about'),  # Route pour la vue About
    path('contact/', ContactView.as_view(), name='contact'),  # Route pour la vue Contact
    path('chatbot/', include('maximum_protection.chatbot.urls')),
]
