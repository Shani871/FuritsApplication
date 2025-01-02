from django.urls import path
from . import views  # Import your views
from .views import fruit

urlpatterns = [
    path('', views.home, name='home'),  # Add a view for the homepage
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('fruit/', views.fruit, name='fruit'),
    path('service/', views.service, name='service'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]