# Generated by Django 2.1.1 on 2018-09-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtestdata',
            name='BlogTest',
            field=models.IntegerField(max_length=50, null=True, unique=True),
        ),
    ]
