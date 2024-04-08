# Generated by Django 5.0.4 on 2024-04-08 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('textbooks', '0003_initial_patch'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdaptedExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='FillWithFreeTextAdaptedExercise',
            fields=[
                ('adaptedexercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='textbooks.adaptedexercise')),
                ('placeholder', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('textbooks.adaptedexercise',),
        ),
        migrations.CreateModel(
            name='SelectWordsAdaptedExercise',
            fields=[
                ('adaptedexercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='textbooks.adaptedexercise')),
                ('colors', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('textbooks.adaptedexercise',),
        ),
        migrations.AddField(
            model_name='exercise',
            name='adapted',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exercise', to='textbooks.adaptedexercise'),
        ),
    ]
