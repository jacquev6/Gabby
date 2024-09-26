from .old_adaptations.fill_with_free_text import FillWithFreeTextAdaptation
from .old_adaptations.items_and_effects__attempt_1 import ItemsAndEffectsAttempt1Adaptation
from .old_adaptations.multiple_choices_in_instructions import MultipleChoicesInInstructionsAdaptation
from .old_adaptations.multiple_choices_in_wording import MultipleChoicesInWordingAdaptation
from .old_adaptations.select_things import SelectThingsAdaptation
from .exercises import OldAdaptation, GenericOldAdaptation, Exercise, ExtractionEvent
from .pdfs import PdfFile, PdfFileNaming
from .pings import Ping
from .projects import Project
from .textbooks import Section, Textbook
from .users import User, UserEmailAddress


all_models = [
    OldAdaptation,
    Exercise,
    ExtractionEvent,
    FillWithFreeTextAdaptation,
    GenericOldAdaptation,
    ItemsAndEffectsAttempt1Adaptation,
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
