from django.contrib import admin
from .models import Post
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Choice


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = 'id'


class YourModelAdmin(TranslationAdmin):
    fields = ('name',)
    # list_display = ('id', 'name',)


admin.site.register(Choice, YourModelAdmin)

# Register your models here.
admin.site.register(Post)
