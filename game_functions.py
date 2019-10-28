import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Reakcja na naciśnięcie klawisza.'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Wytwarzanie pocisku, jeśli nie przekroczono ustalonego limitu.'''
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''Reakcja na zwolnienie klawisza.'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    ''' Reakcja na zdarzenia generowane przez klawiaturę i mysz. '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    ''' Uaktualnienie obrazów na ekranie i przejście do nowego ekranu.'''
    # Odświeżenie ekranu w trakcje każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego i obcych.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Wyświerlenie ostantnio zmodyfikowanego ekranu
    pygame.display.flip()

def update_bullets(aliens, bullets):
    ''' Uaktualnienie położenia pocisków i usunięcie tych niweidocznych na ekranie.'''
    # Uaktualnienie położenia pocisków.
    bullets.update()

    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Sprawdzanie, czy którykolwiek pocisk trafił obcego.
    # Jeżeli tak, usuwamy zarówno pocisk, jak i obcego.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def get_number_aliens_x(ai_settings, alien_width):
    """Ustalenie liczby obcych, którzy zmieszczą się w rzędzie."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Ustalenie. ile rzędów obcych zmieści się na ekranie."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Utworzenie obcego i umeiszczenie go w rzędzie."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Utworzenie pełnej floty obcych."""
    # Utworzenie obcego i ustalenie liczny obcych, którzy zmieszczą się w rzędzie.
    # Odległość międzu poszczególnymi obcymi jest równa szerokości obcego .
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Utworzenie floty obcych.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(aliens):
    """Uaktualnienie położenia wszystkich obcych we flocie."""

def check_fleet_edges(ai_settings, aliens):
    """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona porusza."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """
    Sprawdzenie, czy flota znajduje sie przy krawędzi ekranu, a następnie
    uaktualnienie położenia wszystkich obcych we flocie.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()