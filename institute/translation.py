from modeltranslation.translator import TranslationOptions, register

from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


class DefaultTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(Cafedra)
class CafedraTranslateOptions(DefaultTranslationOptions):
    pass


@register(Fakultet)
class FakultetTranslateOptions(DefaultTranslationOptions):
    pass


@register(Center)
class CenterTranslateOptions(DefaultTranslationOptions):
    pass


@register(Department)
class DepartmentTranslateOptions(DefaultTranslationOptions):
    pass


@register(Page)
class PageTranslateOptions(DefaultTranslationOptions):
    pass


# @register(Cafedra)
# class CafedraTranslateOptions(DefaultTranslationOptions):
#     pass


# @register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ("title", "content")
