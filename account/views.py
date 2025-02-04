from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
            return redirect("dashboard")  # Redirect to user dashboard
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
    return render(request, "account/dashboard.html")