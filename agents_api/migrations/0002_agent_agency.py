# Generated by Django 4.2.14 on 2024-07-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agency',
            field=models.CharField(default='Default Agency', max_length=100),
        ),
    ]
