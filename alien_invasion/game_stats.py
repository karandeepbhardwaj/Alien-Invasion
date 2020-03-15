class GameStats():
    """Track stats for aliens invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start the alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit

