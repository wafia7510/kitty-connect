from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adoption.models import AdoptionRequest
from cat.models import Cat
from account.models import Favorite
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone

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

    # Check if user has a rejected request within last 6 months
    six_months_ago = timezone.now() - timedelta(days=180)
    recent_rejection = AdoptionRequest.objects.filter(
        user=request.user,
        cat=cat,
        status="Rejected",
        request_date__gte=six_months_ago
    ).exists()
    if recent_rejection:
        messages.error(request, "You cannot reapply for this cat within 6 months of rejection.")
        return redirect("cat_list")
    
    if request.method == "POST":
        message = request.POST.get("message", "")
        AdoptionRequest.objects.create(user=request.user, cat=cat, message= message, status="Pending")
        return redirect("dashboard")

    return render(request, "adoption/adoption_request_form.html", {"cat": cat})



@login_required
def adoption_request_cancel(request, pk):
    adoption_request = get_object_or_404(AdoptionRequest, pk=pk, user=request.user)
    cat_name = adoption_request.cat.name  # Save cat name before deletion

    if request.method == "POST":
        adoption_request.delete()
        messages.success(request, "Your adoption request has been canceled.")
        # Render the confirmation template with the cat's name context
        return render(request, "adoption/adoption_request_confirm_delete.html", {"cat_name": cat_name})

    # GET request: render the confirmation page for cancellation
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