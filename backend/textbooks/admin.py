from django.contrib import admin

from .models import PdfFile, PdfFileNaming, Textbook, Section, Exercise, ExtractionEvent


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0

class PdfFileNamingInline(admin.TabularInline):
    model = PdfFileNaming
    extra = 0

@admin.register(PdfFile)
class PdfFileAdmin(admin.ModelAdmin):
    inlines = [PdfFileNamingInline, SectionInline]


class ExerciseInline(admin.StackedInline):
    model = Exercise
    extra = 0

@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ExerciseInline]


class ExtractionEventInline(admin.TabularInline):
    model = ExtractionEvent
    extra = 0

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [ExtractionEventInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
