# Generated by Django 5.1.2 on 2024-10-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
