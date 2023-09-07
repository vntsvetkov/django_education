from django.contrib import admin
from .models import Article
from .models import MailingAddress


admin.site.register(Article)
admin.site.register(MailingAddress)