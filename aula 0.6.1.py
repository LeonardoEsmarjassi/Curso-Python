import pygame
import random
import os
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Corrida com Contramão")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()
SPEED_INCREMENT = 0.001

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.player_speed = 5
        self.base_speed = 5
        self.obstacle_speed = 5
        self.obstacle_frequency = 60  # frames
        self.road_width = SCREEN_WIDTH
        self.lane_width = SCREEN_WIDTH // 2
        self.obstacles = []
        self.last_obstacle_time = 0
        self.player_lane = "right"  # Começa na mão direita
        
        # Carregar imagens
        self.load_images()
        
        # Posição inicial do jogador (mão direita)
        self.player_x = SCREEN_WIDTH // 4 * 3 - self.player_img.get_width() // 2
        self.player_y = SCREEN_HEIGHT - self.player_img.get_height() - 20
        
        # Posição da pista
        self.road_x = 0
        self.road_y = 0
        
    def load_images(self):
        # Tente carregar imagens personalizadas
        try:
            self.player_img = pygame.image.load("player_car.png").convert_alpha()
        except:
            self.player_img = pygame.Surface((50, 80))
            self.player_img.fill(RED)
            
        try:
            self.road_img = pygame.image.load("road.png").convert()
            self.road_img = pygame.transform.scale(self.road_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.road_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.road_img.fill(GRAY)
            # Desenhar linhas da pista
            pygame.draw.rect(self.road_img, WHITE, (SCREEN_WIDTH//2 - 2, 0, 4, SCREEN_HEIGHT))
            for i in range(0, SCREEN_HEIGHT, 50):
                pygame.draw.rect(self.road_img, WHITE, (SCREEN_WIDTH//2 - 20, i, 40, 30))
                
        try:
            self.obstacle_imgs = [
                pygame.image.load("obstacle_car1.png").convert_alpha(),
                pygame.image.load("obstacle_car2.png").convert_alpha(),
                pygame.image.load("obstacle_truck.png").convert_alpha()
            ]
        except:
            self.obstacle_imgs = []
            for i in range(3):
                img = pygame.Surface((50, 80))
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                img.fill(color)
                self.obstacle_imgs.append(img)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.__init__()  # Reinicia o jogo
                if event.key == pygame.K_SPACE and not self.game_over:
                    # Trocar de pista com espaço
                    if self.player_lane == "right":
                        self.player_lane = "left"
                        self.player_x = SCREEN_WIDTH // 4 - self.player_img.get_width() // 2
                    else:
                        self.player_lane = "right"
                        self.player_x = SCREEN_WIDTH // 4 * 3 - self.player_img.get_width() // 2
                    
        if not self.game_over:
            keys = pygame.key.get_pressed()
            # Movimento suave dentro da pista
            if keys[pygame.K_LEFT]:
                if self.player_lane == "right":
                    self.player_x = max(SCREEN_WIDTH // 2 + 10, self.player_x - 5)
                else:
                    self.player_x = max(10, self.player_x - 5)
            if keys[pygame.K_RIGHT]:
                if self.player_lane == "right":
                    self.player_x = min(SCREEN_WIDTH - self.player_img.get_width() - 10, self.player_x + 5)
                else:
                    self.player_x = min(SCREEN_WIDTH // 2 - self.player_img.get_width() - 10, self.player_x + 5)
                    
        return True
    
    def spawn_obstacles(self):
        now = pygame.time.get_ticks()
        if now - self.last_obstacle_time > 1000:  # 1 segundo
            self.last_obstacle_time = now
            
            # Escolher aleatoriamente entre mão direita ou contramão (50% de chance para cada)
            lane = random.choice(["right", "left"])
            
            if lane == "right":
                x = random.randint(SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH - 70)
                speed = self.obstacle_speed
            else:  # contramão
                x = random.randint(20, SCREEN_WIDTH // 2 - 70)
                speed = -self.obstacle_speed * 0.8  # Mais devagar na contramão
                
            img = random.choice(self.obstacle_imgs)
            self.obstacles.append({
                "x": x,
                "y": -img.get_height() if speed > 0 else SCREEN_HEIGHT,  # Vem de cima ou de baixo
                "img": img,
                "speed": speed,
                "lane": lane
            })
    
    def update(self):
        if self.game_over:
            return
            
        # Aumentar dificuldade gradualmente
        self.base_speed += SPEED_INCREMENT
        self.player_speed = self.base_speed
        self.obstacle_speed = self.base_speed
        self.score += self.base_speed / 10
        
        # Gerar obstáculos
        self.spawn_obstacles()
        
        # Atualizar obstáculos
        for obstacle in self.obstacles[:]:
            obstacle["y"] += obstacle["speed"]
            
            # Verificar colisão
            player_rect = pygame.Rect(self.player_x, self.player_y, 
                                     self.player_img.get_width(), self.player_img.get_height())
            obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], 
                                       obstacle["img"].get_width(), obstacle["img"].get_height())
            
            if player_rect.colliderect(obstacle_rect):
                self.game_over = True
                
            # Remover obstáculos que saíram da tela
            if (obstacle["speed"] > 0 and obstacle["y"] > SCREEN_HEIGHT) or \
               (obstacle["speed"] < 0 and obstacle["y"] < -obstacle["img"].get_height()):
                self.obstacles.remove(obstacle)
    
    def draw(self):
        # Desenhar pista
        screen.blit(self.road_img, (self.road_x, self.road_y))
        
        # Desenhar faixa central amarela para contramão
        pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH//2 - 5, 0, 10, SCREEN_HEIGHT))
        
        # Desenhar obstáculos
        for obstacle in self.obstacles:
            screen.blit(obstacle["img"], (obstacle["x"], obstacle["y"]))
        
        # Desenhar jogador
        screen.blit(self.player_img, (self.player_x, self.player_y))
        
        # Desenhar indicador de pista
        font = pygame.font.SysFont(None, 24)
        lane_text = font.render(f"Pista: {'DIREITA' if self.player_lane == 'right' else 'ESQUERDA (Contramão)'}", True, WHITE)
        screen.blit(lane_text, (SCREEN_WIDTH - lane_text.get_width() - 10, 10))
        
        # Desenhar pontuação
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Distância: {int(self.score)}m", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Instruções
        instructions = font.render("Espaço: Trocar de pista", True, WHITE)
        screen.blit(instructions, (10, 50))
        
        # Desenhar tela de game over se necessário
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            font_large = pygame.font.SysFont(None, 72)
            game_over_text = font_large.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            
            font_small = pygame.font.SysFont(None, 36)
            restart_text = font_small.render("Pressione R para reiniciar", True, WHITE)
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 20))
            
            score_text = font_small.render(f"Distância final: {int(self.score)}m", True, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, SCREEN_HEIGHT//2 + 70))
        
        pygame.display.flip()

def main():
    game = Game()
    running = True
    
    while running:
        running = game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()