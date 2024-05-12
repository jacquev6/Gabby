from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent
from .models import Adaptation, SelectThingsAdaptation, FillWithFreeTextAdaptation


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



class AdaptationChildAdmin(PolymorphicChildModelAdmin):
    base_model = Adaptation

@admin.register(SelectThingsAdaptation)
class SelectThingsAdaptationAdmin(AdaptationChildAdmin):
    base_model = SelectThingsAdaptation

@admin.register(FillWithFreeTextAdaptation)
class FillWithFreeTextAdaptationAdmin(AdaptationChildAdmin):
    base_model = FillWithFreeTextAdaptation

@admin.register(Adaptation)
class AdaptationParentAdmin(PolymorphicParentModelAdmin):
    base_model = Adaptation
    child_models = (SelectThingsAdaptation, FillWithFreeTextAdaptation)
