# Generated by Django 3.2.13 on 2022-12-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibleapp', '0004_auto_20221228_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='discription',
            field=models.TextField(max_length=100),
        ),
    ]