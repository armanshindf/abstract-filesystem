# Generated by Django 3.1.5 on 2021-01-13 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htree', '0005_auto_20210113_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pseudofs',
            old_name='fname',
            new_name='ffile',
        ),
        migrations.AlterField(
            model_name='pseudofs',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ffile_children', to='htree.pseudofs', verbose_name='Родительский каталог'),
        ),
    ]