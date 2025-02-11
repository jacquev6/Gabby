import datetime
import hashlib

import PyPDF2

from . import adaptation
from . import api_models
from . import deltas
from . import database_utils
from . import renderable as r
from . import testing
from .api_models import Adaptation, PdfRectangle, Point
from .orm_models import Exercise
from .orm_models import PdfFile, PdfFileNaming, Section
from .orm_models import Ping
from .orm_models import Project, Textbook
from .orm_models import User, UserEmailAddress


def add(session, class_, **kwds):
    item = class_(**kwds)
    session.add(item)
    session.flush()
    return item


def create_admin_user_fixture(session):
    admin = User(
        username="admin",
        clear_text_password="password",
        created_by_id=1,
        updated_by_id=1,
    )
    session.add(admin)
    session.flush()
    assert admin.id == 1
    add(
        session,
        UserEmailAddress,
        user=admin,
        address="jacquev6+gabby-dev-admin@gmail.com",
    )
    return admin


def get_or_create_admin(session):
    admin = session.get(User, 1)
    if admin is None:
        admin = create_admin_user_fixture(session)
    return admin


def create_test_users_fixture(session):
    admin = get_or_create_admin(session)
    # @todo Understand why using the relationships instead of the ids results in a not-null violation
    alice = add(
        session,
        User,
        username="alice",
        clear_text_password="alice-password",
        created_by_id=admin.id,
        updated_by_id=admin.id,
    )
    add(
        session,
        UserEmailAddress,
        user=alice,
        address="jacquev6+gabby-dev-alice@gmail.com",
    )
    bob = add(
        session,
        User,
        username=None,
        clear_text_password="bob-password",
        created_by_id=admin.id,
        updated_by_id=admin.id,
    )
    add(
        session,
        UserEmailAddress,
        user=bob,
        address="jacquev6+gabby-dev-bob-1@gmail.com",
    )
    add(
        session,
        UserEmailAddress,
        user=bob,
        address="jacquev6+gabby-dev-bob-2@gmail.com",
    )
    charles = add(
        session,
        User,
        username=None,
        clear_text_password="charles-password",
        created_by_id=admin.id,
        updated_by_id=admin.id,
    )
    add(
        session,
        UserEmailAddress,
        user=charles,
        address="jacquev6+gabby-dev-charles@gmail.com",
    )


def create_test_pings_fixture(session):
    add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc),
        message="Hello 1",
    )
    ping2 = add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc),
        message="Hello 2",
    )
    ping3 = add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc),
        prev=ping2,
        message="Hello 3",
    )
    add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc),
        prev=ping3,
        message="Hello 4",
    )
    ping5 = add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc),
        prev=ping3,
        message="Hello 5",
    )
    add(
        session,
        Ping,
        created_at=datetime.datetime(2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc),
        prev=ping5,
        message="Hello 6",
    )


def create_empty_project_fixture(session):
    admin = get_or_create_admin(session)
    add(
        session,
        Project,
        title="Test project",
        description="This is a test project, created empty in a fixture.",
        created_by=admin,
        updated_by=admin,
    )


def create_test_exercises_fixture(session):
    admin = get_or_create_admin(session)
    create_test_exercises_1(session, admin)


