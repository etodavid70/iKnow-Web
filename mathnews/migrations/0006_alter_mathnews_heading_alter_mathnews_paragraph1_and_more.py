# Generated by Django 4.2.6 on 2023-10-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathnews', '0005_delete_mathnewsuser_remove_mathnews_paragraph3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathnews',
            name='heading',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mathnews',
            name='paragraph1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mathnews',
            name='paragraph2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mathnews',
            name='timeline',
            field=models.DateField(),
        ),
    ]
