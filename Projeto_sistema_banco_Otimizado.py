#Projeto de sistema bancário - V_01#
def menu():
    menu = """\n 
    ######## MENU ########

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [cc] Cadastrar Conta
    [nu] Novo Usuário
    [lc] Listar Contas do Usuário
    [q]  Sair
    ######################
    """
    return input(menu)
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo +=  valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor informado é inválido")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
                print("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
                print("Operação falhou! Valor solicitado excede o limite.")
    elif excedeu_saques:
                print("Operação falhou! Operação excede os limites de saque.")
                
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falou! Valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n########### Extrato ############")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n######################################")

def criar_usuario(usuarios):
     cpf = input("Infomre o CPF (apenas números): ")
     usuario = filtro_usuario(cpf, usuarios)

     if usuario:
          print("Usuário existente com o CPF informado!")
          return
      
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome, "data_nascimento" :  data_nascimento, "cpf": cpf, "endereco": endereco })

     print(" Usuario criado com sucesso!")

def filtro_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario: 
        print("A conta foi criada com sucesso!")   
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} 
    print("Não foi possível encontrar o usuário, comando de criação de conta encerrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f""" \
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """

        print("="*100)
        

def principal():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Insira o valor a ser depositado:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe valor do saque:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "cc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios) 

             if conta:
                  contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
            
            #excedeu_saldo = valor > saldo
            #excedeu_limite = valor > limite
            #excedeu_saques = numero_saques >= LIMITES_SAQUES

           # if excedeu_saldo:
              #  print("Operação falhou! Saldo insuficiente.")

           # elif excedeu_limite:
              #  print("Operação falhou! Valor solicitado excede o limite.")

           # elif excedeu_saques:
              #  print("Operação falhou! Operação excede os limites de saque.")
                
           # elif valor > 0:
               # saldo -= valor
              #  extrato += f"Saque: R$ {valor:.2f}\n"
               # numero_saques += 1
               # print("Saque realizado com sucesso!")

           # else:
               # print("Operação falou! Valor informado é inválido.")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            print("\n########### Extrato ############")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n######################################")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação.")

principal()