def create_test_exercises_1(session, admin):
    pdffile1 = add(
        session,
        PdfFile,
        bytes_count=484714,
        pages_count=2,
        sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
        created_by=admin,
    )
    add(session, PdfFileNaming, pdf_file=pdffile1, name="test.pdf", created_by=admin)
    project1 = add(
        session,
        Project,
        title="Premier projet de test",
        description="Ce projet contient des exercices d'un seul manuel.",
        created_by=admin,
        updated_by=admin,
    )
    project2 = add(
        session,
        Project,
        title="Deuxième projet de test",
        description="Ce projet contient des exercices originaux.",
        created_by=admin,
        updated_by=admin,
    )
    textbook1 = add(
        session,
        Textbook,
        project=project1,
        title="Français CE2",
        publisher="Slabeuf",
        year=2021,
        isbn="1234567890123",
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Section,
        textbook=textbook1,
        pdf_file=pdffile1,
        textbook_start_page=6,
        pdf_file_start_page=1,
        pages_count=2,
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=6,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=1,
                coordinates="pdfjs",
                start=Point(x=321.7851195562453, y=298.5614176476993),
                stop=Point(x=563.0859853571111, y=165.01653324025676),
                text=None,
                role="bounding",
            )
        ],
        number="3",
        instructions=[
            deltas.InsertOp(insert="Complète avec : ", attributes={}),
            deltas.InsertOp(
                insert="le, une, un, des, tu, elles, ils",
                attributes={
                    "choices2": {
                        "start": "",
                        "separator1": ",",
                        "separator2": "",
                        "stop": "",
                        "placeholder": "...",
                    }
                },
            ),
            deltas.InsertOp(insert=".\r\nPuis, souligne les verbes.\n", attributes={}),
        ],
        example=deltas.empty,
        clue=[deltas.InsertOp(insert="Il peut y avoir plusieurs solutions.\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="... vide\r\n... vident\r\n... dépenses\r\n... dépensent\r\n... savon\r\n... savons\r\n... commande\n",
                attributes={},
            )
        ],
        adaptation=Adaptation(
            kind="multiple-choices",
            wording_paragraphs_per_pagelet=3,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text=None,
            items=None,
            items_are_selectable=None,
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=6,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=1,
                coordinates="pdfjs",
                start=Point(x=321.7851195562453, y=165.93753244306663),
                stop=Point(x=565.8489723700982, y=59.10162491711276),
                text=None,
                role="bounding",
            )
        ],
        number="4",
        instructions=[
            deltas.InsertOp(
                insert="Écris une phrase en respectant l'ordre des classes grammaticales indiquées.\n",
                attributes={},
            )
        ],
        example=[
            deltas.InsertOp(
                insert="pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.\n",
                attributes={},
            )
        ],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="nom propre / verbe / déterminant / adjectif / nom commun\n",
                attributes={},
            )
        ],
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=7,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=313.4961585172843, y=790.3749919482118),
                stop=Point(x=537.2981065692323, y=689.0650796391174),
                text=None,
                role="bounding",
            )
        ],
        number="9",
        instructions=[
            deltas.InsertOp(
                insert="Recopie l’intrus qui se cache dans chaque liste et écris sa classe.\n",
                attributes={},
            )
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="a. partons ◆ bidons ◆ allons ◆ vendons\r\nb. vidons ◆ mentons ◆ ballons ◆ salons\r\nc. voir ◆ armoire ◆ couloir ◆ dortoir\n",
                attributes={},
            )
        ],
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project2,
        textbook=None,
        textbook_page=None,
        number="L1",
        instructions=[deltas.InsertOp(insert="Faire des choses intelligentes.\n", attributes={})],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="\n", attributes={})],
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project2,
        textbook=None,
        textbook_page=None,
        number="L2",
        instructions=[deltas.InsertOp(insert="Faire d'autres choses intelligentes.\n", attributes={})],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="\n", attributes={})],
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project2,
        textbook=None,
        textbook_page=None,
        number="L3",
        instructions=[
            deltas.InsertOp(
                insert="Prendre le temps de faire aussi des choses banales.\n",
                attributes={},
            )
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="\n", attributes={})],
        created_by=admin,
        updated_by=admin,
    )
    return (project1, textbook1)


def create_more_test_exercises_fixture(session):
    admin = get_or_create_admin(session)
    create_test_exercises_2(session, admin)


