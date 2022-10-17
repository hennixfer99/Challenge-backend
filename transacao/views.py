from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from transacao.models import Transacoes
from transacao.serializers import TransacoesSerializer


class TransacaoView(ListCreateAPIView):


    serializer_class = TransacoesSerializer
    queryset = Transacoes.objects.all()


class TransacaoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransacoesSerializer
    queryset = Transacoes.objects.all()

