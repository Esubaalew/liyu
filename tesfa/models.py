from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Author(models.Model):
        first_name = models.CharField(max_length=15)
        last_name = models.CharField(max_length=15)
        about = models.TextField()
        def __str__(self):
             return self.first_name

class Post(models.Model):
    title = models.CharField(max_length=30 )
    slug = models.SlugField(max_length=30)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey( Author,  on_delete=models.CASCADE) 
    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Status(models.IntegerChoices):
        PUBLISHED = 1, 'published'
        DRAFT = 2, 'draft'
    status = models.IntegerField(choices=Status.choices)
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    def __str__(self):
        return self.title
