from django.contrib import admin  # NOQA: F401
from mptt.admin import DraggableMPTTAdmin

from quiz.models import Category, Category2, Choice, Question, Quiz, Result

admin.site.register([Question, Choice, Result])


@admin.register(Category2)
class Category2Admin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = (
        "tree_actions",
        "indented_title",
        "parent",
    )
    list_display_links = ("indented_title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    list_filter = ("parent",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description")
