from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title

# Create your models here.
