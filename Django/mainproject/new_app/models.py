from django.db import models
import datetime


# Статья
class Article(models.Model):
    title = models.CharField(max_length=30, default="Без названия")
    author = models.CharField(max_length=20, default="Неизвестный автор")
    date = models.DateField(default=datetime.date.today())
    description = models.TextField(default="Статья в разработке")


# БД для хранения email адресов для рассылки
class MailingAddress(models.Model):
    ...

# Пользователи
class Pesron(models.Model):
    ...

