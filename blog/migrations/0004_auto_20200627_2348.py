# Generated by Django 3.0 on 2020-06-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]