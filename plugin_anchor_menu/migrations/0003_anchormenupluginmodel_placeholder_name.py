# Generated by Django 2.2.7 on 2020-03-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin_anchor_menu', '0002_anchormenupluginmodel_top_offset_minus'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchormenupluginmodel',
            name='placeholder_name',
            field=models.SlugField(default='content', max_length=254, verbose_name='Placeholder name'),
        ),
    ]