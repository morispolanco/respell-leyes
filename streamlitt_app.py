import streamlit as st
import requests

st.title("Consulta de leyes de Guatemala")

# Función que realiza la petición a la API de Respell
def consulta_leyes(pregunta):
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
    return response.json()

# Función que se encarga de mostrar el resultado de la consulta
def mostrar_resultado(resultado):
    st.write(resultado)

# Captura de la pregunta del usuario
pregunta = st.text_input("Ingresa tu pregunta:")

# Envía la pregunta a la API de Respell y muestra el resultado
consulta_leyes(pregunta)
mostrar_resultado(consulta_leyes(pregunta))
