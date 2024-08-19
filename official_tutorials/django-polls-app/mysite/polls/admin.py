from django.contrib import admin

# Register your models here.
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """Settings for Choice options inline with a Question admin form."""

    model = Choice
    ## Default number of choices to allow when creating inline with a Question.
    #  There will be an option to add additional on the Question form.
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    ## Set order of fields on page
    # fields = ["pub_date", "question_text"]

    ## Detail layout of the admin form
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    ## Add Choice creator to Question admin form
    inlines = [ChoiceInline]

    ## Control layout of Questions in a list in the admin site
    list_display = ["question_text", "pub_date", "was_published_recently"]

    ## Add options to the admin site's filter sidebar
    list_filter = ["pub_date"]

    ## Add search functionality to the admin site for Question objects
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
## Registering a Choice allows adding from admin site, but not from the Question admin form.
# admin.site.register(Choice)
