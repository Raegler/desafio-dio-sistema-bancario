class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None

    def vincular_conta(self, conta_corrente):
        self.conta = conta_corrente


class ContaCorrente:
    def __init__(self, usuario):
        self.usuario = usuario
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


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self, nome, cpf):
        usuario = Usuario(nome, cpf)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} criado com sucesso!")
        return usuario

    def criar_conta_corrente(self, usuario):
        conta_corrente = ContaCorrente(usuario)
        usuario.vincular_conta(conta_corrente)
        self.contas.append(conta_corrente)
        print(f"Conta corrente criada com sucesso para o usuário {usuario.nome}!")

    def encontrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def menu(self):
        while True:
            print("\nMenu do Banco:")
            print("1. Criar Usuário")
            print("2. Criar Conta Corrente")
            print("3. Acessar Conta Corrente")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do usuário: ")
                cpf = input("Digite o CPF do usuário: ")
                self.criar_usuario(nome, cpf)

            elif opcao == "2":
                cpf = input("Digite o CPF do usuário para criar a conta: ")
                usuario = self.encontrar_usuario_por_cpf(cpf)
                if usuario:
                    self.criar_conta_corrente(usuario)
                else:
                    print("Usuário não encontrado!")

            elif opcao == "3":
                cpf = input("Digite o CPF do usuário para acessar a conta: ")
                usuario = self.encontrar_usuario_por_cpf(cpf)
                if usuario and usuario.conta:
                    conta = usuario.conta
                    while True:
                        print("\nMenu da Conta Corrente:")
                        print("1. Depositar")
                        print("2. Sacar")
                        print("3. Extrato")
                        print("4. Voltar ao Menu Principal")
                        
                        opcao_conta = input("Escolha uma opção: ")

                        if opcao_conta == "1":
                            valor = float(input("Digite o valor para depósito: R$"))
                            conta.depositar(valor)
                        elif opcao_conta == "2":
                            valor = float(input("Digite o valor para saque: R$"))
                            conta.sacar(valor)
                        elif opcao_conta == "3":
                            conta.extrato()
                        elif opcao_conta == "4":
                            break
                        else:
                            print("Opção inválida! Tente novamente.")
                else:
                    print("Usuário não encontrado ou conta não criada!")

            elif opcao == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Inicia o banco e o menu
banco = Banco()
banco.menu()
