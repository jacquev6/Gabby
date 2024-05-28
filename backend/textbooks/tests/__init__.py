# @todo Run tests from *all* Python files, not just 'test*.py'. Then remove these imports.
from .rest_api import PdfFileApiTestCase, TextbookApiTestCase, ExerciseModelTestCase, ExerciseApiTestCase, AdaptationModelTestCase, AdaptationApiTestCase
from .adapted_exercise import SelectThingsAdaptationTestCase, FillWithFreeTextAdaptationTestCase, MultipleChoicesAdaptationTestCase, AdaptedExerciseApiTestCase
from ..parsing import ParseGenericSectionTestCase
