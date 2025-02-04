from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AdoptionRequest
from cat.models import Cat

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
        message = request.POST.get("message", "") 
        AdoptionRequest.objects.create(user=request.user, cat=cat, message=message, status="Pending")
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

# Delete adoption request (Admin Only)
@user_passes_test(is_admin)
def adoption_request_delete(request, pk):
    adoption_request = get_object_or_404(AdoptionRequest, pk=pk)

    if request.method == "POST":
        adoption_request.delete()
        return redirect("adoption_request_list")

    return render(request, "adoption/adoption_request_confirm_delete.html", {"adoption_request": adoption_request})

@login_required
def adoption_request_cancel(request, pk):
    adoption_request = get_object_or_404(AdoptionRequest, pk=pk, user=request.user)

    if request.method == "POST":
        adoption_request.delete()
        return redirect("adoption_request_list")

    return render(request, "adoption/adoption_request_cancel.html", {"adoption_request": adoption_request})