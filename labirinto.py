
class Labirinto():
    posicoes = []
    tamanho = 10

    def __init__(self, posicoes=[], tamanho=10):
        self.posicoes = posicoes
        self.tamanho = tamanho

    def get_posicao_labirinto(self, pos1, pos2):

        for i in range(10):
            for j in range(10):
                if self.posicoes[i][j].pos1 == pos1 and self.posicoes[i][j].pos2 == pos2:
                    return self.posicoes[i][j]

    def set_labirinto(self, lista_labirinto):
        self.posicoes.append(lista_labirinto)

    def set_paredes(self, posA, posB):
        noA = self.get_posicao_labirinto(posA[0], posA[1])
        noB = self.get_posicao_labirinto(posB[0], posB[1])
        noA.set_parede(noB)
        noB.set_parede(noA)

    def desenha_labirinto(self):
        for i in range(10):
            linha2 = ""
            for j in range(10):
                linha = ""
                if self.posicoes[i][j].get_parede_esquerda():
                    linha += "#"
                else:
                    linha += "|"
                linha += " " + self.posicoes[i][j].conteudo + " "
                print(linha, end="")

                if self.posicoes[i][j].get_parede_baixo():
                    linha2 += " =="
                else:
                    linha2 += " --"
            print("\n" + linha2)


class NoLabirinto():
    parede = []
    pos1 = ""
    pos2 = ""
    conteudo = ""

    def __init__(self, parede=[], pos1=0, pos2=0, conteudo=""):
        self.parede = parede
        self.pos1 = pos1
        self.pos2 = pos2
        self.conteudo = conteudo

    def set_parede(self, no_labirinto):
        self.parede.append(no_labirinto)

    def verifica_parede(self, no):
        if no in self.parede:
            return True
        return False

    def get_parede_direita(self):
        for no in self.parede:
            if no.pos1 == self.pos1 and no.pos2 > self.pos2:
                return True
        return False

    def get_parede_esquerda(self):
        for no in self.parede:
            if no.pos1 == self.pos1 and no.pos2 < self.pos2:
                return True
        return False

    def get_parede_acima(self):
        for no in self.parede:
            if no.pos1 < self.pos1 and no.pos2 == self.pos2:
                return True
        return False

    def get_parede_baixo(self):
        for no in self.parede:
            if no.pos1 > self.pos1 and no.pos2 == self.pos2:
                return True
        return False

    def set_conteudo(self, conteudo='-'):
        self.conteudo = conteudo


class Agent():
    no = None

    def __init__(self, no=None):
        self.no = no

    def move_direita(self, labirinto):
        pos = self.no.pos2 + 1
        if pos <= 9:
            no = labirinto.get_posicao_labirinto(self.no.pos1, pos)
            self.no = no
            self.no.set_conteudo("-")
            return True
        return False

    def move_esquerda(self, labirinto):
        pos = self.no.pos2 - 1
        if pos > 0:
            no = labirinto.get_posicao_labirinto(self.no.pos1, pos)
            self.no = no
            self.no.set_conteudo("-")
            return True
        return False

    def move_baixo(self, labirinto):
        pos = self.no.pos1 + 1
        if pos <= 9:
            no = labirinto.get_posicao_labirinto(pos, self.no.pos2)
            self.no = no
            self.no.set_conteudo("-")
            return True
        return False

    def move_cima(self, labirinto):
        pos = self.no.pos1 - 1
        if pos > 0:
            no = labirinto.get_posicao_labirinto(pos, self.no.pos2)
            self.no = no
            self.no.set_conteudo("-")
            return True
        return False

