# Generated by Django 5.0.4 on 2024-05-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_day_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='title',
            field=models.CharField(max_length=200, verbose_name='タイトル'),
        ),
    ]
