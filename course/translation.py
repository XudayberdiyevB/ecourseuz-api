from modeltranslation.translator import translator, TranslationOptions

from course.models import Course


class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'desc')


translator.register(Course, CourseTranslationOptions)
