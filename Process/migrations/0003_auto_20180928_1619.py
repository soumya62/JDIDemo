# Generated by Django 2.1.1 on 2018-09-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0002_auto_20180928_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='Name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
