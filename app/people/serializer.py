from rest_framework import serializers

from app.people.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "name", "birthdate", "cpf", "gender", "height", "weight")
