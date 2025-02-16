from django.urls import path
from .views import (
    adoption_request_list, 
    adoption_request_create, 
    adoption_request_update, 
    adoption_request_cancel,
    approve_adoption,  # New: Admin action
    reject_adoption, review_adoption_request,
)

urlpatterns = [
    path("", adoption_request_list, name="adoption_request_list"),
    path("apply/<int:cat_id>/", adoption_request_create, name="adoption_request_create"),
    path("edit/<int:pk>/", adoption_request_update, name="adoption_request_update"),
    path("cancel/<int:pk>/", adoption_request_cancel, name="adoption_request_cancel"), 
    # Admin URLs for managing adoption requests
    path("approve/<int:request_id>/", approve_adoption, name="approve_adoption"),
    path("reject/<int:request_id>/", reject_adoption, name="reject_adoption"),
    path("review/<int:request_id>/", review_adoption_request, name="review_adoption_request"), 
]