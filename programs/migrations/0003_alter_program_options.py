# Generated by Django 3.2.18 on 2023-03-28 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_delete_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['-id']},
        ),
    ]
