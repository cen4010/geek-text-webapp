from django.db import models

class Book(models.Model):
    title = models.CharField(
        'Title of the book',
        max_length=255)
    author = models.ForeignKey(
        'Author',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    description = models.TextField(
        'Description of book contents and misc info',
        max_length=500,
        blank=True)
    genre = models.ForeignKey(
        'Genre',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        'Publisher',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publish_date = models.DateField(
        'Date publisher initially released current book version')

    def __str__(self):
        return '{} -- {}'.format(self.author, self.title)

class Author(models.Model):
    name = models.CharField(
        'Name of author',
        max_length=255)
    bio = models.TextField(
        'Short biography of author and description of work',
        max_length=500,
        blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Publisher(models.Model):
    name = models.CharField(
        'Name of publishing company',
        max_length=255)
    location = models.CharField(
        'Street address of publishing company',
        max_length=255,
        blank=True)
    website = models.URLField(
        'Publisher home webpage',
        blank=True)

class Genre(models.Model):
    name = models.CharField(
        'Short name for genre',
        max_length=16)
