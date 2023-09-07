from django.db import models
import datetime


# Статья
class Article(models.Model):
    title = models.CharField(max_length=30, default="Без названия")
    author = models.CharField(max_length=20, default="Неизвестный автор")
    date = models.DateField(default=datetime.date.today())
    description = models.TextField(default="Статья в разработке")

    def __str__(self):
        return self.title



# БД для хранения email адресов для рассылки
class MailingAddress(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.email

# Пользователи
class Pesron(models.Model):
    ...

