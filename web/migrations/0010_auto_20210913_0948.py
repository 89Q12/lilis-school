# Generated by Django 3.2.7 on 2021-09-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_kontakt_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='wilkommenstext',
            name='BildBeschreibung',
            field=models.TextField(default='null=True', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wilkommenstext',
            name='SmallHeadLine',
            field=models.TextField(max_length=50),
        ),
    ]
