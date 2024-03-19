## Consulta Para CEPs

### Visão Geral

Esse projeto se basea em fazer uma consulta na API de CEPs.

### Uso

O objetivo principal deste projeto é realizar uma consulta usando o CEP ou o lograudoro informado pelo usuario e ele devolve as informações que se pode obter na API.

### Funcionalidades Principais

- **Script main.py:**
  - Esse script é um aplicativo web usando Flask que permite aos usuários consultar informações de um CEP. Ele utiliza o método POST para receber o CEP digitado pelo usuário, faz uma requisição GET ao ViaCEP para obter os dados do CEP e exibe essas informações em uma página HTML renderizada pelo Flask. O aplicativo também lida com casos em que a requisição não é bem-sucedida, retornando None para indicar que não foram encontradas informações para o CEP fornecido. O código inclui também um template HTML chamado 'inicio.html' para renderizar a página com as informações do CEP.
  - [Ver Script](https://github.com/gabriel-joao/Consulta_Cep/blob/main/CEP/main.py)

- **Script CEP_por_numeros:**
  - Esse script em Python utiliza a biblioteca requests para fazer requisições GET ao serviço ViaCEP, obtendo informações detalhadas de um CEP informado pelo usuário. Ele extrai dados como logradouro, bairro, cidade e UF a partir da resposta JSON da requisição. O script também permite ao usuário fazer mais consultas, caso deseje. O fluxo geral inclui verificar se a requisição foi bem-sucedida, imprimir os dados do CEP, e perguntar ao usuário se deseja fazer mais consultas, repetindo o processo se a resposta for afirmativa.
  [Ver Script](https://github.com/gabriel-joao/Consulta_Cep/blob/main/CEP/CEP_por_numeros)

### Autores

João

### Contato

<p align="center">
  <b>João</b><br>
  <a href="https://www.linkedin.com/in/jo%C3%A3o-gabriel-souza-santos-b0289a224/">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>
