from django.contrib.auth.models import User
from django.db import models
from cat.models import Cat

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "cat")  # Prevent duplicate favorites

    def __str__(self):
        return f"{self.user.username} ❤️ {self.cat.name}"