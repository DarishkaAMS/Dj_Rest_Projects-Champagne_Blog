# Generated by Django 2.2.14 on 2021-04-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champagne', '0002_champagneblogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='champagneblogpost',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
