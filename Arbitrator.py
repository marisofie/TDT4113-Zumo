class Arbitrator:

    def __init__(self, bbcon):
        self.bbcon = bbcon

    # Fetches the active behaviors from the BBCON
    def fetch_behaviors(self):
        return self.bbcon.get_active_behaviors()

    # Choses a behavior based on the behavior weight (deterministic)
    # Returns the chosen behaviors motor recommendations (update())
    # and a boolean indicating whether a run should be halted
    def choose_action_deterministic(self):
        active_behaviors = self.fetch_behaviors()
        max_weight = 0
        chosen_behavior = None

        for behavior in active_behaviors:
            weight = behavior.get_weight
            if weight > max_weight:
                max_weight = weight
                chosen_behavior = behavior

        return chosen_behavior.get_motor_recommendations(), chosen_behavior.get_halt_request()
