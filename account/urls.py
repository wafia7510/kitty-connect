from django.urls import path
from .views import user_register, user_login, user_logout, user_dashboard

urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", user_dashboard, name="dashboard")
]
