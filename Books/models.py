from django.db import models



lan = [
    ('en', 'Ingilizce'),
    ('tr', 'Turkce')
]



class BookCategory(models.Model):
    title           = models.CharField(max_length=128)

    def __str__(self):
        return self.title



class Book(models.Model):
    language        = models.CharField(max_length=2,choices=lan,default='en')
    bookcategory    = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)
    name            = models.CharField(max_length=128)
    price           = models.IntegerField()
    sender          = models.CharField(max_length=128)
    subtitle        = models.TextField()
    datetime        = models.DateTimeField()
    image           = models.ImageField()
    file           = models.FileField()
    author          = models.CharField(max_length=64)
    Type            = models.CharField(max_length=128)
    pages           = models.IntegerField()
    dill            = models.CharField(max_length=64)


    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name


