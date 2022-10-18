from django.urls import path
from .views import TransacaoViewCreate, TransacaoViewOthers

urlpatterns = [
    path('transacao/', TransacaoViewCreate.as_view()),
    path('transacao/', TransacaoViewOthers.as_view()),
]
