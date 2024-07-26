from django.contrib import admin

from app.people.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "birthdate", "cpf", "gender", "height", "weight"]
    list_filter = ["gender", "birthdate"]
    search_fields = ["name", "cpf"]
