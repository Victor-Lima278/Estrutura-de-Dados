from typing import List

class Tabuleiro:
    DESCONHECIDO: int = 0
    JOGADOR_0: int = 1
    JOGADOR_X: int = 4

    def __init__(self) -> None:
        self.matriz: List[List[int]] = [
            [Tabuleiro.DESCONHECIDO] * 3,
            [Tabuleiro.DESCONHECIDO] * 3,
            [Tabuleiro.DESCONHECIDO] * 3
        ]

    def tem_campeao(self) -> int:

        for linha in self.matriz:
            soma = sum(linha)
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X

        for c in range(3):
            soma = self.matriz[0][c] + self.matriz[1][c] + self.matriz[2][c]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X

        soma = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        elif soma == 12:
            return Tabuleiro.JOGADOR_X

        soma = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        elif soma == 12:
            return Tabuleiro.JOGADOR_X

        return Tabuleiro.DESCONHECIDO
