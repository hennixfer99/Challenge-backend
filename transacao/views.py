from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from transacao.models import Transacoes
from transacao.serializers import TransacoesSerializer
from .mixins import New_mixin

class TransacaoViewCreate(New_mixin, ListCreateAPIView): 

    serializer_class = TransacoesSerializer
    
    queryset = Transacoes.objects.all()


class TransacaoViewOthers(RetrieveUpdateDestroyAPIView):
    serializer_class = TransacoesSerializer
    queryset = Transacoes.objects.all()

