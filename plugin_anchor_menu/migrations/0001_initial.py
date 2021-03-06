# Generated by Django 2.2.7 on 2020-03-17 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnchorMenuPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='plugin_anchor_menu_anchormenupluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('menu_id', models.SlugField(default='plugin_anchor_menu', max_length=254, verbose_name='The internal menu ID')),
                ('link_type', models.CharField(choices=[('h', "Add '#anchor' to browser addess."), ('s', "Don't add '#anchor' to browser addess.")], default='s', max_length=1, verbose_name='Link type')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AnchorPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='plugin_anchor_menu_anchorpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
