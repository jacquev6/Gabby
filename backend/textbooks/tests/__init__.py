# @todo Run tests from *all* Python files, not just 'test*.py'. Then remove these imports.
from .rest_api import PdfFileApiTestCase, TextbookApiTestCase, ExerciseModelTestCase, ExerciseApiTestCase, AdaptedExerciseModelTestCase, AdaptedExerciseApiTestCase
from .adapted_exercise import SelectWordsAdaptedExerciseBusinessTestCase, AdaptedExerciseApiTestCase
from ..parsing import TokenizeTextTestCase
