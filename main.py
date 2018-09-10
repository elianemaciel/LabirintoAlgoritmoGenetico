# -*- coding: utf-8 -*-

from algoritmo import algoritmo
from populacao import Populacao, Individuo
import random
from labirinto import gera_labirinto
"""
 00 – leste/direita
 01 – norte/cima
 10 – oeste/esquerda
 11 – sul/baixo
"""

def main():
    gera_labirinto()
    eltismo = True
    # tamanho da populacao
    # print(len("000101010000010101000101101010010000000000010100000011000100"))
    # 00010101000001010100010110101001000000000001010000001100010000011010101000110111000001111
    tam_pop = 30
    # numero máximo de geracoes
    num_max_geracoes = 10000

    # define o número de genes do indivíduo baseado na solucao
    num_genes = int(len(algoritmo.solucao)/2)

    # cria a primeira populacao aleatérioa
    populacao = Populacao(num_genes, tam_pop)

    tem_solucao = False
    geracao = 0

    print("Iniciando... Aptidao da solucao: ", len(algoritmo.solucao))

    # loop até o critério de parada
    while (not tem_solucao and geracao < num_max_geracoes):
        geracao += 1

        # cria nova populacao
        populacao = algoritmo.nova_geracao(populacao, eltismo)

        print(
            "Geracao ",
            geracao,
            " | Aptidao: ",
            populacao.get_individuo(0).aptidao,
            " | Melhor: ",
            populacao.get_individuo(0).get_genes()
        )

        # verifica se tem a solucao
        tem_solucao = populacao.tem_solucao(algoritmo.solucao)


    if (geracao == num_max_geracoes):
        print(
            "Número Maximo de Geracoes | ",
            populacao.get_individuo(0).get_genes(),
            " ",
            populacao.get_individuo(0).aptidao
        )


    if (tem_solucao):
        print(
            "Encontrado resultado na geracao ",
            geracao,
            " | ",
            populacao.get_individuo(0).get_genes(),
            " (Aptidão: ",
            populacao.get_individuo(0).aptidao,
            ")"
        )


main()
