from argparse import ArgumentDefaultsHelpFormatter
from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa Abaixo do nivel recomendado: {}'.format(self.caixa))
        else:
            print('O valor de caixa está OK {}'. format(self.caixa))
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Emprestimo de {}'.format(valor))
        else:
            print('Empréstimo Negado')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        self.telefone = telefone
        self.cnpj = cnpj
        #Chamando o init da super class
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor


    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001, 9999))
        self.caixa = 20000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            #usando o metodo da superclasse para não repetir código
            super().adicionar_cliente(nome, cpf, patrimonio)

        else:
           raise ValueError('O cliente não possui patrimonio mínimo necessário para ser Premium')

if __name__ == '__main__':

    agencia1 = Agencia(22222, 123456789, 1234)

    agencia_virtual = AgenciaVirtual('www.ag.com', 123, 1313)

    agencia_virtual.verificar_caixa()

    print(agencia_virtual.site)

    agencia_virtual.depositar_paypal(50000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)


    agencia_comum = AgenciaComum (12331, 465464)


    # agencia_comum.verificar_caixa()

    agencia_premium = AgenciaPremium(789987, 98797)

    #agencia_premium.verificar_caixa()

    agencia_premium.adicionar_cliente('Lira', 123, 5044444440)