# Generated by Django 4.2.2 on 2023-07-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_bangalo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bangalo',
            name='ville',
            field=models.CharField(default='safi'),
        ),
    ]
