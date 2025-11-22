from django.db import models
from django.core.validators import MinValueValidator

class Mlibro(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)  
    stock = models.IntegerField(validators=[MinValueValidator(0)])  
    def __str__(self):
        return self.title
    
# Create your models here.
