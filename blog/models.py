from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)
    time_upload = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thubnails/')
    published = models.BooleanField()
    category = models.ManyToManyField(Category)
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title
