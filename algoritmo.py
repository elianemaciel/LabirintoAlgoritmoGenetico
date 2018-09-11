# -*- coding: utf-8 -*-
from populacao import Populacao, Individuo
import random

class Algoritmo():

    caracteres = []
    solucao = ""
    taxa_crossover = 0.0
    taxa_mutacao = 0.0

    def __init__(self, solucao="", caracteres="", taxa_crossover=0.0, taxa_mutacao=0.0):
        self.caracteres = caracteres
        self.solucao = solucao
        self.taxa_crossover = taxa_crossover
        self.taxa_mutacao = taxa_mutacao

    def nova_geracao(self, populacao, elitismo):
        nova_populacao = Populacao(tam_pop=populacao.get_tam_populacao())

        if (elitismo):
            nova_populacao.set_individuo(populacao.get_individuo(0))

        while (nova_populacao.get_num_individuos() < nova_populacao.get_tam_populacao()):
            pais = self.selecao_torneio(populacao)

            filhos = []

            # verifica a taxa de crossover, se sim realiza o crossover, se não, mantém os pais selecionados para a próxima geração
            if (random.uniform(0.0, 1.0) <= self.taxa_crossover):
                filhos = self.crossover(pais[1], pais[0])
            else:
                filhos.append(Individuo(genes=pais[0].get_genes()))
                filhos.append(Individuo(genes=pais[1].get_genes()))

            # adiciona os filhos na nova geração
            nova_populacao.set_individuo(filhos[0])
            nova_populacao.set_individuo(filhos[1])

        # ordena a nova população
        nova_populacao.ordena_populacao()
        return nova_populacao

    def crossover(self, individuo1, individuo2):
        # sorteia o ponto de corte
        len_genes = int((len(individuo1.get_genes())/2) - 2)
        ponto_corte1 = int(random.randint(0, len_genes) + 1)
        ponto_corte2 = int(random.randint(0, len_genes)) + int(len(individuo1.get_genes())/2)

        filhos = []

        # pega os genes dos pais
        gene_pai1 = individuo1.get_genes()
        gene_pai2 = individuo2.get_genes()

        gene_filho1 = ""
        gene_filho2 = ""

        # realiza o corte,
        gene_filho1 = gene_pai1[0:ponto_corte1]
        gene_filho1 += gene_pai2[ponto_corte1:ponto_corte2]
        gene_filho1 += gene_pai1[ponto_corte2:len(gene_pai1)]

        gene_filho2 = gene_pai2[0:ponto_corte1]
        gene_filho2 += gene_pai1[ponto_corte1:ponto_corte2]
        gene_filho2 += gene_pai2[ponto_corte2:len(gene_pai2)]

        # cria o novo indivíduo com os genes dos pais
        filhos.append(Individuo(genes=gene_filho1))
        filhos.append(Individuo(genes=gene_filho2))

        return filhos

    def selecao_torneio(self, populacao):
        populacao_intermediaria = Populacao(tam_pop=3)

        # seleciona 3 indivíduos aleatóriamente na população
        populacao_intermediaria.set_individuo(
            populacao.get_individuo(random.randint(0, (populacao.get_tam_populacao()-1)))
        )
        populacao_intermediaria.set_individuo(
            populacao.get_individuo(random.randint(0, (populacao.get_tam_populacao()-1)))
        )
        populacao_intermediaria.set_individuo(
            populacao.get_individuo(random.randint(0, (populacao.get_tam_populacao()-1)))
        )

        # ordena a população
        populacao_intermediaria.ordena_populacao()

        pais = []

        # seleciona os 2 melhores deste população
        pais.insert(0, populacao_intermediaria.get_individuo(0))
        pais.insert(1, populacao_intermediaria.get_individuo(1))

        return pais

algoritmo = Algoritmo(
    solucao=(27*2),
    caracteres=["00", "01", "10", "11"],
    taxa_crossover=0.6,
    taxa_mutacao=0.3
)
