# Generated by Django 3.2.7 on 2021-09-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_kontakt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeadLine', models.TextField(max_length=100)),
                ('Beschreibung', models.TextField(max_length=2000)),
                ('Bild', models.ImageField(upload_to='pictures/')),
            ],
        ),
        migrations.DeleteModel(
            name='FotosVideos',
        ),
    ]
