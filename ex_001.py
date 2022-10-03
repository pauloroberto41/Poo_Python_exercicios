class Cachorro:
    def __init__(self, nome):
        self.nome = nome
        self.estômago = []

    def comer(self, alimento):
        self.alimento = alimento
        print(f"O cachorro {self.nome} comeu: {self.alimento}.")
        self.estômago.append(self.alimento)


    def verEstômago(self):
        if len(self.estômago) <= 0:
            print("Estômago vazio!")
        else:
            estomago = ', '.join(self.estômago)
            print(f"Estômago com: {estomago}.")

    def digerir(self):
        self.estômago = []


cachorro_1 = Cachorro("Dino")
cachorro_2 = Cachorro("Bino")
print("#######")

cachorro_1.verEstômago()
cachorro_2.verEstômago()
cachorro_1.comer('Abóbora')
cachorro_2.comer('Cenoura')
print("#######")
cachorro_1.verEstômago()
cachorro_2.verEstômago()
cachorro_1.comer('Maçã')
cachorro_2.comer('Chuchu')
print("#######")
cachorro_1.verEstômago()
cachorro_2.verEstômago()
cachorro_1.digerir()
cachorro_1.comer('Inhame')
cachorro_2.comer('Brócolis')
print("#######")
cachorro_1.verEstômago()
cachorro_2.verEstômago()