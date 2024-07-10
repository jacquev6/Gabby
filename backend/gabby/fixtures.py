import datetime
import json

from . import database_utils
from . import import_from_visio_method
from .orm_models import Exercise, ExtractionEvent
from .orm_models import FillWithFreeTextAdaptation, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInWordingAdaptation, SelectThingsAdaptation
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
    admin = User(username="admin", clear_text_password="password", created_by_id=1, updated_by_id=1)
    session.add(admin)
    session.flush()
    assert admin.id == 1
    add(session, UserEmailAddress, user=admin, address="jacquev6+gabby-dev-admin@gmail.com")
    return admin


def get_or_create_admin(session):
    admin = session.query(User).get(1)
    if admin is None:
        admin = create_admin_user_fixture(session)
    return admin


def create_test_users_fixture(session):
    admin = get_or_create_admin(session)
    # @todo Understand why using the relationships instead of the ids results in a not-null violation
    alice = add(session, User, username="alice", clear_text_password="alice-password", created_by_id=admin.id, updated_by_id=admin.id)
    add(session, UserEmailAddress, user=alice, address="jacquev6+gabby-dev-alice@gmail.com")
    bob = add(session, User, username=None, clear_text_password="bob-password", created_by_id=admin.id, updated_by_id=admin.id)
    add(session, UserEmailAddress, user=bob, address="jacquev6+gabby-dev-bob-1@gmail.com")
    add(session, UserEmailAddress, user=bob, address="jacquev6+gabby-dev-bob-2@gmail.com")
    charles = add(session, User, username=None, clear_text_password="charles-password", created_by_id=admin.id, updated_by_id=admin.id)
    add(session, UserEmailAddress, user=charles, address="jacquev6+gabby-dev-charles@gmail.com")


def create_test_pings_fixture(session):
    ping1 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 15, tzinfo=datetime.timezone.utc), message='Hello 1')
    ping2 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 16, tzinfo=datetime.timezone.utc), message='Hello 2')
    ping3 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 17, tzinfo=datetime.timezone.utc), prev=ping2, message='Hello 3')
    ping4 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 18, tzinfo=datetime.timezone.utc), prev=ping3, message='Hello 4')
    ping5 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 19, tzinfo=datetime.timezone.utc), prev=ping3, message='Hello 5')
    ping6 = add(session, Ping, created_at=datetime.datetime(2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2024, 2, 29, 12, 10, 20, tzinfo=datetime.timezone.utc), prev=ping5, message='Hello 6')


def create_empty_project_fixture(session):
    admin = get_or_create_admin(session)
    project1 = add(session, Project, title='Test project', description='This is a test project, created empty in a fixture.', created_by=admin, updated_by=admin)


