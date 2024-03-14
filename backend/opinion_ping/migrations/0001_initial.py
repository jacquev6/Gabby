# Generated by Django 5.0.2 on 2024-03-02 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=16, null=True)),
                ('prev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='opinion_ping.ping')),
            ],
        ),
    ]
