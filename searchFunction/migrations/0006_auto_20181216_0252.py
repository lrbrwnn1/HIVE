# Generated by Django 2.1.2 on 2018-12-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchFunction', '0005_remove_clinicaltrial_cttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigator',
            name='MI',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='city',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='country',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='department',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='fName',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='institution',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='investigator_tag',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='lName',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='office',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='phone',
            field=models.CharField(default=' ', max_length=25),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='position',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='state',
            field=models.TextField(default=' '),
        ),
    ]
