# Generated by Django 3.2.18 on 2023-03-20 17:53

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(blank=True)),
                ('update', models.DateTimeField()),
                ('content', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excert', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'DRAFT'), (1, 'POST')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