def gera_labirinto():
    labirinto = Labirinto(tamanho=10)
    lista = []
    for i in range(10):
        lista = []
        for j in range(10):
            lista.append(NoLabirinto(parede=[], pos1=i, pos2=j))
        labirinto.set_labirinto(lista)

    labirinto.set_paredes((0, 4),(0, 5))
    labirinto.set_paredes((0, 8),(0, 9))
    labirinto.set_paredes((0, 1),(1, 1))
    labirinto.set_paredes((0, 2),(1, 2))
    labirinto.set_paredes((0, 3),(1, 3))
    labirinto.set_paredes((0, 6),(1, 6))
    labirinto.set_paredes((0, 7),(1, 7))
    labirinto.set_paredes((1, 0),(1, 1))
    labirinto.set_paredes((1, 4),(1, 5))
    labirinto.set_paredes((1, 5),(1, 5))
    labirinto.set_paredes((1, 7),(1, 8))
    labirinto.set_paredes((1, 1),(2, 1))
    labirinto.set_paredes((1, 2),(2, 2))
    labirinto.set_paredes((1, 3),(2, 3))
    labirinto.set_paredes((1, 4),(2, 4))
    labirinto.set_paredes((1, 8),(2, 8))
    labirinto.set_paredes((1, 9),(2, 9))
    labirinto.set_paredes((2, 1),(3, 1))
    labirinto.set_paredes((2, 2),(3, 2))
    labirinto.set_paredes((2, 3),(3, 3))
    labirinto.set_paredes((2, 4),(3, 4))
    labirinto.set_paredes((2, 5),(2, 6))
    labirinto.set_paredes((2, 6),(2, 7))
    labirinto.set_paredes((2, 6),(3, 6))
    labirinto.set_paredes((2, 8),(3, 8))
    labirinto.set_paredes((3, 0),(4, 0))
    labirinto.set_paredes((3, 1),(4, 1))
    labirinto.set_paredes((3, 2),(4, 2))
    labirinto.set_paredes((3, 3),(3, 4))
    labirinto.set_paredes((3, 4),(4, 4))
    labirinto.set_paredes((3, 5),(4, 5))
    labirinto.set_paredes((3, 6),(4, 6))
    labirinto.set_paredes((3, 7),(4, 7))
    labirinto.set_paredes((3, 7),(3, 8))
    labirinto.set_paredes((3, 8),(3, 9))
    labirinto.set_paredes((4, 1),(4, 2))
    labirinto.set_paredes((4, 1),(5, 1))
    labirinto.set_paredes((4, 4),(5, 4))
    labirinto.set_paredes((4, 5),(5, 5))
    labirinto.set_paredes((4, 6),(5, 6))
    labirinto.set_paredes((4, 7),(5, 7))
    labirinto.set_paredes((4, 8),(5, 8))
    labirinto.set_paredes((4, 9),(5, 9))
    labirinto.set_paredes((4, 8),(4, 9))
    labirinto.set_paredes((5, 0),(6, 0))
    labirinto.set_paredes((5, 1),(6, 1))
    labirinto.set_paredes((5, 2),(5, 3))
    labirinto.set_paredes((5, 4),(6, 4))
    labirinto.set_paredes((5, 5),(6, 5))
    labirinto.set_paredes((5, 6),(6, 6))
    labirinto.set_paredes((5, 7),(6, 7))
    labirinto.set_paredes((5, 8),(6, 8))
    labirinto.set_paredes((5, 4),(6, 4))
    labirinto.set_paredes((6, 1),(7, 1))
    labirinto.set_paredes((6, 2),(7, 2))
    labirinto.set_paredes((6, 2),(6, 3))
    labirinto.set_paredes((6, 3),(6, 4))
    labirinto.set_paredes((6, 4),(7, 4))
    labirinto.set_paredes((6, 6),(6, 7))
    labirinto.set_paredes((6, 4),(7, 4))
    labirinto.set_paredes((6, 8),(7, 8))
    labirinto.set_paredes((6, 9),(7, 9))
    labirinto.set_paredes((7, 2),(8, 2))
    labirinto.set_paredes((7, 3),(8, 3))
    labirinto.set_paredes((7, 5),(7, 6))
    labirinto.set_paredes((7, 6),(7, 7))
    labirinto.set_paredes((7, 7),(8, 7))
    labirinto.set_paredes((7, 8),(8, 8))
    labirinto.set_paredes((8, 0),(8, 1))
    labirinto.set_paredes((8, 1),(8, 2))
    labirinto.set_paredes((8, 3),(8, 3))
    labirinto.set_paredes((8, 4),(8, 5))
    labirinto.set_paredes((8, 5),(8, 6))
    labirinto.set_paredes((8, 2),(9, 2))
    labirinto.set_paredes((8, 3),(9, 3))
    labirinto.set_paredes((8, 6),(9, 6))
    labirinto.set_paredes((8, 7),(9, 7))
    labirinto.set_paredes((8, 8),(9, 8))
    labirinto.set_paredes((9, 0),(9, 1))
    labirinto.set_paredes((9, 4),(9, 5))

    return labirinto
