import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        ''' Inicjalizacja statku kosmicznego i jego położenie
        początkowe. '''
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytywanie obrazu statku kosmicznego i pobieranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Punkt środkowy staku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.center = float(self.rect.centerx)
        self.bottom2 = float(self.rect.bottom)

        # Opcje wskazujące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''
        Uaktualnienie położenia statku na postawie operacji wskazującej
        na jego ruch.
        '''
        # Uaktualnienie wartości punktów środkowego statku, a nie jego prostokąta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.bottom2 -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom2 += self.ai_settings.ship_speed_factor

        # Uaktualnienie obiektu rect na podstawie wartości self.center i self.bottom2
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom2

    def blitme(self):
        ''' Wyświerlenie statku kosmicznego w jego aktualnym położeniu.'''
        self.screen.blit(self.image, self.rect)