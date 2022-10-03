from turtle import *

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Retangulo():
    def __init__(self, ponto_inicio, ponto_fim):
        self.ponto_inicio_x, self.ponto_inicio_y = ponto_inicio
        self.ponto_fim_x, self.ponto_fim_y = ponto_fim

        self.largura = 0
        self.altura = 0

    def encontra_largura_altura(self):
        self.largura =  self.ponto_fim_x - self.ponto_inicio_x
        self.altura =   self.ponto_fim_y - self.ponto_inicio_y
        return print(f'Largura: {self.largura}. \nAltura: {self.altura}.')

    def encontra_coordenada_ponto_central(self):
        x =  self.largura /2
        y =  self.altura /2
        return print(f'Coordenada Central x: {x + self.ponto_inicio_x}. \nCoordenada Central y: {y + self.ponto_inicio_y}.')

    def desenha_retangulo(self):
        forward(self.largura)
        right(90)
        forward(self.altura)
        right(90)
        forward(self.largura)
        right(90)
        forward(self.altura)
        right(90)
        done()

coordenada_ponto_inicial = [ -123, -352 ]
coordenada_ponto_final = [ 115,  -114 ] 
retangulo = Retangulo( coordenada_ponto_inicial, coordenada_ponto_final )
retangulo.encontra_largura_altura()
retangulo.encontra_coordenada_ponto_central()
retangulo.desenha_retangulo()

