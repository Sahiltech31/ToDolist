# Generated by Django 5.1.5 on 2025-04-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_todolist_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
