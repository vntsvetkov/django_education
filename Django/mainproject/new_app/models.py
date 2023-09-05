from django.db import models


class Article(models.Model):
    
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    date = models.DateField()
    description = models.TextField()


class MailingAddress(models.Model):
    ...

class Pesron(models.Model):
    ...

class Application(models.Model):
    ...

