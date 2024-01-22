import requests

def obter_informacoes_endereco(uf, cidade, logradouro):
    while True:
        url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'

        # Fazendo a requisição GET para o ViaCEP
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Extraindo e imprimindo os dados JSON
            dados_endereco = response.json()

            # Verificando se há resultados na lista
            if dados_endereco:
                print(f"Informações do Endereço {logradouro}, {cidade}/{uf}:\n")
                print(f"Bairro: {dados_endereco[0].get('bairro')}")
                print(f"CEP: {dados_endereco[0].get('cep')}")

                # Perguntando ao usuário se deseja fazer mais uma consulta
                mais_uma_consulta = input("\nDeseja fazer mais uma consulta? (Digite 'sim' ou 'não'): ")
                if mais_uma_consulta.lower() == 'sim':
                    uf = input("Digite a UF (ex: RS): ")
                    cidade = input("Digite a cidade: ")
                    logradouro = input("Digite o logradouro: ")
                else:
                    print("Consulta encerrada.")
                    break
            else:
                print(f"Falha na requisição baseado nos dados informado.\n")
                # Perguntando ao usuário se deseja fazer mais uma consulta
                mais_uma_consulta = input("\nDeseja fazer mais uma consulta? (Digite 'sim' ou 'não'): ")
                if mais_uma_consulta.lower() == 'sim':
                    uf = input("Digite a UF (ex: RS): ")
                    cidade = input("Digite a cidade: ")
                    logradouro = input("Digite o logradouro: ")
                else:

                    print("Consulta encerrada.")
                    break
        else:
            print(f"Falha na requisição baseado nos dados informado.\n")
            # Perguntando ao usuário se deseja fazer mais uma consulta
            mais_uma_consulta = input("\nDeseja fazer mais uma consulta? (Digite 'sim' ou 'não'): ")
            if mais_uma_consulta.lower() == 'sim':
                uf = input("Digite a UF (ex: RS): ")
                cidade = input("Digite a cidade: ")
                logradouro = input("Digite o logradouro: ")
            else:
                print("Consulta encerrada.")
                break

if __name__ == "__main__":
    # Obtendo as entradas do usuário
    uf_digitada = input("Digite a UF (ex: RS): ")
    cidade_digitada = input("Digite a cidade: ")
    logradouro_digitado = input("Digite o logradouro: ")

    # Chamando a função com as entradas do usuário
    obter_informacoes_endereco(uf_digitada, cidade_digitada, logradouro_digitado)
