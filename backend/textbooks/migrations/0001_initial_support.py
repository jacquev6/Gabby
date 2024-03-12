from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.RunSQL(
            """
            CREATE COLLATION textbooks_exercise_number (provider = icu, locale = 'en-u-kn-true');
            """,
            """
            DROP COLLATION textbooks_exercise_number;
            """,
        ),
    ]
