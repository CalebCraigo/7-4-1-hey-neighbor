# Generated by Django 2.2.6 on 2019-10-14 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hey_neighbor', '0005_auto_20191012_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='image',
            field=models.ImageField(default='testimage', upload_to='images/'),
            preserve_default=False,
        ),
    ]