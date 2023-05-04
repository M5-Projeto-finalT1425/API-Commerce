from django.urls import path
from . import views

urlpatterns = [
    path("accounts/products/", views.ProductView.as_view()),
    path(
        "accounts/products/<int:product_id>/",
        views.ProductDetailViewAndListID.as_view(),
    ),
    path(
        "accounts/products/<str:name__iexact>/",
        views.ProductDetailListView.as_view(),
    ),
]