def create_test_exercises_fixture(session):
    admin = get_or_create_admin(session)
    pdffile1 = add(session, PdfFile, bytes_count=484714, pages_count=2, sha256='f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c', created_by=admin)
    pdffilenaming1 = add(session, PdfFileNaming, pdf_file=pdffile1, name='test.pdf', created_by=admin)
    project1 = add(session, Project, title='Premier projet de test', description="Ce projet contient des exercices d'un seul manuel.", created_by=admin, updated_by=admin)
    project2 = add(session, Project, title='Deuxième projet de test', description='Ce projet contient des exercices originaux.', created_by=admin, updated_by=admin)
    textbook1 = add(session, Textbook, project=project1, title='Français CE2', publisher='Slabeuf', year=2021, isbn='1234567890123', created_by=admin, updated_by=admin)
    section1 = add(session, Section, textbook=textbook1, pdf_file=pdffile1, textbook_start_page=6, pdf_file_start_page=1, pages_count=2, created_by=admin, updated_by=admin)
    exercise1 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=6, bounding_rectangle={'stop': {'x': 563.0859853571111, 'y': 165.01653324025676}, 'start': {'x': 321.7851195562453, 'y': 298.5614176476993}}, number='3', instructions='Complète avec : le, une, un, des, tu, elles, ils.\r\nPuis, souligne les verbes.', example='', clue='Il peut y avoir plusieurs solutions.', wording='... vide\r\n... vident\r\n... dépenses\r\n... dépensent\r\n... savon\r\n... savons\r\n... commande', created_by=admin, updated_by=admin)
    exercise2 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=6, bounding_rectangle={'stop': {'x': 565.8489723700982, 'y': 59.10162491711276}, 'start': {'x': 321.7851195562453, 'y': 165.93753244306663}}, number='4', instructions="Écris une phrase en respectant l'ordre des classes grammaticales indiquées.", example='pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.', clue='', wording='nom propre / verbe / déterminant / adjectif / nom commun', created_by=admin, updated_by=admin)
    exercise3 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=7, bounding_rectangle={'stop': {'x': 537.2981065692323, 'y': 689.0650796391174}, 'start': {'x': 313.4961585172843, 'y': 790.3749919482118}}, number='9', instructions='Recopie l’intrus qui se cache dans chaque liste et écris sa classe.', example='', clue='', wording='a. partons ◆ bidons ◆ allons ◆ vendons\r\nb. vidons ◆ mentons ◆ ballons ◆ salons\r\nc. voir ◆ armoire ◆ couloir ◆ dortoir', created_by=admin, updated_by=admin)
    exercise4 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L1', instructions='Faire des choses intelligentes.', example='', clue='', wording='', created_by=admin, updated_by=admin)
    exercise5 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L2', instructions="Faire d'autres choses intelligentes.", example='', clue='', wording='', created_by=admin, updated_by=admin)
    exercise6 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L3', instructions='Prendre le temps de faire aussi des choses banales.', example='', clue='', wording='', created_by=admin, updated_by=admin)


