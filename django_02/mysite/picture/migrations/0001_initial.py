# Generated by Django 2.2 on 2020-07-13 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='标题')),
                ('image', models.ImageField(blank=True, upload_to='mypictures', verbose_name='图片')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
