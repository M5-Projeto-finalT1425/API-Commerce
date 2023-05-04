from django.urls import path
from . import views

urlpatterns = [path("account/cart/<int:product_id>", views.CartView.as_view())]
