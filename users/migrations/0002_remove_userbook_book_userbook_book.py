# Generated by Django 5.0.6 on 2024-07-13 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_author_image'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='book',
        ),
        migrations.AddField(
            model_name='userbook',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
