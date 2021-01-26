from django.db import models

# Create your models here.



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

