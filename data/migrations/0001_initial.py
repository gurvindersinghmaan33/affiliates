# Generated by Django 4.1.4 on 2023-01-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=300)),
                ('label', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('price_text', models.CharField(max_length=300)),
                ('price_main', models.CharField(max_length=300)),
                ('profit_link', models.CharField(max_length=300)),
            ],
        ),
    ]
