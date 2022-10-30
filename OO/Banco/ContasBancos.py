from datetime import datetime
import pytz
from random import randint

class ContaCorrente():

    """
    Docstring Padrão PEP257

    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
    nome (str): Nome do cliente
    cpf (str): CPF do cliente. Deve ser inserido com pontos e traços
    agencia: Agencia resposnável pela conta corrente do cliente
    num_conta: Número da conta corrente do cliente
    saldo: Saldo disponivel na conta do cliente 
    limite: Limite de cheque especial liberado para aquele cliente
    transacoes: Histórico de Transações


    """

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []
    
    #MÉTODO CONSULTAR SALDO
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

    def transferir(self, valor, conta_destino):
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0 , 9), randint(0 , 9), randint(0, 9))
        self.limite = None
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    #Getter
    @property
    def senha(self):
        return self._senha
    
    #Setter
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            raise ValueError("Nova Senha Inválida")

    
