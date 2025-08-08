from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __inti__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            direction1 = pygame.Vector2(self.velocity).rotate(random_angle)
            direction2 = pygame.Vector2(self.velocity).rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = direction1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = direction2 * 1.2



