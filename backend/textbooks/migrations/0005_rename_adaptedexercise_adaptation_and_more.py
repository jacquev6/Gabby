from django.db import migrations, models


# https://stackoverflow.com/a/61723620/905845
class AlterModelBases(migrations.operations.models.ModelOperation):
    reduce_to_sql = False
    reversible = True

    def __init__(self, name, bases):
        self.bases = bases
        super().__init__(name)

    def state_forwards(self, app_label, state):
        """
        Overwrite a models base classes with a custom list of
        bases instead, then force Django to reload the model
        with this (probably completely) different class hierarchy.
        """
        state.models[app_label, self.name_lower].bases = self.bases
        state.reload_model(app_label, self.name_lower)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def describe(self):
        return "Update %s bases to %s" % (self.name, self.bases)


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0004_adaptedexercise_exercise_bounding_rectangle_and_more'),
    ]

    operations = [
        # Rename derived models
        migrations.RenameModel(
            old_name='SelectWordsAdaptedExercise',
            new_name='SelectThingsAdaptation',
        ),
        migrations.RenameModel(
            old_name='FillWithFreeTextAdaptedExercise',
            new_name='FillWithFreeTextAdaptation',
        ),

        # Rename base model as in https://stackoverflow.com/a/61723620/905845
        migrations.RenameField(
            model_name='fillwithfreetextadaptation',
            old_name='adaptedexercise_ptr',
            new_name='adaptation_ptr',
        ),
        migrations.RenameField(
            model_name='selectthingsadaptation',
            old_name='adaptedexercise_ptr',
            new_name='adaptation_ptr',
        ),
        AlterModelBases("fillwithfreetextadaptation", (models.Model,)),
        AlterModelBases("selectthingsadaptation", (models.Model,)),
        migrations.RenameModel(
            old_name='AdaptedExercise',
            new_name='Adaptation',
        ),
        migrations.AlterField(
            model_name='fillwithfreetextadaptation',
            name='adaptation_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=models.deletion.CASCADE,
                parent_link=True, primary_key=True,
                serialize=False,
                to='textbooks.Adaptation',
            ),
        ),
        migrations.AlterField(
            model_name='selectthingsadaptation',
            name='adaptation_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='textbooks.Adaptation',
            ),
        ),

        # Rename field to base class
        migrations.RenameField(
            model_name='exercise',
            old_name='adapted',
            new_name='adaptation',
        ),

        # Other changes, more usual
        migrations.AddField(
            model_name='SelectThingsAdaptation',
            name='punctuation',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='SelectThingsAdaptation',
            name='words',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
