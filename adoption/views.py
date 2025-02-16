from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adoption.models import AdoptionRequest
from cat.models import Cat
from account.models import Favorite
from django.contrib import messages

# Create your views here.
# Admin Check
def is_admin(user):
    return user.is_superuser

# List all adoption requests (Users see their own, Admins see all)
@login_required
def adoption_request_list(request):
    if request.user.is_superuser:
        requests = AdoptionRequest.objects.all()
    else:
        requests = AdoptionRequest.objects.filter(user=request.user)

    return render(request, "adoption/adoption_request_list.html", {"requests": requests})

# Create an adoption request

@login_required
def adoption_request_create(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == "POST":
        message = request.POST.get("message", "")  # ✅ Now this field exists in the model
        AdoptionRequest.objects.create(user=request.user, cat=cat, message=message, status="pending")
        return redirect("adoption_request_list")

    return render(request, "adoption/adoption_request_form.html", {"cat": cat})


# Update adoption request (Admin Only)
@user_passes_test(is_admin)
def adoption_request_update(request, pk):
    adoption_request = get_object_or_404(AdoptionRequest, pk=pk)

    if request.method == "POST":
        adoption_request.status = request.POST["status"]
        adoption_request.save()
        return redirect("adoption_request_list")

    return render(request, "adoption/adoption_request_update.html", {"adoption_request": adoption_request})

@login_required
def adoption_request_cancel(request, pk):
    adoption_request = get_object_or_404(AdoptionRequest, pk=pk, user=request.user)

    if request.method == "POST":
        adoption_request.delete()
        return redirect("adoption_request_list")

    return render(request, "adoption/adoption_request_cancel.html", {"adoption_request": adoption_request})
# Approve Adoption Request
@user_passes_test(is_admin)
def approve_adoption(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)
    adoption_request.status = "Approved"
    adoption_request.save()
    return redirect("admin_dashboard")

# Reject Adoption Request
@user_passes_test(is_admin)
def reject_adoption(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)
    adoption_request.status = "Rejected"
    adoption_request.save()
    return redirect("admin_dashboard")

# View Adoption Request Details (Admin Only)
@user_passes_test(is_admin)
def review_adoption_request(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "approve":
            adoption_request.status = "Approved"
            messages.success(request, f"Adoption request for {adoption_request.cat.name} has been approved!")
        elif action == "reject":
            adoption_request.status = "Rejected"
            messages.error(request, f"Adoption request for {adoption_request.cat.name} has been rejected.")
        adoption_request.save()
        return redirect("admin_dashboard")

    return render(request, "adoption/review_adoption_request.html", {"adoption_request": adoption_request})