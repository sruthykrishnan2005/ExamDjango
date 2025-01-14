from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contact/add/', views.add_contact, name='add_contact'),
    path('<int:id>/edit/', views.edit_contact, name='edit_contact'),
    path('contact/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('<int:pk>/call/', views.call_contact, name='call_contact'),
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('<int:pk>/', views.view_contact, name='default_view_contact'),
]