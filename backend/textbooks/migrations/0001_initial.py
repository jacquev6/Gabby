# Generated by Django 5.0.2 on 2024-02-22 14:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('sha256', models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-f]{64}$')])),
                ('bytes_count', models.IntegerField()),
                ('pages_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255, null=True)),
                ('year', models.IntegerField(null=True)),
                ('isbn', models.CharField(max_length=25, null=True, validators=[django.core.validators.RegexValidator('[0-9]')])),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('textbook_start_page', models.IntegerField()),
                ('pdf_file_start_page', models.IntegerField()),
                ('pages_count', models.IntegerField()),
                ('pdf_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='textbooks.pdffile')),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='textbooks.textbook')),
            ],
        ),
        migrations.CreateModel(
            name='PdfFileNaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pdf_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='namings', to='textbooks.pdffile')),
            ],
            options={
                'unique_together': {('pdf_file', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page', models.IntegerField()),
                ('number', models.IntegerField()),
                ('instructions', models.TextField(blank=True)),
                ('example', models.TextField(blank=True)),
                ('clue', models.TextField(blank=True)),
                ('wording', models.TextField(blank=True)),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='textbooks.textbook')),
            ],
            options={
                'unique_together': {('textbook', 'page', 'number')},
            },
        ),
    ]
