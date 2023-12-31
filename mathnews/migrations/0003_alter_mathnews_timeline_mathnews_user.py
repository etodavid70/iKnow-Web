# Generated by Django 4.2.6 on 2023-10-15 16:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mathnews', '0002_alter_mathnews_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathnews',
            name='timeline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='MathNews_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(max_length=70)),
                ('paragraph1', models.TextField(max_length=200)),
                ('paragraph2', models.TextField(max_length=200)),
                ('paragraph3', models.TextField(max_length=200)),
                ('timeline', models.DateField(default=datetime.date.today)),
                ('is_authorized', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
