class Arbitrator:

    def __init__(self, BBCON):
        self.BBCON = BBCON
        self.stochastic = False
        self.halt = False

    def fetch_behaviors(self):
        return self.BBCON.active_behaviors

    # Simple deterministic
    def choose_action(self):
        behaviors = self.fetch_behaviors()
        winner = behaviors[0]
        max_weight = -1
        for b in behaviors:
            if b.halt_request:
                self.halt = True
            if b.weight > max_weight:
                max_weight = b.weight
                winner = b
        return winner.motor_recommendations, self.halt



