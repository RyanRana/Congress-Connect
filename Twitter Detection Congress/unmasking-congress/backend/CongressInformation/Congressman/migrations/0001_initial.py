# Generated by Django 3.1.4 on 2021-01-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Congressman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('twitter_handle', models.CharField(max_length=100)),
            ],
        ),
    ]