def create_more_test_exercises_fixture(session):
    admin = get_or_create_admin(session)
    pdffile1 = add(session, PdfFile, bytes_count=484714, pages_count=2, sha256='f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c', created_by=admin)
    pdffilenaming1 = add(session, PdfFileNaming, pdf_file=pdffile1, name='test.pdf', created_by=admin)
    project1 = add(session, Project, title='Premier projet de test', description="Ce projet contient des exercices d'un seul manuel.", created_by=admin, updated_by=admin)
    project2 = add(session, Project, title='Deuxième projet de test', description='Ce projet contient des exercices originaux.', created_by=admin, updated_by=admin)
    textbook1 = add(session, Textbook, project=project1, title='Français CE2', publisher='Slabeuf', year=2021, isbn='1234567890123', created_by=admin, updated_by=admin)
    section1 = add(session, Section, textbook=textbook1, pdf_file=pdffile1, textbook_start_page=6, pdf_file_start_page=1, pages_count=2, created_by=admin, updated_by=admin)
    adaptation1 = add(session, FillWithFreeTextAdaptation, placeholder='…', created_by=admin, updated_by=admin)
    adaptation2 = add(session, SelectThingsAdaptation, colors=4, words=True, punctuation=True, created_by=admin, updated_by=admin)
    adaptation3 = add(session, MultipleChoicesInInstructionsAdaptation, placeholder='@', created_by=admin, updated_by=admin)
    adaptation4 = add(session, MultipleChoicesInWordingAdaptation, created_by=admin, updated_by=admin)
    exercise1 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=6, bounding_rectangle={'stop': {'x': 563.0859853571111, 'y': 165.01653324025676}, 'start': {'x': 321.7851195562453, 'y': 298.5614176476993}}, number='3', instructions='Complète avec : le, une, un, des, tu, elles, ils.\r\nPuis, souligne les verbes.', example='', clue='Il peut y avoir plusieurs solutions.', wording='{choices|le|une|un|des|tu|elles|ils} vide\r\n{choices|le|une|un|des|tu|elles|ils} vident\r\n{choices|le|une|un|des|tu|elles|ils} dépenses\r\n{choices|le|une|un|des|tu|elles|ils} dépensent\r\n{choices|le|une|un|des|tu|elles|ils} savon\r\n{choices|le|une|un|des|tu|elles|ils} savons\r\n{choices|le|une|un|des|tu|elles|ils} commande', adaptation=adaptation4, created_by=admin, updated_by=admin)
    exercise2 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=6, bounding_rectangle={'stop': {'x': 565.8489723700982, 'y': 59.10162491711276}, 'start': {'x': 321.7851195562453, 'y': 165.93753244306663}}, number='4', instructions="Écris une phrase en respectant l'ordre des classes grammaticales indiquées.", example='pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.', clue='', wording='nom propre / verbe / déterminant / adjectif / nom commun', created_by=admin, updated_by=admin)
    exercise3 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=7, bounding_rectangle={'stop': {'x': 537.2981065692323, 'y': 689.0650796391174}, 'start': {'x': 313.4961585172843, 'y': 790.3749919482118}}, number='9', instructions='Recopie l’intrus qui se cache dans chaque liste et écris sa classe.', example='', clue='', wording='a. partons ◆ bidons ◆ allons ◆ vendons\r\nb. vidons ◆ mentons ◆ ballons ◆ salons\r\nc. voir ◆ armoire ◆ couloir ◆ dortoir', created_by=admin, updated_by=admin)
    exercise4 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L1', instructions='Faire des choses intelligentes.', example='', clue='', wording='', created_by=admin, updated_by=admin)
    exercise5 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L2', instructions="Faire d'autres choses intelligentes.", example='', clue='', wording='', created_by=admin, updated_by=admin)
    exercise6 = add(session, Exercise, project=project2, textbook=None, textbook_page=None, number='L3', instructions='Prendre le temps de faire aussi des choses banales.', example='', clue='', wording='', created_by=admin, updated_by=admin)
    exercise7 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=7, bounding_rectangle={'stop': {'x': 303.3652061363319, 'y': 311.45540648703854}, 'start': {'x': 57.45936198048777, 'y': 508.54923588836755}}, number='7', instructions='Relève dans le texte trois\n{sel1|déterminants}, un {sel2|nom propre}, quatre\n{sel3|noms communs} et trois {sel4|verbes}.', example='', clue='', wording='Les Touaregs sont des Berbères, un peuple\nqui habite en Afrique du Nord depuis la\npréhistoire. Ils vivent dans le désert du Sahara\n(Algérie, Libye, Mali, Niger, Burkina Faso…). En\nété, les températures y montent à plus de 50 °C\net elles descendent en dessous de zéro durant\nles nuits d’hiver.', adaptation=adaptation2, created_by=admin, updated_by=admin)
    exercise8 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=7, bounding_rectangle={'stop': {'x': 556.6390156601415, 'y': 462.4992757478701}, 'start': {'x': 317.18014120126696, 'y': 538.0212103782859}}, number='11', instructions='Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.', example='', clue='', wording='nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …', adaptation=adaptation1, created_by=admin, updated_by=admin)
    exercise9 = add(session, Exercise, project=project1, textbook=textbook1, textbook_page=7, bounding_rectangle={'start': {'x': 60, 'y': 180}, 'stop': {'x': 250, 'y': 320}}, number='8', instructions='Réponds par {choice|vrai} ou {choice|faux}.', example='', clue='', wording='a. coccinelle est un adjectif. @\nb. bûche est un verbe. @\nc. cette est un déterminant. @\nd. dentier est un verbe. @\ne. respirer est un verbe. @\nf. aspiration est un nom. @', adaptation=adaptation3, created_by=admin, updated_by=admin)
    extractionevent1 = add(session, ExtractionEvent, exercise=exercise7, event='{"kind":"ExerciseNumberSetManually","value":"7"}', created_by=admin, updated_by=admin)
    extractionevent2 = add(session, ExtractionEvent, exercise=exercise7, event='{"kind":"TextSelectedInPdf","pdf":{"name":"test.pdf","sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","page":2,"rectangle":{"start":{"x":41.81553087016726,"y":512.8599582877939},"stop":{"x":299.93876428559844,"y":444.8714829639081}}},"value":"7\\nRelève dans le texte trois\\ndéterminants, un nom propre, quatre\\nnoms communs et trois verbes.","textItems":[{"str":"","font":"g_d0_f2","left":73.5201,"width":0,"right":73.5201,"bottom":488.3804,"height":0,"top":488.3804},{"str":"7","font":"g_d0_f2","left":73.5201,"width":6.492245200000001,"right":80.0123452,"bottom":488.3804,"height":11.6767,"top":500.0571},{"str":" ","font":"g_d0_f2","left":80.0123452,"width":1.4357699349987583,"right":81.44811513499876,"bottom":488.3804,"height":0,"top":488.3804},{"str":"Relève dans le texte trois","font":"g_d0_f1","left":96.7774,"width":134.49874999999994,"right":231.27614999999994,"bottom":487.2676,"height":12.5,"top":499.7676},{"str":"déterminants, un nom propre, quatre","font":"g_d0_f1","left":68.11489999999999,"width":203.32124999999994,"right":271.43614999999994,"bottom":472.2676,"height":12.5,"top":484.7676},{"str":"noms communs et trois verbes.","font":"g_d0_f1","left":68.11489999999999,"width":167.63500000000002,"right":235.74990000000003,"bottom":457.2676,"height":12.5,"top":469.7676}]}', created_by=admin, updated_by=admin)
    extractionevent3 = add(session, ExtractionEvent, exercise=exercise7, event='{"kind":"SelectedTextAddedToInstructions","valueBefore":"","valueAfter":"Relève dans le texte trois\\ndéterminants, un nom propre, quatre\\nnoms communs et trois verbes."}', created_by=admin, updated_by=admin)
    extractionevent4 = add(session, ExtractionEvent, exercise=exercise7, event='{"kind":"TextSelectedInPdf","pdf":{"name":"test.pdf","sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","page":2,"rectangle":{"start":{"x":51.03421777786123,"y":465.61372967289014},"stop":{"x":308.00511532983063,"y":340.0079023796095}}},"value":"Les Touaregs sont des Berbères, un peuple\\nqui habite en Afrique du Nord depuis la\\npréhistoire. Ils vivent dans le désert du Sahara\\n(Algérie, Libye, Mali, Niger, Burkina Faso…). En\\nété, les températures y montent à plus de 50 °C\\net elles descendent en dessous de zéro durant\\nles nuits d’hiver.","textItems":[{"str":"","font":"g_d0_f3","left":68.11489999999999,"width":0,"right":68.11489999999999,"bottom":442.2676,"height":0,"top":442.2676},{"str":"Les Touaregs sont des Berbères, un peuple","font":"g_d0_f3","left":68.11489999999999,"width":226.02625000000015,"right":294.14115000000015,"bottom":442.2676,"height":12.5,"top":454.7676},{"str":"qui habite en Afrique du Nord depuis la","font":"g_d0_f3","left":68.11489999999999,"width":225.87750000000008,"right":293.9924000000001,"bottom":427.2676,"height":12.5,"top":439.7676},{"str":"préhistoire. Ils vivent dans le désert du Sahara","font":"g_d0_f3","left":68.11489999999999,"width":225.99999999999997,"right":294.1149,"bottom":412.2676,"height":12.5,"top":424.7676},{"str":"(Algérie, Libye, Mali, Niger, Burkina Faso…). En","font":"g_d0_f3","left":68.11489999999999,"width":226.01750000000015,"right":294.13240000000013,"bottom":397.2676,"height":12.5,"top":409.7676},{"str":"été, les températures y montent à plus de 50 °C","font":"g_d0_f3","left":68.11489999999999,"width":225.97625000000008,"right":294.0911500000001,"bottom":382.2676,"height":12.5,"top":394.7676},{"str":"et elles descendent en dessous de zéro durant","font":"g_d0_f3","left":68.11489999999999,"width":225.94750000000005,"right":294.0624,"bottom":367.2676,"height":12.5,"top":379.7676},{"str":"les nuits d’hiver.","font":"g_d0_f3","left":68.11489999999999,"width":80.3125,"right":148.42739999999998,"bottom":352.2676,"height":12.5,"top":364.7676}]}', created_by=admin, updated_by=admin)
    extractionevent5 = add(session, ExtractionEvent, exercise=exercise7, event='{"kind":"SelectedTextAddedToWording","valueBefore":"","valueAfter":"Les Touaregs sont des Berbères, un peuple\\nqui habite en Afrique du Nord depuis la\\npréhistoire. Ils vivent dans le désert du Sahara\\n(Algérie, Libye, Mali, Niger, Burkina Faso…). En\\nété, les températures y montent à plus de 50 °C\\net elles descendent en dessous de zéro durant\\nles nuits d’hiver."}', created_by=admin, updated_by=admin)
    extractionevent6 = add(session, ExtractionEvent, exercise=exercise8, event='{"kind":"ExerciseNumberSetManually","value":"11"}', created_by=admin, updated_by=admin)
    extractionevent7 = add(session, ExtractionEvent, exercise=exercise8, event='{"kind":"TextSelectedInPdf","pdf":{"name":"test.pdf","sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","page":2,"rectangle":{"start":{"x":312.61445878367766,"y":537.0592461149397},"stop":{"x":556.9096618375679,"y":493.27005861819964}}},"value":"11\\nAjoute le suffixe –eur aux verbes.\\nIndique la classe des mots fabriqués.","textItems":[{"str":"","font":"g_d0_f2","left":325.8643,"width":0,"right":325.8643,"bottom":517.465,"height":0,"top":517.465},{"str":"11","font":"g_d0_f2","left":325.8643,"width":12.038677700000026,"right":337.90297770000006,"bottom":517.465,"height":11.6767,"top":529.1417},{"str":" ","font":"g_d0_f2","left":337.90297770000006,"width":1.9171360315842636,"right":339.82011373158434,"bottom":517.465,"height":0,"top":517.465},{"str":"Ajoute le suffixe","font":"g_d0_f1","left":360.28880000000004,"width":93.02749999999995,"right":453.31629999999996,"bottom":516.3522,"height":12.5,"top":528.8522},{"str":" ","font":"g_d0_f1","left":453.31629999999996,"width":0.29,"right":453.6063,"bottom":516.3522,"height":0,"top":516.3522},{"str":"–eur","font":"g_d0_f5","left":456.94129999999996,"width":24.385000000000055,"right":481.3263,"bottom":516.3522,"height":12.5,"top":528.8522},{"str":" ","font":"g_d0_f5","left":481.32630000000006,"width":0.28799999999999726,"right":481.61430000000007,"bottom":516.3522,"height":0,"top":516.3522},{"str":"aux verbes.","font":"g_d0_f1","left":484.9263,"width":64.19874999999993,"right":549.12505,"bottom":516.3522,"height":12.5,"top":528.8522},{"str":"Indique la classe des mots fabriqués.","font":"g_d0_f1","left":323.23879999999997,"width":197.90999999999988,"right":521.1487999999998,"bottom":501.85220000000004,"height":12.5,"top":514.3522}]}', created_by=admin, updated_by=admin)
    extractionevent8 = add(session, ExtractionEvent, exercise=exercise8, event='{"kind":"SelectedTextAddedToInstructions","valueBefore":"","valueAfter":"Ajoute le suffixe –eur aux verbes.\\nIndique la classe des mots fabriqués."}', created_by=admin, updated_by=admin)
    extractionevent9 = add(session, ExtractionEvent, exercise=exercise8, event='{"kind":"TextSelectedInPdf","pdf":{"name":"test.pdf","sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","page":2,"rectangle":{"start":{"x":314.9191305106011,"y":503.64118197269073},"stop":{"x":555.7573259741062,"y":452.9379122396233}}},"value":"nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\\ninventer ➞ … ◆ livrer ➞ …","textItems":[{"str":"","font":"g_d0_f3","left":323.23879999999997,"width":0,"right":323.23879999999997,"bottom":487.35220000000004,"height":0,"top":487.35220000000004},{"str":"nager","font":"g_d0_f3","left":323.23879999999997,"width":28.462500000000002,"right":351.70129999999995,"bottom":487.35220000000004,"height":12.5,"top":499.85220000000004},{"str":" ","font":"g_d0_f3","left":351.7013,"width":0.2164960000000019,"right":351.917796,"bottom":487.35220000000004,"height":0,"top":487.35220000000004},{"str":"➞","font":"g_d0_f6","left":354.4075,"width":11.136000000000001,"right":365.54350000000005,"bottom":487.3521,"height":12,"top":499.3521},{"str":" ","font":"g_d0_f6","left":365.54350000000005,"width":0.22604166666666003,"right":365.7695416666667,"bottom":487.3521,"height":0,"top":487.3521},{"str":"…","font":"g_d0_f3","left":368.256,"width":12.425,"right":380.681,"bottom":487.3521,"height":12.5,"top":499.8521},{"str":" ","font":"g_d0_f3","left":380.681,"width":0.2086307692307689,"right":380.88963076923073,"bottom":487.3521,"height":0,"top":487.3521},{"str":"◆","font":"g_d0_f3","left":383.3932,"width":5.902,"right":389.29519999999997,"bottom":487.3521,"height":13,"top":500.3521},{"str":" ","font":"g_d0_f3","left":389.29519999999997,"width":0.21699200000000018,"right":389.51219199999997,"bottom":487.3521,"height":0,"top":487.3521},{"str":"tracter","font":"g_d0_f3","left":392.00759999999997,"width":32.89999999999995,"right":424.9075999999999,"bottom":487.3521,"height":12.5,"top":499.8521},{"str":" ","font":"g_d0_f3","left":424.90759999999995,"width":0.21694400000000313,"right":425.12454399999996,"bottom":487.3521,"height":0,"top":487.3521},{"str":"➞","font":"g_d0_f6","left":427.6194,"width":11.136000000000001,"right":438.7554,"bottom":487.3521,"height":12,"top":499.3521},{"str":" ","font":"g_d0_f6","left":438.7554,"width":0.22603333333332878,"right":438.9814333333333,"bottom":487.3521,"height":0,"top":487.3521},{"str":"…","font":"g_d0_f3","left":441.46779999999995,"width":12.425,"right":453.89279999999997,"bottom":487.3521,"height":12.5,"top":499.8521},{"str":" ","font":"g_d0_f3","left":453.89279999999997,"width":0.4172846153846177,"right":454.3100846153846,"bottom":487.3521,"height":0,"top":487.3521},{"str":"◆","font":"g_d0_f3","left":459.3175,"width":5.902,"right":465.2195,"bottom":487.3521,"height":13,"top":500.3521},{"str":" ","font":"g_d0_f3","left":465.2195,"width":0.21699200000000018,"right":465.436492,"bottom":487.3521,"height":0,"top":487.3521},{"str":"manger","font":"g_d0_f3","left":467.9319,"width":37.712499999999984,"right":505.64439999999996,"bottom":487.3521,"height":12.5,"top":499.8521},{"str":" ","font":"g_d0_f3","left":505.6444,"width":0.21694399999999858,"right":505.86134400000003,"bottom":487.3521,"height":0,"top":487.3521},{"str":"➞","font":"g_d0_f6","left":508.3562,"width":11.136000000000001,"right":519.4922,"bottom":487.3521,"height":12,"top":499.3521},{"str":" ","font":"g_d0_f6","left":519.4922,"width":0.22603333333333353,"right":519.7182333333334,"bottom":487.3521,"height":0,"top":487.3521},{"str":"…","font":"g_d0_f3","left":522.2046,"width":12.425,"right":534.6296,"bottom":487.3521,"height":12.5,"top":499.8521},{"str":" ","font":"g_d0_f3","left":534.6296,"width":0.4172769230769273,"right":535.0468769230769,"bottom":487.3521,"height":0,"top":487.3521},{"str":"◆","font":"g_d0_f3","left":540.0542,"width":5.902,"right":545.9562000000001,"bottom":487.3521,"height":13,"top":500.3521},{"str":"inventer","font":"g_d0_f3","left":323.2332,"width":41.06249999999997,"right":364.2957,"bottom":472.8521,"height":12.5,"top":485.3521},{"str":" ","font":"g_d0_f3","left":364.2957,"width":0.21695200000000114,"right":364.512652,"bottom":472.8521,"height":0,"top":472.8521},{"str":"➞","font":"g_d0_f6","left":367.0076,"width":11.136000000000001,"right":378.14360000000005,"bottom":472.8521,"height":12,"top":484.8521},{"str":" ","font":"g_d0_f6","left":378.14360000000005,"width":0.22604166666666003,"right":378.3696416666667,"bottom":472.8521,"height":0,"top":472.8521},{"str":"…","font":"g_d0_f3","left":380.85609999999997,"width":12.425,"right":393.2811,"bottom":472.8521,"height":12.5,"top":485.3521},{"str":" ","font":"g_d0_f3","left":393.2811,"width":0.41727692307692293,"right":393.6983769230769,"bottom":472.8521,"height":0,"top":472.8521},{"str":"◆","font":"g_d0_f3","left":398.7057,"width":5.902,"right":404.60769999999997,"bottom":472.8521,"height":13,"top":485.8521},{"str":" ","font":"g_d0_f3","left":404.60769999999997,"width":0.21699200000000018,"right":404.82469199999997,"bottom":472.8521,"height":0,"top":472.8521},{"str":"livrer","font":"g_d0_f3","left":407.32009999999997,"width":25.71250000000005,"right":433.0326,"bottom":472.8521,"height":12.5,"top":485.3521},{"str":" ","font":"g_d0_f3","left":433.0326,"width":0.21692000000000008,"right":433.24952,"bottom":472.8521,"height":0,"top":472.8521},{"str":"➞","font":"g_d0_f6","left":435.7441,"width":11.136000000000001,"right":446.8801,"bottom":472.8521,"height":12,"top":484.8521},{"str":" ","font":"g_d0_f6","left":446.8801,"width":0.22603333333332878,"right":447.10613333333333,"bottom":472.8521,"height":0,"top":472.8521},{"str":"…","font":"g_d0_f3","left":449.5925,"width":12.425,"right":462.0175,"bottom":472.8521,"height":12.5,"top":485.3521}]}', created_by=admin, updated_by=admin)
    extractionevent10 = add(session, ExtractionEvent, exercise=exercise8, event='{"kind":"SelectedTextAddedToWording","valueBefore":"","valueAfter":"nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\\ninventer ➞ … ◆ livrer ➞ …"}', created_by=admin, updated_by=admin)


