from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='cars/')
    def __str__(self): return self.model_name