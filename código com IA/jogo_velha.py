from tabuleiro_screen import TabuleiroScreen
from tabuleiro import Tabuleiro
from jogador import Jogador
from jogador_ia import JogadorIA
from jogador_humano import JogadorHumano

class JogoVelha:
    def __init__(self):
        self.screen: TabuleiroScreen = TabuleiroScreen()
        self.tabuleiro: Tabuleiro = Tabuleiro()
        
        # Jogadores
        self.jogadores: list[Jogador] = [
            JogadorIA(self.tabuleiro, Tabuleiro.JOGADOR_0),
            JogadorHumano(self.tabuleiro, self.screen.buttons, Tabuleiro.JOGADOR_X)
        ]
        self.id_jogador_corrente: int = 0
        self.jogador_corrente: Jogador = self.jogadores[self.id_jogador_corrente]
        
    def troca_jogador(self) -> None:
        self.id_jogador_corrente = (self.id_jogador_corrente + 1) % 2
        self.jogador_corrente = self.jogadores[self.id_jogador_corrente]
        
    def wait_quit_event(self) -> None:
        self.screen.wait_quit_event()
    
    def acabou_jogo(self) -> bool:    
        if self.tabuleiro.tem_campeao() == Tabuleiro.JOGADOR_X:
            self.screen.resultado_txt = "X vencedor!"
            return True
        if self.tabuleiro.tem_campeao() == Tabuleiro.JOGADOR_0:
            self.screen.resultado_txt = "0 vencedor!"
            return True
        return False
                              
    def start(self) -> None:
        acabou_jogo: bool = False
        contador: int = 0
        
        while True:
            x, y = self.jogador_corrente.getJogada()
            self.screen.update_text_button(x, y, self.jogador_corrente.tipo)
            self.tabuleiro.matriz[x][y] = self.jogador_corrente.tipo
                                
            contador += 1
            acabou_jogo = self.acabou_jogo()
                                
            if not acabou_jogo and contador == 9:
                self.screen.resultado_txt = "Deu velha!"
                acabou_jogo = True
            
            self.screen.desenha_tabuleiro()
            
            if acabou_jogo:
                break
            
            self.troca_jogador()
