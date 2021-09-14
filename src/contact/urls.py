from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-dev/', views.dev_contact_view, name='dev-contact'),
]
