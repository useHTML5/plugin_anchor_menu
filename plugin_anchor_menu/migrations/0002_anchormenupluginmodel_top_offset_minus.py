# Generated by Django 2.2.7 on 2020-03-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin_anchor_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchormenupluginmodel',
            name='top_offset_minus',
            field=models.IntegerField(default='40', verbose_name='Поправка на высоту меню'),
        ),
    ]
