from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=132, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.category.name

