# Generated by Django 4.2.4 on 2023-09-14 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0012_article_theme'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticlesThemes',
            new_name='Profile',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 14)),
        ),
    ]
