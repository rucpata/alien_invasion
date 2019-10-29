class GameStats():
    """Monitorowanie danych statystycznych w grze "Alien Invasion"."""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Uruchomienie gry w stanie nieaktywnych
        self.game_avtive = False

    def reset_stats(self):
        """
        Inicjalizacja danych statystycznych, które mogą zmieniać
        się w trakcie gry.
        """
        self.ships_left = self.ai_settings.ship_limit
