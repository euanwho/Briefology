from django.contrib import admin
from .models import Steno, Word

class StenoInline(admin.TabularInline):
    model = Steno

class WordAdmin(admin.ModelAdmin):
    list_display = ['word']
    inlines = [
        StenoInline,
    ]
    child_models = (Steno)

class StenoAdmin(admin.ModelAdmin):
    fields = ['word']

admin.site.register(Steno, StenoAdmin)
admin.site.register(Word, WordAdmin)