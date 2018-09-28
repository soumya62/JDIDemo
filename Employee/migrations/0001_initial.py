# Generated by Django 2.1.1 on 2018-09-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPNO', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('EmpBloodGroup', models.CharField(max_length=50, null=True, unique=True)),
                ('EmpContactNo', models.CharField(max_length=50, null=True, unique=True)),
                ('EmpDOJ', models.CharField(max_length=50, null=True, unique=True)),
            ],
        ),
    ]
