class GameStats():
    """Track statistics for game"""

    def __init__(self, ai_settings):
        """Initialize stats object"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """"Initialize stats that can change during game;
        this will reset upon a new game - not just upon
        reopening the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1