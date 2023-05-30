from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import Profile
# Create your models here.

# getting user model object
User = get_user_model()


class Post(models.Model):
    '''
        this is a class to define posts for blog app
    '''
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    images = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    categoy = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    publishes_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name  = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    