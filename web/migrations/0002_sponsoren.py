# Generated by Django 3.2.7 on 2021-09-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsoren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Summe', models.IntegerField()),
                ('Statement', models.TextField(max_length=2000)),
            ],
        ),
    ]