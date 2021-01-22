from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)



class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)