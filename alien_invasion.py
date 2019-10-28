import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Inicjaliacja Pygame, ustawień i obiektu ekranu .
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    pygame.display.set_caption('Inwazja obcych')

    # Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych.
    ship = Ship(ai_settings, screen)

    aliens = pygame.sprite.Group()
    bullets = Group()

    # Utworzenie floty obcych.
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()