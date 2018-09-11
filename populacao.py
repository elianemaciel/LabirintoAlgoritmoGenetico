# -*- coding: utf-8 -*-
import random
from labirinto import Agent, gera_labirinto

labirinto = gera_labirinto()

class Individuo():

    genes = ""
    aptidao = 0

    def __init__(self, num_genes=0, genes=""):
        from algoritmo import algoritmo
        self.genes = genes
        caracteres = algoritmo.caracteres

        if num_genes:
            self.genes += "00"
            for gene in range(num_genes - 2 ):
                pos = random.randint(0, 3)
                self.genes += caracteres[pos]

        elif genes:
            # se for mutar, cria um gene aleatório
            if random.uniform(0.0, 1.0) <= algoritmo.taxa_mutacao:
                caracteres = algoritmo.caracteres
                gene_novo = ""
                pos_aleatoria = random.randint(0, len(genes))
                for i in range(len(genes)):
                    if (i==pos_aleatoria):
                        gene_novo += caracteres[random.randint(0, 3)]
                    else:
                        gene_novo += genes[i]

                self.genes = gene_novo
        self.gera_aptidao()

    def gera_aptidao(self):
        from algoritmo import algoritmo
        global labirinto

        solucao = algoritmo.solucao
        self.aptidao = 0

        agent = Agent(labirinto.get_posicao_labirinto(9, 0))

        for i in range(0, solucao, 2):
            self.aptidao += 1
            if (self.genes[i:i+2]) == "00":
                if agent.no.get_parede_direita():
                    self.aptidao -= 10
                if not agent.move_direita(labirinto):
                    break
            elif (self.genes[i:i+2]) == "01":
                if agent.no.get_parede_acima():
                    self.aptidao -= 10
                if not agent.move_cima(labirinto):
                    break
            elif (self.genes[i:i+2]) == "10":
                if agent.no.get_parede_esquerda():
                    self.aptidao -= 10
                if not agent.move_esquerda(labirinto):
                    break
            elif (self.genes[i:i+2]) == "11":
                if agent.no.get_parede_baixo():
                    self.aptidao -= 10
                if not agent.move_baixo(labirinto):
                    break
        return self.aptidao

    def verifica_individuo(self):
        global labirinto
        from algoritmo import algoritmo
        solucao = algoritmo.solucao

        agent = Agent(labirinto.get_posicao_labirinto(9, 0))

        for i in range(0, solucao, 2):
            if (self.genes[i:i+2]) == "00":
                if agent.no.get_parede_direita():
                    return False
                if not agent.move_direita(labirinto):
                    return False
            elif (self.genes[i:i+2]) == "01":
                if agent.no.get_parede_acima():
                    return False
                if not agent.move_cima(labirinto):
                    return False
            elif (self.genes[i:i+2]) == "10":
                if agent.no.get_parede_esquerda():
                    return False
                if not agent.move_esquerda(labirinto):
                    return False
            elif (self.genes[i:i+2]) == "11":
                if agent.no.get_parede_baixo():
                    return False
                if not agent.move_baixo(labirinto):
                    return False
        return True

    def get_genes(self):
        return self.genes


class Populacao():

    individuos = []
    tam_populacao = 0

    # cria uma população com indivíduos aleatória
    def __init__(self, num_genes="", tam_pop=100):
        self.tam_populacao = tam_pop
        self.individuos = []

        if num_genes:
            for i in range(tam_pop):
                self.individuos.append(Individuo(num_genes=num_genes))
        else:
            for i in range(tam_pop):
                self.individuos.append(None)

    # coloca um indivíduo em uma certa posição da população
    def set_individuo(self, individuo, posicao=""):
        if posicao:
            self.individuos[posicao] = individuo
        else:
            for i in range(len(self.individuos)):
                if (self.individuos[i] == None):
                    self.individuos[i] = individuo
                    return

    # verifica se algum indivíduo da população possui a solução
    def tem_solucao(self):
        for individuo in self.individuos:
            if individuo.verifica_individuo():
                return True

        return False

    # ordena a população pelo valor de aptidão de cada indivíduo, do maior valor para o menor, assim se eu quiser obter o melhor indivíduo desta população, acesso a posição 0 do array de indivíduos
    def ordena_populacao(self):
        self.individuos = sorted(self.individuos, key=lambda x: x.aptidao, reverse=False)

    # número de indivíduos existentes na população
    def get_num_individuos(self):
        num = 0
        for i in range(len(self.individuos)):
            if (self.individuos[i]):
                num += 1
        return num

    def get_tam_populacao(self):
        return self.tam_populacao

    def get_individuo(self, pos):
        return self.individuos[pos]
