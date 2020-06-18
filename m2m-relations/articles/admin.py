from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        forms_with_is_main = [form.cleaned_data for form in self.forms
            if form.cleaned_data.get('is_main')]
        form_with_is_main_for_delete = [form for form in forms_with_is_main
            if form.get('DELETE')]
        if (len(forms_with_is_main) - len(form_with_is_main_for_delete)) !=1:
            raise ValidationError('Главный таг обезателен и может быть только одним')
        return super().clean()  # вызываем базовый код переопределяемого метода

class TagInline(admin.TabularInline):
    model = Tag.articles.through
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article, Tag)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline, ]
