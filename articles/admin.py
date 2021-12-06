from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from articles.models import Article, Scope,Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):

        main_counter = 0
        for form in self.forms:
            try:
                if form.cleaned_data['is_main']:
                    main_counter += 1
            except KeyError:
                pass
        if main_counter > 1:
            raise ValidationError('Основной раздел может быть только один')
        elif main_counter < 1:
            raise ValidationError('Вы должны назначить хотя бы один основной раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    inlines = [ScopeInline]
    pass


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id','name',]


