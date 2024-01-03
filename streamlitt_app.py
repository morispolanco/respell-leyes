import streamlit as st
import requests

def main():
    st.title('Consulta de leyes de Guatemala')
    question = st.text_input('Ingresa tu pregunta')
    if st.button('Consultar'):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805',
            'Content-Type': 'application/json'
        }
        data = {
            'spellId': 'ca5HnP9i5zD4XoOvfjkc5',
            'spellVersionId': 'ncTyRRaMDQzEk54VktNsq',
            'inputs': {
                'input': question
            }
        }
        response = requests.post('https://api.respell.ai/v1/run', headers=headers, json=data)
        result = response.json()
        st.markdown(f"{result['output']}")
if __name__ == '__main__':
    main()
