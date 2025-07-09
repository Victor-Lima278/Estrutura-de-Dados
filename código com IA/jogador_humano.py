# -*- coding: utf-8 -*-
import pygame
from typing import List, Tuple

from jogador import Jogador
from tabuleiro import Tabuleiro
import buttons as bt

class JogadorHumano(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, _buttons: List[List[bt.Button]], tipo: int) -> None:
        super().__init__(tabuleiro, tipo)
        self.buttons: List[List[bt.Button]] = _buttons
      
    def getJogada(self) -> Tuple[int, int]:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
         
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for l in range(3):
                        for c in range(3):
                            b = self.buttons[l][c]
                            if b.rect.collidepoint(pygame.mouse.get_pos()):
                                return (l, c)
