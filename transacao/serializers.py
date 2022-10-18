from rest_framework import serializers
from .models import Transacoes

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = "__all__"
         