from django.db import models
from datetime import *






class SubCategory(models.Model):
    article                   = models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    title                   = models.CharField(max_length=128, blank=True, null=True)
    image                   = models.ImageField(blank=True, null=True)
    code_image              = models.ImageField(blank=True, null=True)
    sub_title               = models.TextField(blank=True, null=True)
    content                 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'




class Category(models.Model):
    title               = models.CharField(max_length=128, blank=False, null=False)
    image               = models.ImageField()
    # subCategory         = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.title



class Group(models.Model):
    name                = models.CharField(max_length=128, blank=False, null=False)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    name                = models.CharField(max_length=128, blank=False, null=False)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    group               = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    image               = models.ImageField()
    author              = models.CharField(max_length=128, blank=False, null=False)
    date                = models.DateField()
    content             = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name











