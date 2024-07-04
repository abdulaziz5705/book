# Generated by Django 5.0.6 on 2024-07-04 19:52

import book.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_author_image_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=book.helpers.Save.save_image),
        ),
    ]
