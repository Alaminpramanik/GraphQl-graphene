# Generated by Django 3.1.5 on 2022-08-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20220820_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentkeyword',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='category'),
        ),
    ]