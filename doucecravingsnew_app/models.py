from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class List_Of_Items(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    author = models.CharField(max_length=50, default='Admin')
    date_modified = models.DateTimeField(default=datetime.now())
    description = models.TextField(default='')
    toppings = models.CharField(default='Funfetti,Brownie Crumbles,Chocolate Chips, Oreo Crumbles,M&Ms')
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('doucecravingsnew_app:item_details', args=[self.id])

#Home SlideShow
class Home(models.Model):
    slide_image = models.ImageField()

#Best Sellers Dashboard

class Best_Sellers(models.Model):
    box_image = models.ImageField()
    box_name = models.CharField()


#Main Page Nav and Catlog
class Catlog(models.Model):
    item_name = models.CharField(max_length=200)
    item_image = models.ImageField()

#Reviews
class Review(models.Model):
    text = models.TextField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

#Comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(List_Of_Items, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

