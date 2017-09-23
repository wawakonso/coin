
from person.models import Person, Identification
from rest_framework import serializers

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields = ('id_num',)

class PersonSerializer(serializers.ModelSerializer):
    identification = IdentificationSerializer(many=False, read_only=True)
    dob = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Person
        fields = ('prenom','nom','postnom','gender','dob','citizen','identification')
