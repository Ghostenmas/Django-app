# Generated by Django 4.0.4 on 2022-06-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_test_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='sex',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
