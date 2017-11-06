class Behavior():

    def __init__(self, bbcon, sensobs, priority, active_flag):
        self.bbcon = bbcon #Pointer to the bbcon object
        self.sensons = sensobs # A list of all the sensors
        self.priority = priority #A value indicating the priority of the behavior
        self.active_flag = active_flag #A boolean indicating if the behavior is active
        self.weight = 0
        self.match_degree = 0

    def consider_deactivation(self):
        #Test if the behavior should be deactiveted
        pass

    def consider_activation(self):
        #Test if the behaviour should be activated
        pass

    def sense_and_act(self):
        #the core computations performed by the behavior that use sensob readings to produce
        #motor recommendations (and halt requests).
        pass
    
    #Update the weight of the beahvior 
    def get_weight(self):
        self.weight = self.priority * self.match_degree
    
    #Updates the behavior. The main call to the behavior. Returns the motor_reccomantations
    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        elif self.active_flag == False:
            self.consider_deactivation()
        motor_recommendations = self.sense_and_act()
        self.get_weight()
        return motor_recommendations
