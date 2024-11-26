import datetime
import hashlib

import PyPDF2

from . import adaptation
from . import api_models
from . import deltas
from . import database_utils
from . import renderable as r
from . import testing
from .api_models import AdaptationV2, PdfRectangle, Point
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
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc
        ),
        message="Hello 1",
    )
    ping2 = add(
        session,
        Ping,
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc
        ),
        message="Hello 2",
    )
    ping3 = add(
        session,
        Ping,
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc
        ),
        prev=ping2,
        message="Hello 3",
    )
    add(
        session,
        Ping,
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc
        ),
        prev=ping3,
        message="Hello 4",
    )
    ping5 = add(
        session,
        Ping,
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc
        ),
        prev=ping3,
        message="Hello 5",
    )
    add(
        session,
        Ping,
        created_at=datetime.datetime(
            2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc
        ),
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
            deltas.InsertOp(insert="le, une, un, des, tu, elles, ils", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": "..."}}),
            deltas.InsertOp(insert=".\r\nPuis, souligne les verbes.\n", attributes={}),
        ],
        example=deltas.empty,
        clue=[deltas.InsertOp(insert="Il peut y avoir plusieurs solutions.\n", attributes={})],
        wording=[deltas.InsertOp(insert="... vide\r\n... vident\r\n... dépenses\r\n... dépensent\r\n... savon\r\n... savons\r\n... commande\n", attributes={})],
        adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
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
        instructions=[deltas.InsertOp(insert="Écris une phrase en respectant l'ordre des classes grammaticales indiquées.\n", attributes={})],
        example=[deltas.InsertOp(insert="pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="nom propre / verbe / déterminant / adjectif / nom commun\n", attributes={})],
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
        instructions=[deltas.InsertOp(insert="Recopie l’intrus qui se cache dans chaque liste et écris sa classe.\n", attributes={})],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="a. partons ◆ bidons ◆ allons ◆ vendons\r\nb. vidons ◆ mentons ◆ ballons ◆ salons\r\nc. voir ◆ armoire ◆ couloir ◆ dortoir\n", attributes={})],
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
        instructions=[deltas.InsertOp(insert="Prendre le temps de faire aussi des choses banales.\n", attributes={})],
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
        wording=[deltas.InsertOp(insert="Les Touaregs sont des Berbères, un peuple qui habite en Afrique du Nord depuis la préhistoire.\nIls vivent dans le désert du Sahara (Algérie, Libye, Mali, Niger, Burkina Faso…).\nEn été, les températures y montent à plus de 50 °C et elles descendent en dessous de zéro durant les nuits d’hiver.\n", attributes={})],
        adaptation=AdaptationV2(
            kind="generic",
            effects=[api_models.ItemizedAdaptationEffect(
                kind="itemized",
                items=api_models.ItemizedAdaptationEffect.WordsItems(
                    kind="words", punctuation=True,
                ),
                effects=api_models.ItemizedAdaptationEffect.Effects(
                    selectable=api_models.ItemizedAdaptationEffect.Effects.Selectable(
                        colors=["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"],
                    ),
                    boxed=False,
                ),
            )],
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
        instructions=[deltas.InsertOp(insert="Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.\n", attributes={})],
        example=[deltas.InsertOp(insert="\n", attributes={})],
        clue=[deltas.InsertOp(insert="\n", attributes={})],
        wording=[deltas.InsertOp(insert="nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …\n", attributes={})],
        adaptation=AdaptationV2(
            kind="fill-with-free-text",
            effects=[api_models.FillWithFreeTextAdaptationEffect(
                kind="fill-with-free-text", placeholder="…"
            )],
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
        wording=[deltas.InsertOp(insert="a. coccinelle est un adjectif. @\nb. bûche est un verbe. @\nc. cette est un déterminant. @\nd. dentier est un verbe. @\ne. respirer est un verbe. @\nf. aspiration est un nom. @\n", attributes={})],
        adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
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
        wording=[deltas.InsertOp(insert="Les Touaregs sont des Berbères, un peuple qui habite en Afrique du Nord depuis la préhistoire.\nIls vivent dans le désert du Sahara (Algérie, Libye, Mali, Niger, Burkina Faso…).\nEn été, les températures y montent à plus de 50 °C et elles descendent en dessous de zéro durant les nuits d’hiver.\n", attributes={})],
        wording_paragraphs_per_pagelet=1,
        adaptation=AdaptationV2(
            kind="generic",
            effects=[api_models.ItemizedAdaptationEffect(
                kind="itemized",
                items=api_models.ItemizedAdaptationEffect.WordsItems(
                    kind="words", punctuation=False
                ),
                effects=api_models.ItemizedAdaptationEffect.Effects(
                    selectable=api_models.ItemizedAdaptationEffect.Effects.Selectable(
                        colors=["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"]
                    ),
                    boxed=False,
                ),
            )],
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
        wording_paragraphs_per_pagelet=3,
        adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
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

    def test_adapt_exercise_1(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _BoxedText, _MultipleChoicesInput

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 1),
                r.Exercise(number='3', textbook_page=6, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Complète'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avec'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=':'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='une'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='tu'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='elles'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='ils'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Puis'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='souligne'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='les'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbes'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='peut'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='y'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avoir'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='plusieurs'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='solutions'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='vide')])]), Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='vident')])]), Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dépenses')])])])), Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Complète'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avec'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=':'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='une'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='tu'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='elles'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='ils'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Puis'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='souligne'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='les'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbes'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='peut'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='y'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avoir'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='plusieurs'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='solutions'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dépensent')])]), Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='savon')])]), Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='savons')])])])), Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Complète'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avec'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=':'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='une'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='tu'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='elles'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='ils'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Puis'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='souligne'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='les'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbes'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='peut'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='y'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='avoir'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='plusieurs'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='solutions'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_MultipleChoicesInput(type='multipleChoicesInput', choices=['le', 'une', 'un', 'des', 'tu', 'elles', 'ils']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='commande')])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_2(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 2),
                r.Exercise(number='4', textbook_page=6, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Écris'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='une'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='phrase'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='en'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='respectant'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='l'), _PlainText(type='plainText', text="'"), _PlainText(type='plainText', text='ordre'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='classes'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='grammaticales'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='indiquées'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='pronom'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='personnel'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbe'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='déterminant'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='nom'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='commun'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text=':'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='Je'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='mange'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='une'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='pomme'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='nom'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='propre'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbe'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='déterminant'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='adjectif'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='nom'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='commun')])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_3(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 3),
                r.Exercise(number='9', textbook_page=7, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Recopie'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='l'), _PlainText(type='plainText', text='’'), _PlainText(type='plainText', text='intrus'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='qui'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='se'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='cache'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dans'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='chaque'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='liste'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='écris'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='sa'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='classe'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='a'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='partons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='bidons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='allons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='vendons')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='b'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='vidons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='mentons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='ballons'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='salons')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='c'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='voir'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='armoire'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='couloir'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dortoir')])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_4(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 4),
                r.Exercise(number='L1', textbook_page=None, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Faire'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='choses'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='intelligentes'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_5(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 5),
                r.Exercise(number='L2', textbook_page=None, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Faire'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='d'), _PlainText(type='plainText', text="'"), _PlainText(type='plainText', text='autres'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='choses'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='intelligentes'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_6(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 6),
                r.Exercise(number='L3', textbook_page=None, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Prendre'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='temps'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='de'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='faire'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='aussi'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='choses'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='banales'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_7(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _SelectedText, _SelectableText

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 7),
                r.Exercise(number='7', textbook_page=7, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Relève'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dans'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='texte'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='déterminants', color='#ffff00'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='nom propre', color='#ffc0cb'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='quatre'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='noms communs', color='#bbbbff'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='verbes', color='#bbffbb'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='Les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Touaregs', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='sont', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='des', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Berbères', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='un', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='peuple', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='qui', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='habite', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='en', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Afrique', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='du', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Nord', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='depuis', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='la', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='préhistoire', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='.', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False)])]), Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='Ils', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='vivent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='dans', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='le', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='désert', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='du', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Sahara', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='(', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='Algérie', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Libye', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Mali', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Niger', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Burkina', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Faso', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='…', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=')', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='.', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False)])]), Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='En', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='été', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text=',', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='températures', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='y', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='montent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='à', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='plus', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='de', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='50', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='°', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='C', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='et', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='elles', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='descendent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='en', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='dessous', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='de', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='zéro', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='durant', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='nuits', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='d', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='’', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='hiver', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _SelectableText(type='selectableText', text='.', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False)])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_8(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _FreeTextInput

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 8),
                r.Exercise(number='11', textbook_page=7, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Ajoute'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='suffixe'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='–'), _PlainText(type='plainText', text='eur'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='aux'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbes'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Indique'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='la'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='classe'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='des'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='mots'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='fabriqués'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='nager'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='➞'), _Whitespace(type='whitespace'), _FreeTextInput(type='freeTextInput'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='tracter'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='➞'), _Whitespace(type='whitespace'), _FreeTextInput(type='freeTextInput'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='manger'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='➞'), _Whitespace(type='whitespace'), _FreeTextInput(type='freeTextInput'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='inventer'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='➞'), _Whitespace(type='whitespace'), _FreeTextInput(type='freeTextInput'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='◆'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='livrer'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='➞'), _Whitespace(type='whitespace'), _FreeTextInput(type='freeTextInput')])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_9(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _BoxedText, _MultipleChoicesInput

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 9),
                r.Exercise(number='8', textbook_page=7, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Réponds'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='par'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='vrai'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='ou'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='faux'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='a'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='coccinelle'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='adjectif'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='b'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='bûche'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbe'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='c'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='cette'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='déterminant'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])])])), Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Réponds'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='par'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='vrai'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='ou'), _Whitespace(type='whitespace'), _BoxedText(type='boxedText', text='faux'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='d'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dentier'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbe'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='e'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='respirer'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='verbe'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='f'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='aspiration'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='est'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='nom'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['vrai', 'faux'])])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_10(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _SelectedText, _SelectableText

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 10),
                r.Exercise(number='7b', textbook_page=7, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Relève'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dans'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='texte'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='déterminants', color='#ffff00'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='nom propre', color='#ffc0cb'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='quatre'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='noms communs', color='#bbbbff'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='verbes', color='#bbffbb'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='Les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Touaregs', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='sont', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='des', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Berbères', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='un', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='peuple', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='qui', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='habite', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='en', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Afrique', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='du', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Nord', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='depuis', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='la', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='préhistoire', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text='.')])])])), Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Relève'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dans'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='texte'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='déterminants', color='#ffff00'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='nom propre', color='#ffc0cb'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='quatre'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='noms communs', color='#bbbbff'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='verbes', color='#bbffbb'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='Ils', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='vivent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='dans', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='le', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='désert', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='du', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Sahara', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='('), _SelectableText(type='selectableText', text='Algérie', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Libye', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Mali', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Niger', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Burkina', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='Faso', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text='…'), _PlainText(type='plainText', text=')'), _PlainText(type='plainText', text='.')])])])), Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='Relève'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='dans'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='le'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='texte'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='déterminants', color='#ffff00'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='un'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='nom propre', color='#ffc0cb'), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='quatre'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='noms communs', color='#bbbbff'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='trois'), _Whitespace(type='whitespace'), _SelectedText(type='selectedText', text='verbes', color='#bbffbb'), _PlainText(type='plainText', text='.')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_SelectableText(type='selectableText', text='En', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='été', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text=','), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='températures', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='y', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='montent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='à', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='plus', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='de', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='50', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='°'), _SelectableText(type='selectableText', text='C', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='et', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='elles', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='descendent', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='en', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='dessous', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='de', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='zéro', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='durant', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='les', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='nuits', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _Whitespace(type='whitespace'), _SelectableText(type='selectableText', text='d', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text='’'), _SelectableText(type='selectableText', text='hiver', colors=['#ffff00', '#ffc0cb', '#bbbbff', '#bbffbb'], boxed=False), _PlainText(type='plainText', text='.')])])]))]),
            )
            session.rollback()
            self.expect_rollback()

    def test_adapt_exercise_11(self):
        from .renderable import Pagelet, Section, Paragraph, Sentence, _PlainText, _Whitespace, _MultipleChoicesInput, _BoldText, _ItalicText

        with self.make_session() as session:
            load(session, ["even-more-test-exercises"])

            self.do_test(
                session.get(Exercise, 11),
                r.Exercise(number='1', textbook_page=5, pagelets=[Pagelet(instructions=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='...')])])]), wording=Section(paragraphs=[Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='a'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _BoldText(type='boldText', text="Aujourd'hui"), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='fait'), _Whitespace(type='whitespace'), _ItalicText(type='italicText', text='gris'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='('), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='pleuvra'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='pleut'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='/'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='pleuvait'), _PlainText(type='plainText', text=')'), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='b'), _PlainText(type='plainText', text='.')]), Sentence(tokens=[_BoldText(type='boldText', text="Aujourd'hui"), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='fait'), _Whitespace(type='whitespace'), _ItalicText(type='italicText', text='gris'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['il pleuvra', 'il pleut', 'il pleuvait']), _PlainText(type='plainText', text='.')])]), Paragraph(sentences=[Sentence(tokens=[_PlainText(type='plainText', text='c'), _PlainText(type='plainText', text='.'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='Aujourd'), _PlainText(type='plainText', text="'"), _PlainText(type='plainText', text='hui'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='fait'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['gris', 'beau']), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='et'), _Whitespace(type='whitespace'), _PlainText(type='plainText', text='il'), _Whitespace(type='whitespace'), _MultipleChoicesInput(type='multipleChoicesInput', choices=['pleut', 'pleuvra']), _PlainText(type='plainText', text='.')])])]))]),
            )
            session.rollback()
            self.expect_rollback()
