from django.contrib import admin
from .models import Cat

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ("name", "breed", "age", "available")
    search_fields = ('name', 'breed', 'description')  # ✅ Search by description
    list_filter = ('available',)
    fields = ('name', 'breed', 'age', 'image', 'description', 'available')  # ✅ Ensure descriptio
