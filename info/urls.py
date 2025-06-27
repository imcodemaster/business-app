from django.urls import path
from . import views
from info.views import ContactView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('open-shop/', views.shop, name='shop'),
    path('contact/', ContactView.as_view(), name = 'contact'),

]