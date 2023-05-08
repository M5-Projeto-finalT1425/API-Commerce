from django.urls import path
from . import views

urlpatterns = [
    path("account/cart/<int:pk>/", views.CartUpdateDestroyView.as_view()),
    path("account/cart/retrieve/<int:pk>/", views.CartRetrieveView.as_view()),
]