def create_test_exercises_2(session, admin):
    (project1, textbook1) = create_test_exercises_1(session, admin)
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=7,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=57.45936198048777, y=508.54923588836755),
                stop=Point(x=303.3652061363319, y=311.45540648703854),
                text=None,
                role="bounding",
            ),
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=41.81553087016726, y=512.8599582877939),
                stop=Point(x=299.93876428559844, y=444.8714829639081),
                text="7\nRelève dans le texte trois\ndéterminants, un nom propre, quatre\nnoms communs et trois verbes.",
                role="instructions",
            ),
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=51.03421777786123, y=465.61372967289014),
                stop=Point(x=308.00511532983063, y=340.0079023796095),
                text="Les Touaregs sont des Berbères, un peuple\nqui habite en Afrique du Nord depuis la\npréhistoire. Ils vivent dans le désert du Sahara\n(Algérie, Libye, Mali, Niger, Burkina Faso…). En\nété, les températures y montent à plus de 50 °C\net elles descendent en dessous de zéro durant\nles nuits d’hiver.",
                role="wording",
            ),
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=112.37332314140376, y=352.2926939550555),
                stop=Point(x=304.6623309473473, y=312.1753253726276),
                text="Mon quotidien, pour les 10-14 ans, www.monquotidien.fr, 13 septembre 2014.\n",
                role="textReference",
            ),
        ],
        number="7",
        instructions=[
            deltas.InsertOp(insert="Relève dans le texte trois\n", attributes={}),
            deltas.InsertOp(insert="déterminants", attributes={"sel": 1}),
            deltas.InsertOp(insert=", un ", attributes={}),
            deltas.InsertOp(insert="nom propre", attributes={"sel": 2}),
            deltas.InsertOp(insert=", quatre\n", attributes={}),
            deltas.InsertOp(insert="noms communs", attributes={"sel": 3}),
            deltas.InsertOp(insert=" et trois ", attributes={}),
            deltas.InsertOp(insert="verbes", attributes={"sel": 4}),
            deltas.InsertOp(insert=".\n", attributes={}),
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="Les Touaregs sont des Berbères, un peuple qui habite en Afrique du Nord depuis la préhistoire.\nIls vivent dans le désert du Sahara (Algérie, Libye, Mali, Niger, Burkina Faso…).\nEn été, les températures y montent à plus de 50 °C et elles descendent en dessous de zéro durant les nuits d’hiver.\n",
                attributes={},
            )
        ],
        text_reference=[
            deltas.InsertOp(
                insert="Mon quotidien, pour les 10-14 ans, www.monquotidien.fr, 13 septembre 2014.\n",
                attributes={},
            ),
        ],
        adaptation=Adaptation(
            kind="generic",
            wording_paragraphs_per_pagelet=3,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text=None,
            items=api_models.TokensItems(
                kind="tokens",
                words=True,
                punctuation=True,
            ),
            items_are_selectable=api_models.Selectable(
                colors=["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"],
            ),
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=7,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=317.18014120126696, y=538.0212103782859),
                stop=Point(x=556.6390156601415, y=462.4992757478701),
                text=None,
                role="bounding",
            ),
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=312.61445878367766, y=537.0592461149397),
                stop=Point(x=556.9096618375679, y=493.27005861819964),
                text="11\nAjoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.",
                role="instructions",
            ),
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=314.9191305106011, y=503.64118197269073),
                stop=Point(x=555.7573259741062, y=452.9379122396233),
                text="nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …",
                role="wording",
            ),
        ],
        number="11",
        instructions=[
            deltas.InsertOp(
                insert="Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.\n",
                attributes={},
            )
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …\n",
                attributes={},
            )
        ],
        adaptation=Adaptation(
            kind="fill-with-free-text",
            wording_paragraphs_per_pagelet=None,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text="…",
            items=None,
            items_are_selectable=None,
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=7,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=60.0, y=180.0),
                stop=Point(x=250.0, y=320.0),
                text=None,
                role="bounding",
            )
        ],
        number="8",
        instructions=[
            deltas.InsertOp(insert="Réponds par ", attributes={}),
            deltas.InsertOp(
                insert="vrai ou faux",
                attributes={
                    "choices2": {
                        "start": "",
                        "separator1": "ou",
                        "separator2": "",
                        "stop": "",
                        "placeholder": "@",
                    },
                },
            ),
            deltas.InsertOp(insert=".\n", attributes={}),
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="a. coccinelle est un adjectif. @\nb. bûche est un verbe. @\nc. cette est un déterminant. @\nd. dentier est un verbe. @\ne. respirer est un verbe. @\nf. aspiration est un nom. @\n",
                attributes={},
            )
        ],
        adaptation=Adaptation(
            kind="multiple-choices",
            wording_paragraphs_per_pagelet=3,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text=None,
            items=None,
            items_are_selectable=None,
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )
    return (project1, textbook1)


