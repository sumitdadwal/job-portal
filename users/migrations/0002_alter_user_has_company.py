# Generated by Django 5.0.3 on 2024-03-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='has_company',
            field=models.BooleanField(default=False),
        ),
    ]
