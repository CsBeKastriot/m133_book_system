from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return '{}'.format(self.title)