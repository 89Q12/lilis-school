# Generated by Django 3.2.7 on 2021-09-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20210913_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='TimeToRead',
            field=models.IntegerField(),
        ),
    ]
