from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import CEP


def buscar_cep(request, cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        data = response.json()

        if 'erro' in data:
            return JsonResponse({'error': 'CEP não encontrado!'}, status=404)

        # Criar ou atualizar o objeto do CEP no banco de dados
        obj, created = CEP.objects.update_or_create(
            cep=data['cep'],
            defaults={
                'logradouro': data['logradouro'],
                'bairro': data['bairro'],
                'localidade': data['localidade'],
                'uf': data['uf']
            }
        )
        return JsonResponse({
            'cep': obj.cep,
            'logradouro': obj.logradouro,
            'bairro': obj.bairro,
            'localidade': obj.localidade,
            'uf': obj.uf
        })
    except requests.ConnectionError:
        return JsonResponse({'error': 'Erro de conexão'}, status=500)
