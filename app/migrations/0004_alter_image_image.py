# Generated by Django 4.2.2 on 2023-06-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]