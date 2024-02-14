from django.db import models

class House(models.Model):
    owner = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    negotiable = models.BooleanField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} - {self.area}'