# Generated by Django 4.2.6 on 2023-10-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathnews', '0009_rename_mathnews_technews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technews',
            name='paragraph1',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='technews',
            name='paragraph2',
            field=models.TextField(max_length=1024),
        ),
    ]