def create_even_more_test_exercises_fixture(session):
    admin = get_or_create_admin(session)
    create_test_exercises_3(session, admin)


def create_test_exercises_3(session, admin):
    (project1, textbook1) = create_test_exercises_2(session, admin)
    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=7,
        rectangles=[
            PdfRectangle(
                pdf_sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c",
                pdf_page=2,
                coordinates="pdfjs",
                start=Point(x=57.45936198048777, y=508.54923588836755),
                stop=Point(x=303.3652061363319, y=311.45540648703854),
                text=None,
                role="bounding",
            )
        ],
        number="7b",
        instructions=[
            deltas.InsertOp(insert="Relève dans le texte trois\n", attributes={}),
            deltas.InsertOp(insert="déterminants", attributes={"sel": 1}),
            deltas.InsertOp(insert=", un ", attributes={}),
            deltas.InsertOp(insert="nom propre", attributes={"sel": 2}),
            deltas.InsertOp(insert=", quatre\n", attributes={}),
            deltas.InsertOp(insert="noms communs", attributes={"sel": 3}),
            deltas.InsertOp(insert=" et trois ", attributes={}),
            deltas.InsertOp(insert="verbes", attributes={"sel": 4}),
            deltas.InsertOp(insert=".\n", attributes={}),
        ],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(
                insert="Les Touaregs sont des Berbères, un peuple qui habite en Afrique du Nord depuis la préhistoire.\nIls vivent dans le désert du Sahara (Algérie, Libye, Mali, Niger, Burkina Faso…).\nEn été, les températures y montent à plus de 50 °C et elles descendent en dessous de zéro durant les nuits d’hiver.\n",
                attributes={},
            )
        ],
        adaptation=Adaptation(
            kind="generic",
            wording_paragraphs_per_pagelet=1,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text=None,
            items=api_models.TokensItems(kind="tokens", words=True, punctuation=False),
            items_are_selectable=api_models.Selectable(
                colors=["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"]
            ),
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )

    add(
        session,
        Exercise,
        project=project1,
        textbook=textbook1,
        textbook_page=5,
        number="1",
        instructions=[deltas.InsertOp(insert="...\n", attributes={})],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[
            deltas.InsertOp(insert="a. ", attributes={}),
            deltas.InsertOp(insert="Aujourd'hui", attributes={"bold": True}),
            deltas.InsertOp(insert=" il fait ", attributes={}),
            deltas.InsertOp(insert="gris", attributes={"italic": True}),
            deltas.InsertOp(insert=" et (il pleuvra / il pleut / il pleuvait).\nb. ", attributes={}),
            deltas.InsertOp(insert="Aujourd'hui", attributes={"bold": True}),
            deltas.InsertOp(insert=" il fait ", attributes={}),
            deltas.InsertOp(insert="gris", attributes={"italic": True}),
            deltas.InsertOp(insert=" et ", attributes={}),
            deltas.InsertOp(
                insert="(il pleuvra / il pleut / il pleuvait)",
                attributes={
                    "choices2": {
                        "start": "(",
                        "separator1": "/",
                        "separator2": "",
                        "stop": ")",
                        "placeholder": "",
                    }
                },
            ),
            deltas.InsertOp(insert=".\nc. Aujourd'hui il fait @1 et il @2. ", attributes={}),
            deltas.InsertOp(
                insert="(gris / beau)",
                attributes={
                    "choices2": {
                        "start": "(",
                        "separator1": "/",
                        "separator2": "",
                        "stop": ")",
                        "placeholder": "@1",
                    }
                },
            ),
            deltas.InsertOp(insert=" ", attributes={}),
            deltas.InsertOp(
                insert="[pleut * pleuvra]",
                attributes={
                    "choices2": {
                        "start": "[",
                        "separator1": "*",
                        "separator2": "",
                        "stop": "]",
                        "placeholder": "@2",
                    }
                },
            ),
            deltas.InsertOp(insert="\n\n", attributes={}),
        ],
        adaptation=Adaptation(
            kind="multiple-choices",
            wording_paragraphs_per_pagelet=3,
            single_item_per_paragraph=False,
            placeholder_for_fill_with_free_text=None,
            items=None,
            items_are_selectable=None,
            items_are_boxed=False,
            items_have_mcq_beside=False,
            items_have_mcq_below=False,
            items_have_predefined_mcq=api_models.PredefinedMcq(grammatical_gender=False, grammatical_number=False),
            show_arrow_before_mcq_fields=False,
            show_mcq_choices_by_default=False,
        ),
        created_by=admin,
        updated_by=admin,
    )


