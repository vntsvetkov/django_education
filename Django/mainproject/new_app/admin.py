from django.contrib import admin
from .models import Article
from .models import MailingAddress
from .models import Person


admin.site.register(Article)
admin.site.register(MailingAddress)
admin.site.register(Person)
