# Generated by Django 3.2.5 on 2021-08-02 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_book_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Category',
            new_name='category',
        ),
    ]
