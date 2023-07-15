from django.db import models



lan = [
    ('en', 'Ingilizce'),
    ('tr', 'Turkce')
]

class Manager(models.Model):
    language            = models.CharField(max_length=2,choices=lan,default='en')
    name                = models.CharField(max_length=128, blank=False, null=False)
    lastname            = models.CharField(max_length=128, blank=False, null=False)
    department          = models.CharField(max_length=128, blank=False, null=False)
    age                 = models.IntegerField()
    phone               = models.CharField(max_length=32, blank=False, null=False)
    email               = models.EmailField(max_length=64, blank=False, null=False)
    image               = models.ImageField()
    description         = models.TextField()
    address             = models.TextField()


    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Manager'

    def __str__(self):
        return self.name








class Project(models.Model):
    language            = models.CharField(max_length=2,choices=lan,default='en')
    name                = models.CharField(max_length=128, blank=False, null=False)
    description         = models.TextField()
    image               = models.ImageField()
    link_project        = models.CharField(max_length=128, blank=False, null=False)
    start_date          = models.DateField(blank=True, null=True)
    end_date            = models.DateField(blank=True, null=True)
    manager             = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='manager')


    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name



class Experience(models.Model):
    language            = models.CharField(max_length=128, default='en')
    title               = models.CharField(max_length=128, blank=False, null=False)
    description         = models.TextField()
    start_date          = models.DateField(blank=True, null=True)
    end_date            = models.DateField(blank=True, null=True)
    file                = models.FileField()
    country             = models.CharField(max_length=128, blank=False, null=False)


    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.title





class CategoryEducation(models.Model):
    category            = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.category

class Education(models.Model):
    language            = models.CharField(max_length=128, default='en')
    categoryEducation   = models.ForeignKey(CategoryEducation, on_delete=models.CASCADE, blank=False, null=False)
    name                = models.CharField(max_length=128, blank=False, null=False)
    description         = models.TextField()
    start_date          = models.DateTimeField(blank=True, null=True)
    end_date            = models.DateTimeField(blank=True, null=True)
    file                = models.FileField()
    country             = models.CharField(max_length=128, blank=False, null=False)


    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.name




class Contact(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    surname = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=128, blank=False, null=False)
    content = models.TextField()

    def __str__(self):
        return self.name







