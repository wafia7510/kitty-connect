from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)  
    #image = models.ImageField(upload_to='cat_images/', blank=True, null=True) 
    image = models.ImageField(upload_to='cat_images/', null=True, blank=True)

    description = models.TextField()
    available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name