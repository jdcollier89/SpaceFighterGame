class GameStats:
    """Track statistics for game"""

    def __init__(self, ai_settings):
        """Initialize stats object"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in inactive state
        self.game_active = False
        self.level_begun = False # If mid-game this will be true; needed for pausing

        self.load_highscore()

    def reset_stats(self):
        """"Initialize stats that can change during game;
        this will reset upon a new game - not just upon
        reopening the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_highscore(self):
        """Load the previous high score (if any) from
        a text file - if no previous high score is found
        simply use 0."""
        try:
            f = open("high_score.txt", "r")
            if f.mode == 'r':
                self.high_score = f.read()
                self.high_score = int(self.high_score)
            f.close()
        except:
            self.high_score = 0
        return

    def save_highscore(self):
        """Save the current high score to a text file
        so that it can be reloaded upon opening the game
        again."""
        try:
            f = open("high_score.txt", "w+")
            f.write(str(self.high_score))
            f.close()
        except:
            pass