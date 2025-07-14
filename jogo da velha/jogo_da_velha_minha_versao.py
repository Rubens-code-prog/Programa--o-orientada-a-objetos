import os

class jogador1:
    def __init__(self):
        pass

    def jogada(self):
        movimento = input('Selecione sua casa. ')
        return movimento


class jogador2:
    def __init__(self):
        pass
    
    def jogada(self):
        movimento = input('Selecione sua casa. ')
        return movimento

class tabuleiro:
    def __init__(self, jogador1, jogador2):
        self.linha1 = {
        'a1': ' ', 'a4': '|', 'a2': ' ', 'a5': '|', 'a3': ' ',
        }
        self.linha2 = {
        'n': '-----'
        }
        self.linha3 = {
        'b1': ' ', 'b4': '|', 'b2': ' ', 'b5': '|', 'b3': ' ',
        }
        self.linha4 = {
        'n': '-----'
        }
        self.linha5 = {
        'c1': ' ', 'c4': '|', 'c2': ' ', 'c5': '|', 'c3': ' '
        }
        self.tabuleiro = [self.linha1, self.linha2, self.linha3, self.linha4, self.linha5]
        self.mostrar_tabuleiro()
        
    def mostrar_tabuleiro(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for linha in self.tabuleiro:
            linha_tela = ''.join(linha.values())
            print(linha_tela)
    
    def jogo(self):
        while True:
            movimento2 = jogador2.jogada()
            if movimento2 in self.linha1.keys():
                self.linha1[movimento2] = 'X'
            elif movimento2 in self.linha3.keys():
                self.linha3[movimento2] = 'X'
            elif movimento2 in self.linha5.keys():
                self.linha5[movimento2] = 'X'
            tabuleiro.mostrar_tabuleiro()
            movimento2 = jogador2.jogada()
            if movimento2 in self.linha1.keys():
                self.linha1[movimento2] = 'O'
            elif movimento2 in self.linha3.keys():
                self.linha3[movimento2] = 'O'
            elif movimento2 in self.linha5.keys():
                self.linha5[movimento2] = 'O'
            tabuleiro.mostrar_tabuleiro()
        
jogador1 = jogador1()
jogador2 = jogador2()
tabuleiro = tabuleiro(jogador1, jogador2)
tabuleiro.jogo()