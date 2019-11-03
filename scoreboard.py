import pygame.font

class Scoreboard():
    """Klasa przeznaczona do przedstawienia infomracji o punktacji."""

    def __init__(self, ai_settings, screen, stats):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Ustawienia czcionki dla informaci dotyczących punktacji.
        self.text_color =(30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_high_score(self):
        """Konwersja najlepszego wyniku w grze na wygenerowany obraz."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.ai_settings.bg_color)

        # Wyświetlenie najlepszego wyniku w grze na środku ekranu, przy górnej krawędzi
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        #Wyświetlenie punktacji w prawym górym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlenie na ekranie punktacji oraz statków"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                           self.ai_settings.bg_color)

        #Numer poziomu jest wyświetlany pod aktualną pozycją
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
