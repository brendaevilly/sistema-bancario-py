import random
from datetime import datetime

class Conta():

    contas = {}

    #construtor
    def __init__(self, nomeTitular, saldo=0):
        self._nomeTitular = nomeTitular
        self._numeroConta = self.gerarNumeroUnicoParaConta()
        self._saldo = saldo
        self.historico = {"dataCriacao": datetime.now(),
                          "transacoes": []}
        Conta.contas[self._numeroConta] = self
    
    #gets e sets: _nomeTitular
    @property
    def nomeTitular(self):
        return self._nomeTitular
    @nomeTitular.setter
    def nomeTitular(self, nome):
        self._nomeTitular = nome

    #gets e sets: _numeroConta
    @property
    def numeroConta(self):
        return self._numeroConta
    @numeroConta.setter
    def numeroConta(self, numero):
        self._numeroConta = numero

    #gets e sets: _saldo
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, novoSaldo):
        self._saldo = novoSaldo

    #métodos
    def gerarNumeroUnicoParaConta(self):
        numero = random.randint(100, 999)
        while numero in Conta.contas:
            numero = random.randint(100, 999)
        return numero

    @classmethod
    def listarContas(cls):
        for numero, conta in Conta.contas.items():
            print(f"Conta: {numero}")
            print(f"Titular: {conta.nomeTitular}")
            print(f"Saldo: ${conta.saldo}")

    @classmethod
    def sacarValor(cls, numConta, valor):
        cls.listarContas()
        if numConta in Conta.contas:
            c = Conta.contas[numConta]
            if valor > 0 and valor <= c.saldo:
                c.saldo -= valor
                c.historico["transacoes"].append(f"Saque: ${valor:.2f}")
                return f"Saque de ${valor:.2f} realizado com sucesso."
            else:
                return "[ERRO] Saldo insuficiente." 
        else:
            return "Não existe nenhuma conta registrada com esse número."

    @classmethod
    def depositarValor(cls, numConta, valor):
        cls.listarContas()
        if numConta in Conta.contas:
            c = Conta.contas[numConta]
            if valor > 0:
                c.saldo += valor
                c.historico["transacoes"].append(f"Depósito: ${valor:.2f}")
                return f"Depósito de ${valor:.2f} realizado com sucesso."
            else:
                return "[ERRO] Valor inválido para depósito." 
        else:
            return "Não existe nenhuma conta registrada com esse número."

    @classmethod
    def transferirValor(cls, numContaOrigem, numContaDestino, valor):
        cls.listarContas()
        if numContaOrigem not in Conta.contas:
            return "[ERRO] Conta de origem não encontrada."
        if numContaDestino not in Conta.contas:
            return "[ERRO] Conta de destino não encontrada."
        if valor <= 0:
            return "[ERRO] Valor inválido para transferência."
        c1 = Conta.contas[numContaOrigem]
        c2 = Conta.contas[numContaDestino]
        if valor > c1.saldo:
            return "[ERRO] Saldo insuficiente para transferência."
        c1.saldo -= valor
        c2.saldo += valor
        c1.historico["transacoes"].append(f"Fez transferência de ${valor:.2f} para a conta {numContaDestino}")
        c2.historico["transacoes"].append(f"Recebeu transferência de ${valor:.2f} da conta {numContaOrigem}")
        return f"Transferência de ${valor:.2f} realizada com sucesso."
    
    @classmethod
    def excluirConta(cls, numConta):
        if numConta in Conta.contas:
            del Conta.contas[numConta]
        else:
            print("Não existe nenhuma conta registrada com esse número.")

    @classmethod
    def imprimirHistorico(cls, numero):
        if numero in Conta.contas:
            c = Conta.contas[numero]
            print("HISTÓRICO:")
            print(f"Data de criação: {c.historico['dataCriacao']}")
            if c.historico["transacoes"]:
                for transacao in c.historico["transacoes"]:
                    print(f"    - {transacao}")
            else:
                print("Nenhuma transação foi registrada nessa conta.")
        else:
            print("Não existe nenhuma conta registrada com esse número.")

def menu():
    return "------ MENU ------\n1. Criar conta\n2. Listar contas\n3. Sacar valor\n4. Depositar valor\n5. Transferir valor\n6. Excluir conta\n7. Imprimir histórico\n8. Sair"

#main ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    print(menu())
    op = input("Opcão: ")
    while op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6' and op != '7' and op != '8':
        print("[ERRO] Opção inválida!")
        op = input("Opcão: ")

    if op == '1':
        titular = input("Nome do titular da conta: ")
        c = Conta(titular)
        print("Conta criada!")
    elif op == '2':
        Conta.listarContas()
    elif op == '3':
        num = input("Insira o número da conta: ")
        try:
            num = int(num)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
        val = input("Insira o valor do saque: ")
        try:
            val = float(val)
            print(Conta.sacarValor(num, val))
        except ValueError:
            print("[ERRO] Valor inválido para saque.")
    elif op == '4':
        num = input("Insira o número da conta: ")
        try:
            num = int(num)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
        val = input("Insira o valor do depósito: ")
        try:
            val = float(val)
            print(Conta.depositarValor(num, val))
        except ValueError:
            print("[ERRO] Valor inválido para depósito.")
    elif op == '5':
        numOri = input("Insira o número da conta de origem: ")
        try:
            numOri = int(numOri)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
        numDest = input("Insira o número da conta de destino: ")
        try:
            numDest = int(numDest)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
        val = input("Insira o valor da transferência: ")
        try:
            val = float(val)
            print(Conta.transferirValor(numOri, numDest, val))
        except ValueError:
            print("[ERRO] Valor inválido para transferência.")
    elif op == '6':
        num = input("Insira o número da conta: ")
        try:
            num = int(num)
            Conta.excluirConta(num)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
    elif op == '7':
        num = input("Insira o número da conta: ")
        try:
            num = int(num)
            Conta.imprimirHistorico(num)
        except ValueError:
            print("[ERRO] Número da conta inválido.")
    else:
        print("Finalizando programa...")
        break
