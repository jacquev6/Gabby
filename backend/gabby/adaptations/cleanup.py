from ..database_utils import Session


def delete_previous_adaptation(*, exercise, **kwargs):
    if exercise.adaptation is not None:
        session = Session.object_session(exercise.adaptation)
        session.delete(exercise.adaptation)
    return {"exercise": exercise, **kwargs}
