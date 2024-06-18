from .adaptations.fill_with_free_text import FillWithFreeTextAdaptation
from .adaptations.multiple_choices_in_instructions import MultipleChoicesInInstructionsAdaptation
from .adaptations.multiple_choices_in_wording import MultipleChoicesInWordingAdaptation
from .adaptations.select_things import SelectThingsAdaptation
from .exercises import Adaptation, GenericAdaptation, Exercise, ExtractionEvent
from .pdfs import PdfFile, PdfFileNaming
from .pings import Ping
from .projects import Project
from .textbooks import Section, Textbook
from .users import User, UserEmailAddress


all_models = [
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
    UserEmailAddress,
]
