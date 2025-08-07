import pygame

from circleshape import *
from constants import *

class Player(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.timer -= dt
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):         # Overwrite the parent CircleShape method
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)  # Set the position of the player as the starting point
            shot.velocity = pygame.Vector2(0,1)                         # We set the direction x = 0, y = 1 to pooint upward
            shot.velocity = shot.velocity.rotate(self.rotation)         # the velocity = the velocity rotated to the player
            shot.velocity *= PLAYER_SHOOT_SPEED                         # Increase the shooting speed
            self.timer = PLAYER_SHOOT_COOLDOWN


class Shot(CircleShape):
    def __inti__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,2)
    
    def update(self, dt):
        self.position += self.velocity * dt

