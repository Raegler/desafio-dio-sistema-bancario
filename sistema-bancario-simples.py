class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_diarios = 0
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite diário de saques atingido!")
        elif valor > 500:
            print("Valor máximo por saque é R$500.00")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.transacoes.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        print("\nExtrato:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_diarios}\n")

def menu():
    conta = ContaBancaria()
    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: R$"))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: R$"))
            conta.sacar(valor)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o menu
menu()
