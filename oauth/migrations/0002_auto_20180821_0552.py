# Generated by Django 2.0.5 on 2018-08-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='token_type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Token type'),
        ),
    ]
