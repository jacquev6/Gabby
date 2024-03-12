from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("textbooks", "0002_initial"),
    ]

    operations = [
        # A "fat" foreign key that Django's ORM cannot handle
        # https://stackoverflow.com/a/12299547/905845
        migrations.RunSQL(
            """
            ALTER TABLE textbooks_exercise
            ADD CONSTRAINT textbooks_exercise_textbook_project_matches_exercise_project
              FOREIGN KEY (project_id, textbook_id)
              REFERENCES textbooks_textbook(project_id, id)
              ON DELETE CASCADE
            """,
            """
            ALTER TABLE textbooks_exercise
            DROP CONSTRAINT textbooks_exercise_textbook_project_matches_exercise_project
            """,
        ),
    ]
