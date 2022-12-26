from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name} - {self.address}'


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'
