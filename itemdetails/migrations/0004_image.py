# Generated by Django 2.2.4 on 2020-04-05 15:09

from django.db import migrations, models
import itemdetails.models


class Migration(migrations.Migration):

    dependencies = [
        ('itemdetails', '0003_auto_20200322_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=itemdetails.models.upload_path)),
            ],
        ),
    ]
