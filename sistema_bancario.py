# Projeto de um sistema bancário com 1 único usuário, 4 operações principais a seguir: 

# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""


# Variáveis do sistema bancário
saldo = 0           # Saldo inicial da conta
limite = 500        # Limite de saque por operação
extrato = ""        # Extrato das operações realizadas
numero_saques = 0   # Contador de saques realizados
limite_saques = 3   # Limite máximo de saques por dia


# Loop principal do sistema bancário:
while True:  
    opcao = input(menu + "Informe a opção desejada: ")  # Guarda a opção escolhida pelo usuário
	

	#DEPÓSITO
    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))  # Guarda valor depositado
		
        # Verifica se valor do depósito é válido: 
        if valor > 0:
            saldo += valor                              # Atualiza o saldo com valor depositado
            extrato += f"Depósito: R$ {valor:.2f}\n"    # Atualiza o extrato, mencionando haver depósito 
			
        else:
            print("Operação falhou! O valor informado é inválido.") 


	#SAQUE										
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
		
		# Criando variáveis para as respostas
        excedeu_saldo = valor > saldo                  # Verifica se saque é maior que valor disponível 
		
        excedeu_limite = valor > limite                # Verifica se valor de saque excede o limite por saque
		
        excedeu_saques = numero_saques >= limite_saques# Verifica se o número de saques diários foi excedido
		
		

		# Exibe respostas das condições - SAQUE
        if excedeu_saldo:
	        print("Operação falhou! Você não tem saldo suficiente.")
				
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite por operação.")
				
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor >= 0:                               # Verifica se valor de saque é positivo
            saldo -= valor                             # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"      # Atualiza o extrato
            numero_saques += 1                         # Incrementa o contador de saques
						
        else:
            print("Operação falhou! O valor informado é inválido")
			

	
	# EXTRATO - mostrará movimentações e saldo atual					
    elif opcao == "e":
        print("\n============Extrato============")     # Cabeçalho do extrato, com quebras de linha
        print("Não foram realizadas movimentações") if not extrato else extrato 
        # se extrato estiver vazio, imprime Não foram real.... caso contrário, imprime conteúdo armazenado em extrato
        print(f"\nSaldo: R$ {saldo:.2f}")              # Imprime saldo atual da conta
        print("=============Extrato=============")     # Imprime rodapé, encerrando a seção de visualização das funções
				
				
	# SAIR	
    elif opcao == "q":
        break   # Sai do loop While True quando usuário escolhe opção Sair, finalizando execução do sistema bancário
		
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada") 
        # Imprime mensagem se opção informada do usuário não corresponder a nenhuma das opções válidas, nem mesmo a opção Sair
