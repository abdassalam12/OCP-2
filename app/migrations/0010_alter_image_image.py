# Generated by Django 4.2.2 on 2023-06-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_offrefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=models.ImageField(default='images/B.jpg', null=True, upload_to='images/'),
        ),
    ]
