import pygame
import random
import sys
from pygame import gfxdraw

# Inicialização Premium
pygame.init()

# Configurações da Tela
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WORD HUNTER - Edição Dark Blood")

# Sistema de Cores Premium
class Colors:
    BLACK = (10, 10, 15)
    DARK_BLOOD = (40, 0, 0)
    BLOOD_RED = (180, 0, 20)
    LIGHT_BLOOD = (220, 30, 40)
    NEON_RED = (255, 20, 30)
    METALIC = (100, 100, 110)
    SILVER = (200, 200, 210)
    WHITE = (240, 240, 245)
    HIGHLIGHT = (255, 50, 60)

# Efeitos Visuais
def draw_pulse_effect(surface, color, center, max_radius, pulse_speed=0.05):
    time = pygame.time.get_ticks() / 1000
    radius = int(max_radius * 0.8 + max_radius * 0.2 * abs(pygame.math.Vector2.from_polar((1, time * 360 * pulse_speed)).x))
    gfxdraw.filled_circle(surface, center[0], center[1], radius, (*color, 30))

def draw_glow_text(surface, text, font, color, pos, glow_color, intensity=10):
    text_surface = font.render(text, True, color)
    for i in range(1, intensity):
        glow_surf = font.render(text, True, (*glow_color, 5))
        surface.blit(glow_surf, (pos[0] - i, pos[1] - i))
        surface.blit(glow_surf, (pos[0] + i, pos[1] + i))
    surface.blit(text_surface, pos)

# Fontes Premium
try:
    title_font = pygame.font.SysFont("impact", 72)
    main_font = pygame.font.SysFont("arial", 36, bold=True)
    ui_font = pygame.font.SysFont("consolas", 28)
except:
    title_font = pygame.font.SysFont("arial", 72, bold=True)
    main_font = pygame.font.SysFont("arial", 36)
    ui_font = pygame.font.SysFont("arial", 28)

# Banco de Palavras
palavras = {
    "python": "Linguagem de programação popular para automação e IA.",
    "teclado": "Periférico usado para digitar em computadores.",
    "monitor": "Tela que exibe a saída visual do computador.",
    "mouse": "Dispositivo apontador com botões.",
    "internet": "Rede global que conecta computadores mundialmente.",
    "algoritmo": "Sequência lógica para resolver problemas.",
    "dados": "Informações armazenadas para análise.",
    "nuvem": "Armazenamento remoto acessível online.",
    "aplicativo": "Programa projetado para tarefas específicas.",
    "bateria": "Fonte de energia portátil para dispositivos.",
    "wifi": "Tecnologia de rede sem fio.",
    "senha": "Código secreto para acesso seguro.",
    "robotica": "Área que estuda a criação de robôs.",
    "jogos": "Forma de entretenimento interativo.",
    "streaming": "Transmissão contínua de mídia online.",
    "smartphone": "Telefone celular com funções avançadas.",
    "notebook": "Computador portátil compacto.",
    "headset": "Fones de ouvido com microfone.",
    "webcam": "Câmera para transmissão ao vivo.",
    "roteador": "Dispositivo que direciona tráfego de rede.",
    "impressora": "Aparelho que produz cópias físicas de documentos.",
    "hacker": "Especialista em segurança digital (ou invasor).",
    "programador": "Profissional que escreve códigos.",
    "memoria": "Componente que armazena dados temporários.",
    "processador": "Cérebro do computador, executa cálculos.",
    "gigabyte": "Unidade de medida de armazenamento digital.",
    "criptografia": "Técnica para proteger informações.",
    "backup": "Cópia de segurança de arquivos.",
    "download": "Transferência de arquivos da internet.",
    "upload": "Envio de arquivos para a internet.",
    "firewall": "Sistema de segurança contra acessos não autorizados.",
    "browser": "Navegador para acessar páginas da web.",
    "hashtag": "Palavra-chave precedida por '#' em redes sociais.",
    "emoticon": "Representação gráfica de emoções (ex: 😊).",
    "spam": "Mensagens eletrônicas não solicitadas."
}

# Classe para Botões
class BloodButton:
    def __init__(self, x, y, w, h, text, 
                 base_color=Colors.BLOOD_RED, 
                 hover_color=Colors.LIGHT_BLOOD,
                 text_color=Colors.WHITE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.current_color = base_color
        self.hover = False
        self.shadow = 0
        
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)
        target_color = self.hover_color if self.hover else self.base_color
        self.current_color = [
            self.current_color[0] + (target_color[0] - self.current_color[0]) * 0.2,
            self.current_color[1] + (target_color[1] - self.current_color[1]) * 0.2,
            self.current_color[2] + (target_color[2] - self.current_color[2]) * 0.2
        ]
        self.shadow = 10 if self.hover else 5
    
    def draw(self, surface):
        # Sombra
        shadow_rect = self.rect.copy()
        shadow_rect.y += self.shadow
        pygame.draw.rect(surface, (*Colors.BLACK, 100), shadow_rect, border_radius=15)
        
        # Botão principal
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=12)
        pygame.draw.rect(surface, Colors.NEON_RED, self.rect, 3, border_radius=12)
        
        # Texto
        text_surf = main_font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    
    def is_clicked(self, pos, event):
        return (self.hover and event.type == pygame.MOUSEBUTTONDOWN 
                and event.button == 1)

