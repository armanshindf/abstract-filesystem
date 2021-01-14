# Generated by Django 3.1.5 on 2021-01-13 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('htree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pseudofs',
            name='content_type',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]