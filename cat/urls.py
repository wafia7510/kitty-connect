from django.urls import path
from .views import cat_list, cat_create, cat_update, cat_delete, admin_dashboard

urlpatterns = [
    path("", cat_list, name="cat_list"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add/", cat_create, name="cat_create"),
    path("edit/<int:pk>/", cat_update, name="cat_update"),
    path("delete/<int:pk>/", cat_delete, name="cat_delete"),
]