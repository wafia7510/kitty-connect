from django.urls import path
from .views import cat_list, cat_create, cat_update, cat_delete

urlpatterns = [
    path("", cat_list, name="cat_list"),
    path("add/", cat_create, name="cat_create"),
    path("edit/<int:pk>/", cat_update, name="cat_update"),
    path("delete/<int:pk>/", cat_delete, name="cat_delete"),
]