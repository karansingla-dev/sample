import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)

class Particle:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-2, -1)
        self.life = 255
        self.size = random.uniform(3, 6)
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 2
        self.size += 0.1
        
    def draw(self, screen):
        if self.life > 0:
            color = (100, 100, 100, self.life)
            surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, color, (self.size, self.size), self.size)
            screen.blit(surf, (self.x - self.size, self.y - self.size))

class Smoke:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        
    def update(self):
        # Add new particles
        for _ in range(2):
            px = self.x + random.uniform(-3, 3)
            py = self.y + random.uniform(-2, 2)
            self.particles.append(Particle(px, py))
        
        # Update and remove dead particles
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.life > 0]
        
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Smooth Smoke")
    clock = pygame.time.Clock()
    
    smoke = Smoke(WIDTH // 2, HEIGHT - 50)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        smoke.update()
        
        screen.fill(BLACK)
        smoke.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()