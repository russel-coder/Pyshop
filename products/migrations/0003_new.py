# Generated by Django 3.1.5 on 2021-01-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='Date shipped')),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
