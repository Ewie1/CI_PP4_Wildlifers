# Generated by Django 3.2.18 on 2023-02-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_alter_country_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Survival_cateogory',
            new_name='Survival_category',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='animal_cateogory',
            new_name='animal_category',
        ),
        migrations.RenameField(
            model_name='survival_category',
            old_name='cateogory',
            new_name='category',
        ),
    ]
