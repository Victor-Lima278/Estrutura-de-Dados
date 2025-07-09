import pygame
import buttons as bt
from typing import List

class TabuleiroScreen:
    def __init__(self) -> None:
        self.resultado_txt: str = ""
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        screen.fill((255, 255, 255))                
        self.screen: pygame.Surface = screen
        self.buttons: List[List[bt.Button]] = [[], [], []]
         
        for l in range(3):
            y = 50 + l * 200
            for c in range(3):
                x = 50 + c * 200
                self.buttons[l].append(bt.Button(self.screen, (x, y), (200, 200)))
        
        self.desenha_tabuleiro()
         
    def wait_quit_event(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 
         
    def desenha_tabuleiro(self) -> None:
        bt.buttons_v.update()
        bt.buttons_v.draw(self.screen)
        
        pygame.draw.line(self.screen, (0, 0, 0), (250, 50), (250, 650), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (450, 50), (450, 650), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (50, 250), (650, 250), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (50, 450), (650, 450), 5)
        
        font = pygame.font.SysFont("Arial", 40)
        text_render = font.render(self.resultado_txt, True, "black")
        self.screen.blit(text_render, (270, 5))
        
        pygame.display.update()
        
    def update_text_button(self, x: int, y: int, player: int) -> None:
        b = self.buttons[x][y]
        b.change_text(player)
