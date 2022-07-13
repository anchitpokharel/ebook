from django.db import models

# Create your models here.    
class Contact_us(models.Model):
    
    your_name = models.CharField(max_length=255)
    your_number = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    flag = models.CharField(max_length=50, blank=True, editable=False)
class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    
class Author(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    image = models.ImageField()
    alt_desc_image = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    