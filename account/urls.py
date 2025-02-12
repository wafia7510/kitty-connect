from django.urls import path
from .views import user_register, user_login, user_logout, user_dashboard, add_to_favorites, remove_from_favorites
urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", user_dashboard, name="dashboard"),
    path("favorite/add/<int:cat_id>/", add_to_favorites, name="add_to_favorites"),
    path("favorite/remove/<int:cat_id>/", remove_from_favorites, name="remove_from_favorites")
]