def create_import_from_visio_method_fixture(session):
    admin = get_or_create_admin(session)
    pdfFile = add(session, PdfFile, bytes_count=484714, pages_count=2, sha256="0beb715f8ed379b056a3d40522dcc8e0658c58316b3ef7a09da78c541257d756", created_by=admin)
    add(session, PdfFileNaming, pdf_file=pdfFile, name="manual_CE2_FRANCAIS_HACHETTE.p13a15.pdf", created_by=admin)
    project = add(session, Project, title="Vincent teste l'import des fichiers de Olivier", description="", created_by=admin, updated_by=admin)
    textbook = add(session, Textbook, project=project, title="Français CE2", publisher="Hachette", year=2024, isbn=None, created_by=admin, updated_by=admin)
    add(session, Section, textbook=textbook, pdf_file=pdfFile, textbook_start_page=13, pdf_file_start_page=1, pages_count=3, created_by=admin, updated_by=admin)

    with open("../pdf-examples/manual_CE2_FRANCAIS_HACHETTE.p13.json", "r") as f:
        page_data = import_from_visio_method.PageData(**json.load(f))

    import_from_visio_method.import_page(session, admin, textbook, page_data)



available_fixtures = {
    "admin-user": create_admin_user_fixture,
    "test-users": create_test_users_fixture,
    "test-pings": create_test_pings_fixture,
    "empty-project": create_empty_project_fixture,
    "test-exercises": create_test_exercises_fixture,
    "more-test-exercises": create_more_test_exercises_fixture,
    "import-from-visio-method": create_import_from_visio_method_fixture,
}

def load(session, fixtures):
    database_utils.truncate_all_tables(session)
    for fixture in fixtures:
        available_fixtures[fixture](session)
