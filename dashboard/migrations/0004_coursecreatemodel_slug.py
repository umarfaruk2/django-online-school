# Generated by Django 4.2.3 on 2023-09-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_coursecreatemodel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecreatemodel',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
    ]
