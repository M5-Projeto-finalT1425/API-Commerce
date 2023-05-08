from django.urls import path
from . import views

urlpatterns = [
    path("accounts/orders/", views.OrderView.as_view()),
    path("accounts/orders/<int:order_id>/", views.OrderDetailView.as_view()),
]
