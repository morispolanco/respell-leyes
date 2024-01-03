import requests

def consultar_respuesta(pregunta):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805',
        'Content-Type': 'application/json'
    }
    data = {
        'spellId': 'ca5HnP9i5zD4XoOvfjkc5',
        'spellVersionId': 'ncTyRRaMDQzEk54VktNsq',
        'inputs': {
            'input': pregunta
        }
    }
    response = requests.post('https://api.respell.ai/v1/run', headers=headers, json=data)
    result = response.json()
    return result

# Ejemplo de uso:
pregunta_usuario = "¿Cuál es mi pregunta?"
resultado = consultar_respuesta(pregunta_usuario)
print(resultado)
