# Gerador de Senhas

Aplicação web em Python que gera senhas aleatórias e também verifica se uma senha já apareceu em vazamentos de dados.

## Funcionalidades
- Escolha o tamanho e os tipos de caracteres (maiúsculas, números, símbolos)
- Garantia de pelo menos um caractere de cada tipo escolhido
- Histórico das últimas senhas geradas na sessão
- Verificação de vazamento pela API pública Pwned Passwords

## Tecnologias
Python, Streamlit, Requests, API Pwned Passwords

## Segurança
- As senhas são sorteadas com o módulo `secrets`, próprio para uso criptográfico.
- Na verificação de vazamento, apenas os 5 primeiros caracteres do hash SHA-1 são enviados à API Pwned Passwords (k-anonimidade). A API nunca recebe a senha nem o hash completo.
- O histórico fica apenas na memória da sessão (`st.session_state`) e é descartado ao fechar a página. Nada é gravado em disco ou banco de dados.

### Demo online x uso local
No Streamlit, o código Python roda no servidor, não no navegador. Por isso, na versão publicada no Streamlit Cloud, a senha digitada trafega (via HTTPS) até o servidor do app antes de o hash ser calculado, e as senhas geradas também são criadas lá. Use a demo apenas com senhas de teste. Para verificar ou gerar senhas reais, rode localmente: assim todo o processamento acontece na sua máquina.

## Como rodar localmente
    git clone https://github.com/BernalDy/Gerador-Senhas-Simp.git
    cd Gerador-Senhas-Simp
    pip install -r requirements.txt
    streamlit run app.py
## Sobre o projeto
Primeiro projeto em Python, desenvolvido em um dia como prova de conceito, com alguns pedidos de linhas criadas com a mentoria de IA (Claude). Todo o código foi digitado e testado no terminal por mim.
