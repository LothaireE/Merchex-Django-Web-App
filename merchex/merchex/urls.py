"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),


    # path('bands/', views.band_list, name='band-list'),
    path('bands/', views.BandListView.as_view(), name='band-list'),
    path('offers/', views.OfferListView.as_view(), name='offer-list'),

    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_add, name='band-add'),
    path('bands/update/<int:band_id>/', views.band_update, name='band-update'),
    path('bands/remove/<int:band_id>/', views.band_remove, name='band-remove'), 

    # path('offers/', views.offer_list, name='offer-list'),
    path('offers/<int:offer_id>/', views.offer_detail, name='offer-detail'),
    path('offers/add/', views.offer_add, name='offer-add'),
    path('offers/update/<int:offer_id>/', views.offer_update, name='offer-update'),
    path('offers/remove/<int:offer_id>/', views.offer_remove, name='offer-remove'),
    
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent')

]