def create_empty_textbook(session, stem):
    demo_pdf_path = f"../pdf-examples/{stem}.pdf"
    with open(demo_pdf_path, "rb") as f:
        pdf_bytes = f.read()
        bytes_count = len(pdf_bytes)
        sha256 = hashlib.sha256(pdf_bytes).hexdigest()
    with open(demo_pdf_path, "rb") as f:
        pages_count = len(PyPDF2.PdfReader(f).pages)
    admin = get_or_create_admin(session)
    pdffile1 = add(
        session,
        PdfFile,
        bytes_count=bytes_count,
        pages_count=pages_count,
        sha256=sha256,
        created_by=admin,
    )
    add(session, PdfFileNaming, pdf_file=pdffile1, name=f"{stem}.pdf", created_by=admin)
    project1 = add(
        session,
        Project,
        title=f"{stem.capitalize()} project",
        description="",
        created_by=admin,
        updated_by=admin,
    )
    textbook1 = add(
        session,
        Textbook,
        project=project1,
        title=f"{stem.capitalize()} textbook",
        publisher="Gabby",
        year=2024,
        isbn="9783161484100",
        created_by=admin,
        updated_by=admin,
    )
    add(
        session,
        Section,
        textbook=textbook1,
        pdf_file=pdffile1,
        textbook_start_page=1,
        pdf_file_start_page=1,
        pages_count=pages_count,
        created_by=admin,
        updated_by=admin,
    )


available_fixtures = {
    "admin-user": create_admin_user_fixture,
    "test-users": create_test_users_fixture,
    "test-pings": create_test_pings_fixture,
    "empty-project": create_empty_project_fixture,
    "test-exercises": create_test_exercises_fixture,
    "more-test-exercises": create_more_test_exercises_fixture,
    "even-more-test-exercises": create_even_more_test_exercises_fixture,
    "empty-test-textbook": lambda session: create_empty_textbook(session, "test"),
    "empty-demo-textbook": lambda session: create_empty_textbook(session, "demo"),
    "empty-text-extraction-textbook": lambda session: create_empty_textbook(session, "text-extraction"),
}


def load(session, fixtures):
    database_utils.truncate_all_tables(session)
    for fixture in fixtures:
        available_fixtures[fixture](session)


