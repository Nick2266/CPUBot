# Generated by Django 2.1.1 on 2018-09-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20180821_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='opt_out_email',
            field=models.BooleanField(default=False, verbose_name='Opted out email'),
        ),
        migrations.AddField(
            model_name='record',
            name='opt_out_pm',
            field=models.BooleanField(default=False, verbose_name='Opted out discord private message'),
        ),
    ]
