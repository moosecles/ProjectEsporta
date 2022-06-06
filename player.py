
class Player:
    def __init__(self):
        self.total_points = 100
        self.multiplier = 5
        self.yoga_mats = 0
        self.punching_bag = 0
        self.treadmills = 0
        self.dead_lift = 0
        self.db_rack = 0
        self.dumbbells = 0
        self.squat_rack = 0

    def add_score(self):
        self.total_points += 1 * self.multiplier
        # return self.total_points

    def upgrade_multiplier(self):  # Function to return the multiplier we are adding per second
        return (self.yoga_mats * 1) + (self.punching_bag * 10)


