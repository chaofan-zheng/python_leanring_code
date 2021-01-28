# Generated by Django 2.2.17 on 2021-01-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='sing',
            new_name='sign',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='info',
            field=models.CharField(default='', max_length=150, verbose_name='个人简介'),
        ),
    ]