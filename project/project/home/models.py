from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    result = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class Survey(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return self.name


