from datetime import datetime
import pytz


class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
    
    def consultar_saldo(self):
        print('Seu saldo é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    # _ MÉTODO PRIVADO, SÓ PODE SER VISTO DENTRO DA CLASSE CONTA CORRENTE
    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não possui saldo suficiente")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    
    def consultar_limite(self):
        print("Seu limite de conta é R${:,.2f}".format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        print("Valor, Saldo, Data e Hora")
        for transacao in self.transacoes:
            print(transacao)

#Programa
conta_Lira = ContaCorrente("Lira", "436.881.198-43", 1234, 34062)

print(conta_Lira.nome)
print(conta_Lira.cpf)

#Consultando
conta_Lira.consultar_saldo()

#Despositando
conta_Lira.depositar(10)

#Sacando
conta_Lira.sacar(150)

#Consultando
print("Saldo Final")
conta_Lira.consultar_saldo()


print(conta_Lira.transacoes)

conta_Lira.consultar_historico_transacoes()