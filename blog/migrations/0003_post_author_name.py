# Generated by Django 2.1.1 on 2020-07-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]