from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent
from .models import AdaptedExercise, SelectThingsAdaptedExercise, FillWithFreeTextAdaptedExercise


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0

class PdfFileNamingInline(admin.TabularInline):
    model = PdfFileNaming
    extra = 0

@admin.register(PdfFile)
class PdfFileAdmin(admin.ModelAdmin):
    inlines = [PdfFileNamingInline, SectionInline]


@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


class ExtractionEventInline(admin.TabularInline):
    model = ExtractionEvent
    extra = 0

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [ExtractionEventInline]



class AdaptedExerciseChildAdmin(PolymorphicChildModelAdmin):
    base_model = AdaptedExercise

@admin.register(SelectThingsAdaptedExercise)
class SelectThingsAdaptedExerciseAdmin(AdaptedExerciseChildAdmin):
    base_model = SelectThingsAdaptedExercise

@admin.register(FillWithFreeTextAdaptedExercise)
class FillWithFreeTextAdaptedExerciseAdmin(AdaptedExerciseChildAdmin):
    base_model = FillWithFreeTextAdaptedExercise

@admin.register(AdaptedExercise)
class AdaptedExerciseParentAdmin(PolymorphicParentModelAdmin):
    base_model = AdaptedExercise
    child_models = (SelectThingsAdaptedExercise, FillWithFreeTextAdaptedExercise)
