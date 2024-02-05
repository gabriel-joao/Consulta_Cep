import requests


def obter_informacoes_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Fazendo a requisição GET para o ViaCEP
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Extraindo e imprimindo os dados JSON
        dados_cep = response.json()
        print(f"Informações do CEP {cep}:\n")
        print(f"Logradouro: {dados_cep.get('logradouro')}")
        print(f"Bairro: {dados_cep.get('bairro')}")
        print(f"Cidade/UF: {dados_cep.get('localidade')}/{dados_cep.get('uf')}\n")

        # Perguntando ao usuário se deseja fazer mais uma consulta
        mais_uma_consulta = input("Deseja fazer mais uma consulta? (Digite 'sim' ou 'não'): ")
        if mais_uma_consulta.lower() == 'sim':
            cep_digitado = input("Digite o CEP (apenas números): ")
            obter_informacoes_cep(cep_digitado)
        else:
            print("Consulta encerrada.")
    else:
        print(f"Falha na requisição baseado no CEP informado.\n")

        # Perguntando ao usuário se deseja fazer mais uma consulta
        mais_uma_consulta = input("Deseja fazer mais uma consulta? (Digite 'sim' ou 'não'): ")
        if mais_uma_consulta.lower() == 'sim':
            cep_digitado = input("Digite o CEP (apenas números): ")
            obter_informacoes_cep(cep_digitado)


# Exemplo de uso
cep_digitado = input("Digite o CEP (apenas números): ")
obter_informacoes_cep(cep_digitado)
