# Generated by Django 4.2.2 on 2023-06-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_image_image_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='decouvrir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150)),
                ('DecouvreImage', models.ImageField(upload_to='')),
            ],
        ),
    ]