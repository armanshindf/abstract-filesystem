# Generated by Django 3.1.5 on 2021-01-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htree', '0006_auto_20210113_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='pseudofs',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]
