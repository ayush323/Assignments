from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.core.validators import MinLengthValidator 

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key= True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    emailAddress=models.EmailField()
    




class post(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length= 100)
    image=models.ImageField(upload_to = 'posts', null = True)
    date = models.DateField(auto_now= True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author= models.ForeignKey(Author, on_delete=models.SET_NULL, related_name= "posts", null= True)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.AutoField(primary_key= True)
    caption= models.CharField(max_length=10)
    post = models.ManyToManyField(post, related_name= "tag")

class comments(models.Model):
    id = models.AutoField(primary_key= True)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    text = models.TextField(max_length = 400)
    post = models.ForeignKey(post,on_delete = CASCADE, related_name = 'comments')