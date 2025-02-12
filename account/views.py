from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adoption.models import AdoptionRequest
from cat.models import Cat
from .models import Favorite


# User Account Views
# User Registration
def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "account/register.html")

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get("next")  # Get the URL to redirect after login
            return redirect(next_url if next_url else "dashboard")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login")

    return render(request, "account/login.html")


# User Logout
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def user_dashboard(request):
    user = request.user

    # Get user's adoption requests
    adoption_requests = AdoptionRequest.objects.filter(user=user)

    # Filter approved requests for adoption history
    adopted_cats = adoption_requests.filter(status="Approved")

    # Get user's favorite cats
    favorite_cats = Favorite.objects.filter(user=user).select_related("cat")

    return render(request, "account/dashboard.html", {
        "adoption_requests": adoption_requests,
        "adopted_cats": adopted_cats,
        "favorite_cats": favorite_cats,
    })


def home(request):
    cats = Cat.objects.all()[:3]  # Show 3 random cats
    return render(request, "home.html", {"cats": cats})


@login_required
def add_to_favorites(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    
    # Check if already favorited
    favorite, created = Favorite.objects.get_or_create(user=request.user, cat=cat)

    if created:
        messages.success(request, f"{cat.name} added to your favorites!")
    else:
        messages.info(request, f"{cat.name} is already in your favorites!")

    return redirect("cat_list")  # ✅ Redirecting to cat list

@login_required
def remove_from_favorites(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    favorite = Favorite.objects.filter(user=request.user, cat=cat)

    if favorite.exists():
        favorite.delete()
        messages.success(request, f"{cat.name} removed from favorites!")
    
    return redirect("dashboard")  # ✅ Redirect back to dashboard

