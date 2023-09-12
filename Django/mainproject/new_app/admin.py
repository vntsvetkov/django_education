from django.contrib import admin
from .models import Article
from .models import MailingAddress
from .models import Person
from .models import Account


admin.site.register(Article)
admin.site.register(MailingAddress)
admin.site.register(Person)
admin.site.register(Account)
