# Generated by Django 5.0 on 2023-12-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('trainer', models.CharField(max_length=25)),
            ],
        ),
    ]
