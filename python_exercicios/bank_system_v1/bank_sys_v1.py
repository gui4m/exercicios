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

menu = '''

=== BANCO LOREM IPSUM ===

      Depositar [d]
      Sacar     [s]
      Extrato   [e]
      Sair      [q]

Digite a letra correspondente à Operação desejada.
=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = 0
        
        print("\n\n {:^30}".format("DEPÓSITO") + f"\n{'='*30}")
        deposito = float(input("Digite o valor do Depósito: "))
        if deposito <= 0:
            print("ERRO: Valor Inválido! Digite um valor positivo.")
            opcao = "d"
        else:
            saldo += deposito
            extrato = extrato + (f'Depósito: R$ {deposito:.2f} \n')
            print("Operação Realizada com Sucesso!")
    
    elif opcao == "s":
        saque = 0
        numero_saques += 1

        print("\n\n {:^30}".format("SAQUE") + f"\n{'='*30}")
        
        if numero_saques > LIMITE_SAQUES:
            print("Alerta: Número de SAQUES DIÁRIOS já atingiu o limite!")

        else:
            saque = float(input("Digite o valor do saque: "))
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
                saldo -= saque
                extrato = extrato + (f'Saque: R$ {saque:.2f} \n')
                print("Operação Realizada com Sucesso!")
                
    elif opcao == "e":
        print("\n\n {:^20}".format("Extrato") + f"\n{20*'='}")
        print(f"{extrato}{20*'='}\n Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Obrigado por ser nosso cliente!")
        break

    else:
        print("Operação INVÁLIDA! Por favor selecione novamente a operação desejada ")