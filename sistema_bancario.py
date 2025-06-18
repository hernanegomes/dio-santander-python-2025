menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
       deposito = float(input("Informe o valor do depósito: "))

       if deposito > 0:
           saldo += deposito
           extrato += f"Depósito: R${deposito:.2f}\n"

    elif opcao == "s":
        if numero_saques < 4:
            saque =  float(input("Informe o valor de saque: "))

            if saldo < saque:
                print("Saldo insuficiente.")
            
            else:
                if saque > 500:
                    print("Limite de saque diário foi ultrapassado.")

                else:
                    saldo -= saque
                    numero_saques -= 1
                    extrato += f"Saque: R${saque:.2f}\n"

        
        else:
            print("Quantidade de saques diários foi ultrapassado.")



    elif opcao == "e":
        print('=' * 15, ' Extrato ', '=' * 15)
        if extrato == '':
            print('Não foram realizadas movimentações.')
        
        else:
            print(extrato)
            print('=' * 16, ' Saldo ', '=' * 16)
            print(f'Saldo: R${saldo:.2f}')
        
        print('=' * 41)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")