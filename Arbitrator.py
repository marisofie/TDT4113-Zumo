class Arbitrator:

    def __init__(self, bbcon):
        self.bbcon = bbcon

    # Fetches the active behaviours from the BBCON
    def fetch_behaviors(self):
        return self.bbcon.get_active_behaviours()

    # Choses a behaviour based on the behaviour weight (deterministic)
    # Returns the chosen behaviours motor recommendations (update())
    # and a boolean indicating whether a run should be halted
    def choose_action_deterministic(self):
        active_behaviours = self.fetch_behaviors()
        max_weight = 0
        chosen_behaviour = None

        for behaviour in active_behaviours:
            weight = behaviour.get_weight
            if weight > max_weight:
                max_weight = weight
                chosen_behaviour = behaviour

        return chosen_behaviour.get_motor_recommendations(), chosen_behaviour.get_halt_request()
