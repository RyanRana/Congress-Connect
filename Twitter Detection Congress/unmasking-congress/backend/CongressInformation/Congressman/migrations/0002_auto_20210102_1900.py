# Generated by Django 3.1.4 on 2021-01-02 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Congressman', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Congressman',
            new_name='Representative',
        ),
    ]