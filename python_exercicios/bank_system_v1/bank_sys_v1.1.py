'''
3 Operações:
- Depósito
    * Valores Positivos;
    * Todos os Depósitos devem ser armazenados em uma varíavel e exibidos
        na operação de Extrato.
- Saque
    * Limite de 3 Saques;
    * Máximo de R$500,00 por saque;
    * Caso não tenha saldo, exibir mensagem de que não será possível
        completar a operação por falta de saldo;
    * Todos os Saques devem ser armazenados em uma varíavel e exibidos
        na operação de Extrato.
- Extrato
    * Listar todos os depósitos e saques realizados na conta;
    * Exibir saldo atual no final da listagem;
    * Exibir valores no formato "R$ xxx.xx".
'''

# Define the menu string to display available bank operations
menu = '''
=== BANCO LOREM IPSUM ===

      Depositar [d]
      Sacar     [s]
      Extrato   [e]
      Sair      [q]

Digite a letra correspondente à Operação desejada.
=> '''

# Initialize the account balance, withdrawal limit, transaction history, and daily withdrawal count
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

# Main loop to handle user operations
while True:
    # Get user input for the operation they want to perform
    opcao = input(menu)

    # Deposit operation
    if opcao == "d":
        # Initialize deposit amount
        deposito = 0
        
        # Display deposit header
        print("\n\n {:^30}".format("DEPÓSITO") + f"\n{'='*30}")
        # Get deposit amount from user
        deposito = float(input("Digite o valor do Depósito: "))
        # Validate deposit amount
        if deposito <= 0:
            print("ERRO: Valor Inválido! Digite um valor positivo.")
        
        else:
            # Update account balance and transaction history
            saldo += deposito
            extrato = extrato + (f'Depósito: R$ {deposito:.2f} \n')
            print("Operação Realizada com Sucesso!")
    
    # Withdrawal operation
    elif opcao == "s":
        saque = 0
        numero_saques += 1

        # Display withdrawal header
        print("\n\n {:^30}".format("SAQUE") + f"\n{'='*30}")
        
        # Check if the number of withdrawals has reached the limit
        if numero_saques > LIMITE_SAQUES:
            print("Alerta: Número de SAQUES DIÁRIOS já atingiu o limite!")

        else:
            # Get withdrawal amount from user
            saque = float(input("Digite o valor do saque: "))
            # Validate withdrawal amount
            if saque > 500:
                print(f"ERRO: Valor de saque por operação excedido! Digite um valor de até R${limite}.")
                numero_saques -= 1

            elif saque > saldo:
                print("ERRO: SALDO insuficiente!")
                numero_saques -= 1

            elif saque <= 0:    
                print(f"ERRO: Valor Inválido! Digite um valor positivo.")
                numero_saques -= 1
        
            else:
                # Update account balance and transaction history
                saldo -= saque
                extrato = extrato + (f'Saque: R$ {saque:.2f} \n')
                print("Operação Realizada com Sucesso!")
                
    # Display account statement
    elif opcao == "e":
        print("\n\n {:^20}".format("Extrato") + f"\n{20*'='}")
        print(f"{extrato}{20*'='}\n Saldo: R$ {saldo:.2f}")

    # Exit the program
    elif opcao == "q":
        print("Obrigado por ser nosso cliente!")
        break

    # Invalid operation
    else:
        print("Operação INVÁLIDA! Por favor selecione novamente a operação desejada ")
