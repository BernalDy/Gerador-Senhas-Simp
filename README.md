# Gerador de Senhas

Aplicação web em Python que gera senhas aleatórias e também verifica se uma senha já apareceu em vazamentos de dados.

## Funcionalidades
- Escolha o tamanho e os tipos de caracteres (maiúsculas, números, símbolos)
- Garantia de pelo menos um caracteres de cada tipo escolhido
- Histórico das últimas senhas geradas na sessão
- Verificação de vazamento pela API pública Pwned Passwords

## Tecnologias
Python, Streamlit, Requests, API Pwned Passwords

## Segurança
- As senhas são sorteadas com o módulo `secrets`, próprio para uso criptográfico.
- Na verificação de vazamento, a senha não sai do computador: apenas os 5 primeiros caracteres do hash SHA-1 são enviados à API.
- O histórico existe só durante a sessão do navegador e não é salvo em servidor.

## Como rodar localmente
    pip install -r requirements.txt
    streamlit run app.py

## Sobre o projeto
Primeiro projeto em Python, desenvolvido em um dia como prova de conceito, com alguns pedidos de linhas criadas com a mentoria de IA (Claude). Todo o código foi digitado e testado no terminal por mim.