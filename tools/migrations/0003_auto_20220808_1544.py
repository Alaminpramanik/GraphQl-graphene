# Generated by Django 3.1.5 on 2022-08-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_auto_20220807_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='article'),
        ),
    ]
