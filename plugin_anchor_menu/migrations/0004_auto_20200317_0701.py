# Generated by Django 2.2.7 on 2020-03-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin_anchor_menu', '0003_anchormenupluginmodel_placeholder_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anchormenupluginmodel',
            name='placeholder_name',
        ),
        migrations.AlterField(
            model_name='anchormenupluginmodel',
            name='top_offset_minus',
            field=models.IntegerField(default='80', verbose_name='Поправка на высоту меню'),
        ),
    ]
