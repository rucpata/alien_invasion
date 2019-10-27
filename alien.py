import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedyńczego obcego ."""
    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego położenia
        początkowego."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytywanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywnaie dokładnego położenia obcego.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Przesunięcie obcego w prawo lub w lewo."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Wywietlenie obcego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

