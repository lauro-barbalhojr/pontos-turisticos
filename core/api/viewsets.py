from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'nome'


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.filter()

        if id:
            queryset = PontoTuristico.objects.filter(pk = id)

        if nome:
            queryset = queryset.filter(nome__iexact = nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact = descricao)

        return queryset