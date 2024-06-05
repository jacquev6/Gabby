from sqlalchemy import orm
import sqlalchemy as sql

from .database_utils import OrmBase

from .projects import Project
from .textbooks import Textbook


class Adaptation(OrmBase):
    __tablename__ = "adaptations"

    __mapper_args__ = {
        "polymorphic_on": "kind",
    }

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    kind: orm.Mapped[str] = orm.mapped_column(sql.String(16))

    exercise: orm.Mapped["Exercise"] = orm.relationship(back_populates="adaptation")


class Exercise(OrmBase):
    __tablename__ = "exercises"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="exercises")

    textbook_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(Textbook.id))
    textbook: orm.Mapped[Textbook | None] = orm.relationship(back_populates="exercises")
    textbook_page: orm.Mapped[int | None]
    bounding_rectangle: orm.Mapped[dict | None] = orm.mapped_column(sql.JSON)

    number: orm.Mapped[str]
    instructions: orm.Mapped[str]
    wording: orm.Mapped[str]
    example: orm.Mapped[str]
    clue: orm.Mapped[str]

    adaptation_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(Adaptation.id))
    adaptation: orm.Mapped[Adaptation | None] = orm.relationship(back_populates="exercise")

    extraction_events: orm.Mapped[list["ExtractionEvent"]] = orm.relationship(back_populates="exercise")

class ExtractionEvent(OrmBase):
    __tablename__ = "extraction_events"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    exercise_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Exercise.id))
    exercise: orm.Mapped[Exercise] = orm.relationship(back_populates="extraction_events")

    event: orm.Mapped[str]


class GenericAdaptation(Adaptation):
    __tablename__ = "adaptations__g"
    __mapper_args__ = {
        "polymorphic_identity": "g",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)


class SelectThingsAdaptation(Adaptation):
    __tablename__ = "adaptations__st"
    __mapper_args__ = {
        "polymorphic_identity": "st",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    punctuation: orm.Mapped[bool]
    words: orm.Mapped[bool]
    colors: orm.Mapped[int]


class FillWithFreeTextAdaptation(Adaptation):
    __tablename__ = "adaptations__fwft"
    __mapper_args__ = {
        "polymorphic_identity": "fwft",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    placeholder: orm.Mapped[str]


class MultipleChoicesInInstructionsAdaptation(Adaptation):
    __tablename__ = "adaptations__mcii"
    __mapper_args__ = {
        "polymorphic_identity": "mcii",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    placeholder: orm.Mapped[str]


class MultipleChoicesInWordingAdaptation(Adaptation):
    __tablename__ = "adaptations__mciw"
    __mapper_args__ = {
        "polymorphic_identity": "mciw",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)
