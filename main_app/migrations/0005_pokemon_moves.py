# Generated by Django 5.0 on 2023-12-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_move_alter_battle_options_alter_battle_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='main_app.move'),
        ),
    ]
