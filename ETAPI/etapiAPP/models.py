from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Category(models.TextChoices):
    Groceries = 'G', 'Groceries'
    Leisure = 'L', 'Leisure'
    Electronics = 'E', 'Electronics'
    Utilities = 'U', 'Utilities'
    Clothing = 'C', 'Clothing'
    Health = 'H', 'Health'
    Others = 'O', 'Others'


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=1, choices=Category.choices)

    def __str__(self):
        return self.description


