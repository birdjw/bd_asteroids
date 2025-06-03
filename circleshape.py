import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

    def update(self, dt):
        # sub-classes must override
        pass

def collision_check(self, Asteroid):
    radii_sum = self.radius + Asteroid.radius
    if self.position.distance_to(Asteroid.position) <= radii_sum:
        return True
    else:
        return False

def asteroid_bullet_collision(bullet, asteroid):
    radii_sum = bullet.radius + asteroid.radius
    if bullet.position.distance_to(asteroid.position) <= radii_sum:
        bullet.kill()
        asteroid.kill()

