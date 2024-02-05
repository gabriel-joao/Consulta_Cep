from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index():
    informacoes_cep = None

    if request.method == 'POST':
        cep_digitado = request.form['cep']
        print(f'Tentativa de consultar o CEP: {cep_digitado}')

        informacoes_cep = obter_informacoes_cep(cep_digitado)
        print(f'Resultado da consulta: {informacoes_cep}')

    print('Renderizando template')
    return render_template('inicio.html', informacoes_cep=informacoes_cep)


def obter_informacoes_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)