from django.db import models

# Create your models here.
class Cat(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    breed=models.TextField()
    #image=models.ImageField(upload_to='cat_images/')
    description=models.TextField()
    available=models.BooleanField(default=False)

    def __str__(self):
        return self.name