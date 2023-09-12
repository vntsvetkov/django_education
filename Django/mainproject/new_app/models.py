from django.db import models
import datetime

# Пользователи
class Person(models.Model):
    name = models.CharField(max_length=30, default="Неизвестно")
    surname = models.CharField(max_length=30, default="Неизвестно")
    phone = models.CharField(max_length=17, default="Неизвестно")
    email = models.EmailField(unique=True, null=True, blank=True)
    city = models.CharField(max_length=30, default="Неизвестно")
    # Необходимо связать пользователя с его аккаунтом

    def __str__(self) -> str:
        return f"{self.surname} {self.name[0]}."


# Аккаунт
class Account(models.Model):
    login = models.CharField(max_length=30, default="Неизвестно")
    password = models.CharField(max_length=30, default="Неизвестно")
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.login}"


# Тема статьи
class Theme(models.Model):
    name = models.CharField(max_length=30, default="Без названия")

    def __str__(self) -> str:
        return f"{self.name}"


# Статья
class Article(models.Model):
    title = models.CharField(max_length=30, default="Без названия")
    author = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    date = models.DateField(default=datetime.date.today())
    description = models.TextField(default="Статья в разработке")
    theme = models.ManyToManyField(Theme)

    def __str__(self):
        return self.title



# Многие ко многим 
# class ArticlesThemes(models.Model):
#     id_article = models.ForeignKey(Article)
#     id_theme = models.ForeignKey(Theme)


# БД для хранения email адресов для рассылки
class MailingAddress(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.email


