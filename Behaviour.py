class Behavior():

    def __init__(self, bbcon, sensobs, priority, active_flag):
        self.bbcon = bbcon  # Pointer to the bbcon object
        self.sensobs = sensobs  # A list of all the Sensobs
        self.active_flag = active_flag  # A boolean indicating if the behavior is active
        self.halt_request = False
        self.motor_recommendations = []
        self.weight = 0
        self.match_degree = 0
        self.priority = priority  # A value indicating the priority of the behavior

    def get_halt_request(self):
        return self.halt_request

    def get_motor_recommendations(self):
        return self.motor_recommendations

    def get_active_flag(self):
        return self.active_flag

    # Update the weight of the beahvior
    def set_weight(self):
        self.weight = self.priority * self.match_degree

    def get_weight(self):
        return self.weight

    def consider_deactivation(self):
        #Test if the behavior should be deactiveted
        pass

    def consider_activation(self):
        #Test if the behaviour should be activated
        pass

    def sense_and_act(self):
        #the core computations performed by the behavior that use sensob readings to produce
        #motor recommendations (and halt requests).
        #MUST UPDATE MOTORRECOMMENDATIONS
        pass
    
    #Updates the behavior. The main call to the behavior. Returns the motor_reccomantations
    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()
            self.set_weight()

