from __future__ import annotations
from typing import Optional, Tuple
from tabuleiro import Tabuleiro

class Jogador:
    def __init__(self, tabuleiro: Tabuleiro, tipo: int) -> None:
        self.matriz: list[list[int]] = tabuleiro.matriz
        self.tabuleiro: Tabuleiro = tabuleiro
        self.tipo: int = tipo

    def getJogada(self) -> Optional[Tuple[int, int]]:
        pass
