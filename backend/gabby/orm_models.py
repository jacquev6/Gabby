from .exercises import Exercise
from .pdfs import PdfFile, PdfFileNaming
from .pings import Ping
from .projects import Project
from .textbooks import Section, Textbook
from .users import User, UserEmailAddress


all_models = [
    Exercise,
    PdfFile,
    PdfFileNaming,
    Ping,
    Project,
    Section,
    Textbook,
    User,
    UserEmailAddress,
]
