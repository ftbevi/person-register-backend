from rest_framework import viewsets
from rest_framework.views import APIView
from app.people.models import Person, GenderOption
from app.people.serializer import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

class PersonModelView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCalcAPIView(APIView):
    def get(self, request, user_id, format=None):
        person = Person.objects.filter(id=user_id).first()

        if not person:
            return Response(status=status.HTTP_404_NOT_FOUND)

        person_calc =  {
            GenderOption.NAO_INFORMAR.value: { "person": "Não é possível calcular. Gênero Indefinido"},
            GenderOption.MASCULINO.value: { "person": (Decimal(72.7) * person.height) - Decimal(58) },
            GenderOption.FEMININO.value: { "person": (Decimal(62.1) * person.height) - Decimal(44.7) }
        }

        return Response(data=person_calc[person.gender], status=status.HTTP_200_OK)
