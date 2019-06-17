from django.contrib import admin

from .models import Choice, Question, Phrase, Burarra, Warlpiri

class BurarraInline(admin.TabularInline):
    model = Burarra


class WarlpiriInline(admin.TabularInline):
    model = Warlpiri

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PhraseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['phrase_text']}),
    ]
    inlines = [BurarraInline, WarlpiriInline]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Burarra)
admin.site.register(Warlpiri)

list_display = ('question_text', 'pub_date')
list_filter = ['pub_date']
search_fields = ['question_text']