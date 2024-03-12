from django.contrib import admin

from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent


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
