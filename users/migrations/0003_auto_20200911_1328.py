# Generated by Django 2.2.16 on 2020-09-11 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200911_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='fax',
        ),
    ]