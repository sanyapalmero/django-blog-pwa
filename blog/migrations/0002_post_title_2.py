# Generated by Django 3.2.9 on 2021-12-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название 2'),
        ),
    ]
