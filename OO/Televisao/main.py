#Classe
class TV:

    #Instância
    def __init__(self, tamanho):
        # Self . Atibuto = Valor Inicial
        self.cor = 'Preta'
        self.ligado = False
        self.tamanho = tamanho
        self.canal = 'Combate'
    
    def mudar_canal (self, novo_canal):
        self.canal = novo_canal



#TV Sala HERDA todos os atributos da classe TV, mas é possivel alterar esses atributos

tv_sala = TV(55)

tv_quarto = TV(70)


print(tv_sala.tamanho)
print(tv_quarto.tamanho)