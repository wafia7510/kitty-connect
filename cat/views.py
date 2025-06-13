from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from django.contrib.auth.decorators import user_passes_test
from account.models import Favorite
from adoption.models import AdoptionRequest
from django.utils import timezone
from datetime import timedelta

# Admin Check
def is_admin(user):
    return user.is_superuser

# List all cats
def cat_list(request):
    # Exclude cats that are already adopted (approved requests)
    adopted_cats = AdoptionRequest.objects.filter(
        status="Approved"
    ).values_list("cat_id", flat=True)
    cats = Cat.objects.exclude(id__in=adopted_cats)
    
    # Initialize user-specific lists
    favorite_cats = []
    pending_requests = []
    recent_rejections = []
    
    if request.user.is_authenticated:
        favorite_cats = list(
            Favorite.objects.filter(user=request.user)
                .values_list("cat_id", flat=True)
        )
        pending_requests = list(
            AdoptionRequest.objects.filter(
                user=request.user,
                status="Pending"
            ).values_list("cat_id", flat=True)
        )
        
        six_months_ago = timezone.now() - timedelta(days=180)
        recent_rejections = list(
            AdoptionRequest.objects.filter(
                user=request.user,
                status="Rejected",
                request_date__gte=six_months_ago
            ).values_list("cat_id", flat=True)
        )
    
    context = {
        "cats": cats,
        "favorite_cats": favorite_cats,
        "pending_requests": pending_requests,
        "recent_rejections": recent_rejections,
    }
    return render(request, "cat/cat_list.html", context)

# Create a new cat (Admin Only)
@user_passes_test(is_admin)
def cat_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        breed = request.POST["breed"]
        age = request.POST["age"]
        description = request.POST["description"]
        image = request.FILES.get("image")

        Cat.objects.create(
            name=name,
            breed=breed,
            age=age,
            description=description,
            image=image
        )
        return redirect("admin_dashboard")
    return render(request, "cat/cat_form.html", {"cat": None})

# Update cat details (Admin Only)
@user_passes_test(is_admin)
def cat_update(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == "POST":
        cat.name = request.POST["name"]
        cat.breed = request.POST["breed"]
        cat.age = request.POST["age"]
        cat.description = request.POST["description"]
        cat.image = request.FILES.get("image", cat.image)
        cat.save()
        return redirect("admin_dashboard")
    return render(request, "cat/cat_form.html", {"cat": cat})

# Delete a cat (Admin Only)
@user_passes_test(is_admin)
def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == "POST":
        cat.delete()
        return redirect("admin_dashboard")
    return render(request, "cat/cat_confirm_delete.html", {"cat": cat})

# Admin Dashboard: show only 5 most recently added cats
@user_passes_test(is_admin)
def admin_dashboard(request):
    recent_cats = Cat.objects.order_by('-id')[:5]
    adoption_requests = AdoptionRequest.objects.all()

    return render(request, "admin/admin_dashboard.html", {
        "cats": recent_cats,
        "adoption_requests": adoption_requests,
    })
