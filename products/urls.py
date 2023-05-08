from django.urls import path
from . import views

urlpatterns = [
    path("accounts/products/", views.ProductView.as_view()),
    path(
        "accounts/products/<int:product_id>/",
        views.ProductDetailView.as_view(),
    ),
]
