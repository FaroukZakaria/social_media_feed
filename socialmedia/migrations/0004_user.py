# Generated by Django 5.1.7 on 2025-03-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
