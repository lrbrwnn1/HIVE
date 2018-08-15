# Generated by Django 2.0.6 on 2018-06-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchFunction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='agency',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='grant',
            name='docNum',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='grant',
            name='guidelink',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='grant',
            name='parentFOA',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='grant',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='city',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='country',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='department',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='institution',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='office',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='phone',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='state',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='guidelink',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='medline',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.TextField(default=''),
        ),
    ]