from .exercises import Adaptation, Exercise, ExtractionEvent
from .exercises import GenericAdaptation, SelectThingsAdaptation, FillWithFreeTextAdaptation, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInWordingAdaptation
from .pdfs import PdfFile, PdfFileNaming
from .pings import Ping
from .projects import Project
from .textbooks import Section, Textbook
from .users import User


models = [
    Adaptation,
    Exercise,
    ExtractionEvent,
    FillWithFreeTextAdaptation,
    GenericAdaptation,
    MultipleChoicesInInstructionsAdaptation,
    MultipleChoicesInWordingAdaptation,
    PdfFile,
    PdfFileNaming,
    Ping,
    Project,
    Section,
    SelectThingsAdaptation,
    Textbook,
    User,
]
