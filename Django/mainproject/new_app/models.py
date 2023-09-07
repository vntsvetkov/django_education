from django.db import models
import datetime


# Статья
class Article(models.Model):
    title = models.CharField(max_length=30, default="Без названия")
    # Необходимо связать автора с экземпляром Person
    author = models.CharField(max_length=20, default="Неизвестный автор")
    date = models.DateField(default=datetime.date.today())
    description = models.TextField(default="Статья в разработке")

    def __str__(self):
        return self.title


# Тема статьи
class Theme(models.Model):
    ...


# Многие ко многим 
class ArticlesThemes(models.Model):
    ...


# БД для хранения email адресов для рассылки
class MailingAddress(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.email


# Пользователи
class Person(models.Model):
    name = models.CharField(max_length=30, default="Неизвестно")
    surname = models.CharField(max_length=30, default="Неизвестно")
    phone = models.CharField(max_length=17, default="Неизвестно")
    email = models.EmailField(unique=True, null=True, blank=True)
    city = models.CharField(max_length=30, default="Неизвестно")
    # Необходимо связать пользователя с его аккаунтом

# Аккаунт
class Account(models.Model):
    login = models.CharField(max_length=30, default="Неизвестно")
    password = models.CharField(max_length=30, default="Неизвестно")

