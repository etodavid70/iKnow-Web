# Generated by Django 4.2.6 on 2023-10-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathnews', '0006_alter_mathnews_heading_alter_mathnews_paragraph1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathnews',
            name='heading',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='mathnews',
            name='paragraph1',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='mathnews',
            name='paragraph2',
            field=models.CharField(max_length=1024),
        ),
    ]