from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0