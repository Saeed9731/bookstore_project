# Generated by Django 4.0.6 on 2022-08-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recomment',
            field=models.BooleanField(default=True),
        ),
    ]
