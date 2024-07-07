

print("\n\nSeja Bem Vindo ao Banco da Má Vontade use nosso menu para a opção que melhor lhe atende. ")

LISTA_SALDO = []
saldo = sum(LISTA_SALDO)

LimiteDiario = 3
Limite = 500
LISTA_SAQUE = []


def extrato():
    global saldo

    if not LISTA_SALDO and not LISTA_SAQUE:
        print("Não houve nenhum depósito ou saque na conta durante esta sessão.\n\n")
    else:
        for Saldostring in LISTA_SALDO:
            print(f"Depósito: R${Saldostring:.2f}")
        for Saquestring in LISTA_SAQUE:
            print(f"Saque: R${Saquestring:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

    Menu()


def saqueF():
    global LimiteDiario
    global saldo
    global Limite

    try:
        qntsaque = float(input(
            "Digite a quantidade que deseja sacar (limite máximo de R$500,00 por saque):\n"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    if qntsaque > saldo:
        print("Quantidade do saque excede o saldo\n\nAcessando menu novamente...\n")
        Menu()
        return

    if qntsaque > Limite:
        print("Saque solicitado excede o limite de R$500, acessando menu novamente...")
        Menu()
        return

    saldo -= qntsaque
    print("Saque realizado com sucesso, por favor retire o dinheiro.")
    LISTA_SAQUE.append(qntsaque)

    escolha = input("Deseja fazer mais um saque?(S / N)\n").upper()

    if LimiteDiario > 0 and escolha == "S":
        LimiteDiario -= 1
        saqueF()
    else:
        Menu()


def deposito():
    global saldo
    global LISTA_SALDO
    try:
        depositar = float(input("Digite a quantia que deseja depositar.\n"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.\n\n")
        deposito()
    LISTA_SALDO.append(depositar)
    saldo = sum(LISTA_SALDO)
    escolha = input("Deseja fazer mais um depósito?(S / N)\n").upper()

    if (escolha == "S"):
        deposito()
    else:
        Menu()


def Menu():
    print("\nMenu:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        deposito()
    elif escolha == 2:
        saqueF()
    elif escolha == 3:
        extrato()
    elif escolha == 4:
        print("Saindo...")
    else:
        print("Opção inválida!")
        Menu()


Menu()
