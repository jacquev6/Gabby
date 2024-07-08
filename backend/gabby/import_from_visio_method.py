import textwrap
from typing import Tuple
import json

from pydantic import BaseModel

from .database_utils import Session
from .orm_models import User, Project, Textbook, Exercise
from .testing import TransactionTestCase


# File format comes from external tool with some field names in French
class PageData(BaseModel):
    pdfSha256: str
    textbookPage: int
    imageHeight: int
    imageWidth: int
    class Contenu(BaseModel):
        class Exercice(BaseModel):
            class Textbox(BaseModel):
                contenu: str
                box: Tuple[Tuple[float, float], Tuple[float, float]]
            num: Textbox
            consigne: list[Textbox] = []
            enonce: list[Textbox] = []
            exemple: list[Textbox] = []
            conseil: list[Textbox] = []
        exercices: list[Exercice]
    contenu: Contenu


def import_page(session: Session, user: User, textbook: Textbook, page_data: PageData):
    def text_from_textboxes_list(textboxes: list[PageData.Contenu.Exercice.Textbox]) -> str:
        return "\n".join(textbox.contenu.strip() for textbox in textboxes)

    for exercise in page_data.contenu.exercices:
        session.add(Exercise(
            created_by=user,
            updated_by=user,
            project=textbook.project,
            textbook=textbook,
            textbook_page=page_data.textbookPage,
            number=exercise.num.contenu,
            instructions=text_from_textboxes_list(exercise.consigne),
            wording=text_from_textboxes_list(exercise.enonce),
            example=text_from_textboxes_list(exercise.exemple),
            clue=text_from_textboxes_list(exercise.conseil),
        ))


class ImportTestCase(TransactionTestCase):
    def test(self):
        self.expect_commit()

        textbook_id = self.create_model(Textbook, title="CE2 Français Hachette", project=self.create_model(Project, title="CE2 Français Hachette", description="")).id

        with open("../pdf-examples/manual_CE2_FRANCAIS_HACHETTE.p13.json", "r") as f:
            page_data = PageData(**json.load(f))

        with self.make_session() as session:
            textbook = session.get(Textbook, textbook_id)
            user = session.get(User, self.user_for_create.id)
            import_page(session, user, textbook, page_data)
            session.commit()

        self.assertEqual(self.count_models(Exercise), 2)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.textbook_id, textbook_id)
        self.assertEqual(exercise.textbook_page, 13)
        self.assertEqual(exercise.number, "6")
        self.assertEqual(exercise.instructions, "Recopie uniquement les phrases qui ont un sens.")
        self.assertEqual(exercise.wording, textwrap.dedent("""\
            a. Mon nom est Fripouille.
            b. Monstre sous lit
            c. J'ai une grande famille.
            d. Mes amis sont invisibles.
            e. Je avec Marie souevnt joue"""))
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")

        exercise = self.get_model(Exercise, 2)
        self.assertEqual(exercise.textbook_id, textbook_id)
        self.assertEqual(exercise.textbook_page, 13)
        self.assertEqual(exercise.number, "7")
        self.assertEqual(exercise.instructions, "Recopie uniquement les phrases correctement écrites.")
        self.assertEqual(exercise.wording, textwrap.dedent("""\
            a. Elle n'aime pas la glace au chocolat.
            b. J'arrive dans cinq minutes !
            c. Quand viendras-tu nous voir?
            d. Je l'ai appelé mais il n'a pas répondu..."""))
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")