class FixturesTestCase(testing.TransactionTestCase, adaptation.AdaptationTestCase):
    def test_load_all(self):
        for fixture in available_fixtures:
            with self.subTest(fixture=fixture):
                with self.make_session() as session:
                    load(session, [fixture])
                    session.rollback()
        self.expect_commits_rollbacks(0, len(available_fixtures))

    def test_adapt_exercise_01(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 1),
                r.Exercise(number='3', textbook_page=6, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Complète'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avec'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text=':'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='le')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='une')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='un')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='des')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='tu')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='elles')], boxed=True), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ou'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='ils')], boxed=True), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Puis'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='souligne'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='les'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbes'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='peut'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='y'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avoir'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='plusieurs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='solutions'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='vide')]), r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='vident')]), r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dépenses')])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Complète'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avec'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text=':'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='le')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='une')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='un')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='des')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='tu')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='elles')], boxed=True), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ou'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='ils')], boxed=True), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Puis'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='souligne'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='les'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbes'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='peut'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='y'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avoir'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='plusieurs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='solutions'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dépensent')]), r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='savon')]), r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='savons')])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Complète'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avec'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text=':'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='le')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='une')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='un')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='des')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='tu')], boxed=True), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='elles')], boxed=True), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ou'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='ils')], boxed=True), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Puis'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='souligne'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='les'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbes'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='peut'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='y'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='avoir'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='plusieurs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='solutions'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='le')], [r.Text(kind='text', text='une')], [r.Text(kind='text', text='un')], [r.Text(kind='text', text='des')], [r.Text(kind='text', text='tu')], [r.Text(kind='text', text='elles')], [r.Text(kind='text', text='ils')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='commande')])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_02(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 2),
                r.Exercise(number='4', textbook_page=6, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Écris'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='une'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='phrase'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='en'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='respectant'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='l'), r.Text(kind='text', text="'"), r.Text(kind='text', text='ordre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='des'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='classes'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='grammaticales'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='indiquées'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='pronom'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='personnel'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbe'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='déterminant'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='nom'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='commun'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text=':'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='Je'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='mange'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='une'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='pomme'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='nom'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='propre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbe'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='déterminant'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='adjectif'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='nom'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='commun')])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_03(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 3),
                r.Exercise(number='9', textbook_page=7, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Recopie'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='l'), r.Text(kind='text', text='’'), r.Text(kind='text', text='intrus'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='qui'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='se'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='cache'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dans'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='chaque'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='liste'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='écris'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='sa'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='classe'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='a'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='partons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='bidons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='allons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='vendons')]), r.Paragraph(contents=[r.Text(kind='text', text='b'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='vidons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='mentons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ballons'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='salons')]), r.Paragraph(contents=[r.Text(kind='text', text='c'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='voir'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='armoire'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='couloir'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dortoir')])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_04(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 4),
                r.Exercise(number='L1', textbook_page=None, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Faire'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='des'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='choses'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='intelligentes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_05(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 5),
                r.Exercise(number='L2', textbook_page=None, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Faire'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='d'), r.Text(kind='text', text="'"), r.Text(kind='text', text='autres'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='choses'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='intelligentes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_06(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 6),
                r.Exercise(number='L3', textbook_page=None, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Prendre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='temps'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='de'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='faire'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='aussi'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='des'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='choses'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='banales'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_07(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 7),
                r.Exercise(number='7', textbook_page=7, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Relève'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dans'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='texte'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffff00', text='déterminants'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffc0cb', text='nom propre'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='quatre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbbbff', text='noms communs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbffbb', text='verbes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Touaregs')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='sont')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='des')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Berbères')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='un')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='peuple')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='qui')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='habite')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='en')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Afrique')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='du')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Nord')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='depuis')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='la')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='préhistoire')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='.')])]), r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Ils')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='vivent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='dans')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='le')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='désert')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='du')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Sahara')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='(')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Algérie')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Libye')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Mali')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Niger')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Burkina')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Faso')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='…')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=')')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='.')])]), r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='En')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='été')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text=',')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='températures')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='y')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='montent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='à')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='plus')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='de')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='50')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='°')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='C')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='et')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='elles')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='descendent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='en')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='dessous')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='de')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='zéro')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='durant')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='nuits')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='d')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='’')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='hiver')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='.')])])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Mon'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='quotidien'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='pour'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='les'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='10'), r.Text(kind='text', text='-'), r.Text(kind='text', text='14'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ans'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='www'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='monquotidien'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='fr'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='13'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='septembre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='2014'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_08(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 8),
                r.Exercise(number='11', textbook_page=7, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Ajoute'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='suffixe'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='–'), r.Text(kind='text', text='eur'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='aux'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbes'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='Indique'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='la'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='classe'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='des'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='mots'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='fabriqués'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='nager'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='➞'), r.Whitespace(kind='whitespace'), r.FreeTextInput(kind='freeTextInput'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='tracter'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='➞'), r.Whitespace(kind='whitespace'), r.FreeTextInput(kind='freeTextInput'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='manger'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='➞'), r.Whitespace(kind='whitespace'), r.FreeTextInput(kind='freeTextInput'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆')]), r.Paragraph(contents=[r.Text(kind='text', text='inventer'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='➞'), r.Whitespace(kind='whitespace'), r.FreeTextInput(kind='freeTextInput'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='◆'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='livrer'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='➞'), r.Whitespace(kind='whitespace'), r.FreeTextInput(kind='freeTextInput')])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_09(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 9),
                r.Exercise(number='8', textbook_page=7, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Réponds'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='par'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='vrai')], boxed=True), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ou'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='faux')], boxed=True), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='a'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='coccinelle'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='adjectif'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)]), r.Paragraph(contents=[r.Text(kind='text', text='b'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='bûche'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbe'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)]), r.Paragraph(contents=[r.Text(kind='text', text='c'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='cette'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='déterminant'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Réponds'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='par'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='vrai')], boxed=True), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='ou'), r.Whitespace(kind='whitespace'), r.PassiveSequence(kind='passiveSequence', contents=[r.Text(kind='text', text='faux')], boxed=True), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='d'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dentier'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbe'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)]), r.Paragraph(contents=[r.Text(kind='text', text='e'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='respirer'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='verbe'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)]), r.Paragraph(contents=[r.Text(kind='text', text='f'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='aspiration'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='est'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='nom'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='vrai')], [r.Text(kind='text', text='faux')]], show_choices_by_default=False)])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_10(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 10),
                r.Exercise(number='7b', textbook_page=7, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Relève'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dans'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='texte'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffff00', text='déterminants'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffc0cb', text='nom propre'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='quatre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbbbff', text='noms communs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbffbb', text='verbes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Touaregs')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='sont')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='des')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Berbères')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='un')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='peuple')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='qui')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='habite')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='en')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Afrique')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='du')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Nord')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='depuis')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='la')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='préhistoire')]), r.Text(kind='text', text='.')])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Relève'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dans'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='texte'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffff00', text='déterminants'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffc0cb', text='nom propre'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='quatre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbbbff', text='noms communs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbffbb', text='verbes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Ils')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='vivent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='dans')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='le')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='désert')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='du')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Sahara')]), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='('), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Algérie')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Libye')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Mali')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Niger')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Burkina')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='Faso')]), r.Text(kind='text', text='…'), r.Text(kind='text', text=')'), r.Text(kind='text', text='.')])])), r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='Relève'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='dans'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='le'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='texte'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffff00', text='déterminants'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='un'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#ffc0cb', text='nom propre'), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='quatre'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbbbff', text='noms communs'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='trois'), r.Whitespace(kind='whitespace'), r.Text(kind='text', highlighted='#bbffbb', text='verbes'), r.Text(kind='text', text='.')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='En')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='été')]), r.Text(kind='text', text=','), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='températures')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='y')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='montent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='à')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='plus')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='de')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='50')]), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='°'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='C')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='et')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='elles')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='descendent')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='en')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='dessous')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='de')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='zéro')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='durant')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='les')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='nuits')]), r.Whitespace(kind='whitespace'), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='d'), r.Text(kind='text', text='’')]), r.SelectableInput(kind='selectableInput', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], contents=[r.Text(kind='text', text='hiver')]), r.Text(kind='text', text='.')])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_11(self):
        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 11),
                r.Exercise(number='1', textbook_page=5, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='...')])]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind='text', text='a'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', bold=True, text="Aujourd'hui"), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='fait'), r.Whitespace(kind='whitespace'), r.Text(kind='text', italic=True, text='gris'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='('), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='pleuvra'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='pleut'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='/'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='pleuvait'), r.Text(kind='text', text=')'), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='b'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', bold=True, text="Aujourd'hui"), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='fait'), r.Whitespace(kind='whitespace'), r.Text(kind='text', italic=True, text='gris'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='il pleuvra')], [r.Text(kind='text', text='il pleut')], [r.Text(kind='text', text='il pleuvait')]], show_choices_by_default=False), r.Text(kind='text', text='.')]), r.Paragraph(contents=[r.Text(kind='text', text='c'), r.Text(kind='text', text='.'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='Aujourd'), r.Text(kind='text', text="'"), r.Text(kind='text', text='hui'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='fait'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='gris')], [r.Text(kind='text', text='beau')]], show_choices_by_default=False), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='et'), r.Whitespace(kind='whitespace'), r.Text(kind='text', text='il'), r.Whitespace(kind='whitespace'), r.MultipleChoicesInput(kind='multipleChoicesInput', choices=[[r.Text(kind='text', text='pleut')], [r.Text(kind='text', text='pleuvra')]], show_choices_by_default=False), r.Text(kind='text', text='.')])]))]),
            )
            session.rollback()
            self.expect_rollback()
