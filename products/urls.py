from django.urls import path
from . import views

urlpatterns = [
    path("accounts/products/", views.ProductView.as_view()),
    # path("accounts/<int:account_id>/", views.AccountDetailView.as_view()),
    # path("accounts/login/", jwt_views.TokenObtainPairView.as_view()),
]
