import json

from .models import Project


def make_extraction_report(project_id):
    project = Project.objects.get(id=project_id)
    return {
        "project": {
            "title": project.title,
            "textbooks": [
                {
                    "title": textbook.title,
                    "exercises": [
                        {
                            "page": exercise.textbook_page,
                            "number": exercise.number,
                            "events": [
                                json.loads(event.event)
                                for event in exercise.extraction_events.order_by('id')
                            ],
                        }
                        for exercise in textbook.exercises.order_by("textbook_page", "number")
                    ],
                }
                for textbook in project.textbooks.order_by("id")
            ],
        },
    }
