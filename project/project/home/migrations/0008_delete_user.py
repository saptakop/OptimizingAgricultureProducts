# Generated by Django 4.0.3 on 2022-05-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_officer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]