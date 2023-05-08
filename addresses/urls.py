from django.urls import path
from . import views

urlpatterns = [
    path("account/address/", views.AddressView.as_view()),
    path("account/address/<int:address_id>/", views.AddressDetailView.as_view()),
]
