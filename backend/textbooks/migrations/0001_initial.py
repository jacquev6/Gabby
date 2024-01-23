# Generated by Django 5.0.1 on 2024-01-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pdf_sha1', models.CharField(max_length=40)),
                ('pdf_page', models.IntegerField()),
                ('number', models.TextField()),
                ('instructions', models.TextField(blank=True)),
                ('example', models.TextField(blank=True)),
                ('clue', models.TextField(blank=True)),
                ('wording', models.TextField(blank=True)),
            ],
        ),
    ]