# Função para escolher palavra aleatória
def escolher_palavra():
    palavra = random.choice(list(palavras.keys()))
    dica = palavras[palavra]
    return palavra, dica

# Tela do Jogo Principal
def jogo(acertos, erros):
    palavra, dica = escolher_palavra()
    tentativas = 3
    input_text = ""
    mensagem = ""
    cor_mensagem = Colors.WHITE
    
    input_box = pygame.Rect(WIDTH//2 - 200, HEIGHT//2, 400, 50)
    active = True
    
    clock = pygame.time.Clock()
    
    while tentativas > 0:
        dt = clock.tick(60) / 1000
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if input_text.lower() == palavra:
                            mensagem = "🎉 VOCÊ ACERTOU!"
                            cor_mensagem = Colors.HIGHLIGHT
                            pygame.display.flip()
                            pygame.time.delay(1500)
                            return True, acertos + 1, erros
                        else:
                            tentativas -= 1
                            mensagem = "❌ ERRADO! Tente novamente."
                            cor_mensagem = Colors.NEON_RED
                            input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
        
        # Renderização
        screen.fill(Colors.BLACK)
        
        # Cabeçalho
        pygame.draw.rect(screen, Colors.DARK_BLOOD, (0, 0, WIDTH, 100))
        title = main_font.render("WORD HUNTER", True, Colors.NEON_RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        
        # Contadores
        acertos_text = ui_font.render(f"Acertos: {acertos}", True, Colors.WHITE)
        erros_text = ui_font.render(f"Erros: {erros}", True, Colors.WHITE)
        screen.blit(acertos_text, (50, 50))
        screen.blit(erros_text, (WIDTH - 150, 50))
        
        # Dica
        dica_text = ui_font.render(f"Dica: {dica}", True, Colors.SILVER)
        screen.blit(dica_text, (WIDTH//2 - dica_text.get_width()//2, 150))
        
        # Tentativas
        tentativas_text = main_font.render(f"Tentativas: {tentativas}", True, Colors.LIGHT_BLOOD)
        screen.blit(tentativas_text, (WIDTH//2 - tentativas_text.get_width()//2, 200))
        
        # Input Box
        pygame.draw.rect(screen, Colors.METALIC, input_box, border_radius=8)
        pygame.draw.rect(screen, Colors.NEON_RED if active else Colors.SILVER, input_box, 3, border_radius=8)
        text_surf = main_font.render(input_text, True, Colors.WHITE)
        screen.blit(text_surf, (input_box.x + 15, input_box.y + 10))
        
        # Mensagem
        if mensagem:
            msg_surf = main_font.render(mensagem, True, cor_mensagem)
            screen.blit(msg_surf, (WIDTH//2 - msg_surf.get_width()//2, 350))
        
        pygame.display.flip()
    
    # Se acabaram as tentativas
    erros += 1
    screen.fill(Colors.BLACK)
    resultado = main_font.render(f"A palavra era: {palavra.upper()}", True, Colors.NEON_RED)
    screen.blit(resultado, (WIDTH//2 - resultado.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    return False, acertos, erros

# Tela de Jogar Novamente
def jogar_novamente(acertos, erros):
    btn_sim = BloodButton(WIDTH//2 - 220, HEIGHT//2 + 50, 200, 60, "SIM")
    btn_nao = BloodButton(WIDTH//2 + 20, HEIGHT//2 + 50, 200, 60, "NÃO")
    
    clock = pygame.time.Clock()
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        btn_sim.update(mouse_pos)
        btn_nao.update(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if btn_sim.is_clicked(mouse_pos, event):
                return True
            if btn_nao.is_clicked(mouse_pos, event):
                return False
        
        # Renderização
        screen.fill(Colors.BLACK)
        
        # Título
        title = main_font.render("FIM DE JOGO", True, Colors.NEON_RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        
        # Estatísticas
        stats = ui_font.render(f"Acertos: {acertos}   |   Erros: {erros}", True, Colors.SILVER)
        screen.blit(stats, (WIDTH//2 - stats.get_width()//2, 250))
        
        # Pergunta
        question = main_font.render("Jogar novamente?", True, Colors.WHITE)
        screen.blit(question, (WIDTH//2 - question.get_width()//2, 350))
        
        # Botões
        btn_sim.draw(screen)
        btn_nao.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

# Tela Inicial
def tela_inicial():
    start_button = BloodButton(WIDTH//2 - 150, HEIGHT//2 + 100, 300, 70, "INICIAR CAÇADA")
    
    clock = pygame.time.Clock()
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        start_button.update(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if start_button.is_clicked(mouse_pos, event):
                return
        
        # Renderização
        screen.fill(Colors.BLACK)
        
        # Título
        draw_glow_text(screen, "WORD HUNTER", title_font, Colors.NEON_RED, 
                      (WIDTH//2 - title_font.size("WORD HUNTER")[0]//2, 150),
                      Colors.LIGHT_BLOOD)
        
        # Subtítulo
        subtitle = main_font.render("Edição Dark Blood", True, Colors.SILVER)
        screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 250))
        
        # Botão
        start_button.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

# Função Principal
def main():
    pygame.mouse.set_visible(True)
    
    acertos = 0
    erros = 0
    
    tela_inicial()
    
    while True:
        resultado, acertos, erros = jogo(acertos, erros)
        if not jogar_novamente(acertos, erros):
            break
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()