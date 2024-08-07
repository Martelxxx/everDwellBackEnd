# Generated by Django 4.2.14 on 2024-07-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents_api', '0003_alter_agent_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('preapproval', models.BooleanField(default=False)),
                ('budget', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('homerating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
