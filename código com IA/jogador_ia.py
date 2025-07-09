# -*- coding: utf-8 -*-
from random import randint
from typing import Optional, Tuple
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int) -> None:
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> Optional[Tuple[int, int]]:
        tipo = self.tipo
        oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        def livre(i: int, j: int) -> bool:
            return self.matriz[i][j] == Tabuleiro.DESCONHECIDO

        for jogador in (tipo, oponente):
            for i in range(3):
                linha = self.matriz[i]
                if linha.count(jogador) == 2 and linha.count(Tabuleiro.DESCONHECIDO) == 1:
                    return (i, linha.index(Tabuleiro.DESCONHECIDO))
                col = [self.matriz[0][i], self.matriz[1][i], self.matriz[2][i]]
                if col.count(jogador) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                    return (col.index(Tabuleiro.DESCONHECIDO), i)

            diag1 = [self.matriz[i][i] for i in range(3)]
            diag2 = [self.matriz[i][2 - i] for i in range(3)]

            if diag1.count(jogador) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
                idx = diag1.index(Tabuleiro.DESCONHECIDO)
                return (idx, idx)

            if diag2.count(jogador) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
                idx = diag2.index(Tabuleiro.DESCONHECIDO)
                return (idx, 2 - idx)

        def conta_jogadas_vencedoras(simulador: list[list[int]], jogador: int) -> int:
            total = 0
            for i in range(3):
                if simulador[i].count(jogador) == 2 and simulador[i].count(Tabuleiro.DESCONHECIDO) == 1:
                    total += 1
                col = [simulador[0][i], simulador[1][i], simulador[2][i]]
                if col.count(jogador) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                    total += 1
            diag1 = [simulador[i][i] for i in range(3)]
            diag2 = [simulador[i][2 - i] for i in range(3)]
            if diag1.count(jogador) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
                total += 1
            if diag2.count(jogador) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
                total += 1
            return total

        for i in range(3):
            for j in range(3):
                if livre(i, j):
                    copia = [linha[:] for linha in self.matriz]
                    copia[i][j] = tipo
                    if conta_jogadas_vencedoras(copia, tipo) >= 2:
                        return (i, j)

        if livre(1, 1):
            return (1, 1)

        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = {(0, 0): (2, 2), (2, 2): (0, 0), (0, 2): (2, 0), (2, 0): (0, 2)}
        for canto in cantos:
            i, j = canto
            if self.matriz[i][j] == oponente:
                op = opostos[canto]
                if livre(*op):
                    return op
                
        for canto in cantos:
            if livre(*canto):
                return canto

        livres: list[Tuple[int, int]] = [(i, j) for i in range(3) for j in range(3) if livre(i, j)]
        if livres:
            return livres[randint(0, len(livres) - 1)]

        return None
