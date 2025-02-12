from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from django.contrib.auth.decorators import login_required, user_passes_test
from account.models import Favorite

# Create your views here.
# Admin Check
def is_admin(user):
    return user.is_superuser

# List all cats
def cat_list(request):
    cats = Cat.objects.all()
    favorite_cats = []

    if request.user.is_authenticated:
        favorite_cats = Favorite.objects.filter(user=request.user).values_list("cat_id", flat=True)

    return render(request, "cat/cat_list.html", {
        "cats": cats,
        "favorite_cats": favorite_cats,  # Pass favorite cat IDs to the template
    })

# Create a new cat (Admin Only)
@user_passes_test(is_admin)

def cat_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        breed = request.POST["breed"]
        age = request.POST["age"]
        image = request.FILES.get("image")

        Cat.objects.create(name=name, breed=breed, age=age, image=image)
        return redirect("cat_list")

    return render(request, "cat/cat_form.html")

# Update cat details (Admin Only)
@user_passes_test(is_admin)
def cat_update(request, pk):
    cat = get_object_or_404(Cat, pk=pk)

    if request.method == "POST":
        cat.name = request.POST["name"]
        cat.breed = request.POST["breed"]
        cat.age = request.POST["age"]
        cat.image = request.FILES.get("image", cat.image)
        cat.save()
        return redirect("cat_list")

    return render(request, "cat/cat_form.html", {"cat": cat})

# Delete a cat (Admin Only)
@user_passes_test(is_admin)

def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == "POST":
        cat.delete()
        return redirect("cat_list")

    return render(request, "cat/cat_confirm_delete.html", {"cat": cat})