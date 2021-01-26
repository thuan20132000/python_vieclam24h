from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):



    STATUS_CHOICES = (
        ("pending","PENDING"),
        ("daft","DRAFT"),
        ("published","PUBLISHED")
    )

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/category/',blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="pending")

    def __str__(self):
        return self.name





class Occupation(models.Model):
    
    STATUS_CHOICES = (
        ("pending","PENDING"),
        ("daft","DRAFT"),
        ("published","PUBLISHED")
    )

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/occupation/',blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(
        Category,
        related_name='occupation',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name




class Job(models.Model):

    STATUS_CHOICES = (
        ("pending","PENDING"),
        ("daft","DRAFT"),
        ("published","PUBLISHED")
    )

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.TextField()
    suggestion_price = models.DecimalField(max_digits=18,decimal_places=2)
    image = models.ImageField(upload_to='uploads/job/',blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(
        User,
        related_name='job',
        on_delete=models.CASCADE
    )
    occupation = models.ForeignKey(
        Occupation,
        related_name='job',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class JobImages(models.Model):
    image = models.ImageField(upload_to='uploads/job',blank=True)
    job = models.ForeignKey(Job,related_name='job_images',on_delete=models.CASCADE)