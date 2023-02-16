from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico, Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa',
            )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
