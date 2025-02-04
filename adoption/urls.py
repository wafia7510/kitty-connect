from django.urls import path
from .views import (
    adoption_request_list, 
    adoption_request_create, 
    adoption_request_update, 
    adoption_request_delete,
    adoption_request_cancel,  # New Cancel Request View
)

urlpatterns = [
    path("", adoption_request_list, name="adoption_request_list"),
    path("apply/<int:cat_id>/", adoption_request_create, name="adoption_request_create"),
    path("edit/<int:pk>/", adoption_request_update, name="adoption_request_update"),
    path("delete/<int:pk>/", adoption_request_delete, name="adoption_request_delete"),
    path("cancel/<int:pk>/", adoption_request_cancel, name="adoption_request_cancel"), 
]