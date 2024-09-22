# Sistema bancário

## Descrição: Um sistema bancário simples que permite ao usuário realizar operações de depósito, saque e consultar o extrato da conta.

## Instalação: 
    1. Clone o repositório:
    git clone <URL_do_repositório>
    2. Navegue até a pasta do projeto: cd sistema_bancario

## Uso: Para executar o sistema, use:python sistema_bancario.py

## Tecnologias
- Python

## Licença
-

## Detalhes da V.1:
- V.1  do sistema: implementar as operações depósito, saque e extrato
    - DEPÓSITO:
        - Depositar valores positivos na conta bancária, visto que não existe depósito negativo de dinheiro
        - Essa versão trabalhará apenas com 1 usuário, não necessitando identificação de agência e conta bancária de usuário
        - Todos os depósitos serão armazenados em uma variável só e exibidos na operação de extrato, pois usaremos a variável que os armazena em outra operação
    - SAQUE
        - Sistema permitirá realizar 3 saques diários
        - Cada saque tem limite máximo R$ 500,00 → se usuário tem saldo = 1000 e tenta sacar R$ 1000,00, sistema não permitirá
        - Se usuário não tiver saldo em conta, sistema exibirá mensagem informando impossibilidade do saque devido a falta de saldo → se saldo = 2, ele não permitirá sacar valor maior que R$ 2,00
        - Todos os saques serão armazenados em uma variável e exibidos na operação de extrato
    - EXTRATO
        - Deve listar todos os depósitos e saques realizados
        - No fim da listagem, deve exibir o saldo atual da conta
        - Exibir os valores usando formato R$ xxx.xx
            - 100.45 → R$ 100.45
