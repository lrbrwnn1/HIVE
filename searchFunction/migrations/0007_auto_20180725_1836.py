# Generated by Django 2.0.6 on 2018-07-25 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchFunction', '0006_auto_20180720_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authors_grants_list',
            old_name='author',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='authors_grants_list',
            name='grant_id',
        ),
    ]
