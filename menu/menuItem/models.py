from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    isAvailable = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add = True)
    imageUrl = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
