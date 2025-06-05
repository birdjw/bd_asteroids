import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            self.radius - ASTEROID_MIN_RADIUS
            new_angle_1 = self.velocity.rotate(random_angle)
            new_angle_2 = self.velocity.rotate(- random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_position_1 = self.position
            new_position_2 = self.position
            new_ast_1 = Asteroid(new_position_1.x, new_position_1.y, new_radius)
            new_ast_2 = Asteroid(new_position_2.x, new_position_2.y, new_radius)
            new_ast_1.velocity = (new_angle_1 * 1.2)
            new_ast_2.velocity = (new_angle_2 * 1.2)

