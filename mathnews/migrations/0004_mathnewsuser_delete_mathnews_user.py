# Generated by Django 4.2.6 on 2023-10-17 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathnews', '0003_alter_mathnews_timeline_mathnews_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MathNewsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(max_length=70)),
                ('paragraph1', models.TextField(max_length=200)),
                ('paragraph2', models.TextField(max_length=200)),
                ('timeline', models.DateField(default=datetime.date.today)),
                ('author', models.CharField(max_length=20)),
                ('is_authorized', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='MathNews_user',
        ),
    ]
