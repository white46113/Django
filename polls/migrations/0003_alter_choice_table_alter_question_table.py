# Generated by Django 5.2.2 on 2025-06-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_votes'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]
