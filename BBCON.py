class BBCON:

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = None

        self.current_timestep = 0

    # Adds a newly-created behavior to he list of behaviours
    def add_behaviour(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    # Adds a newly-created sensob to the list of sensobs
    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    # Adds existing behvior to list of active behaviors
    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    # Removes existing behavior from active to inactive list of behaviors
    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        self.inactive_behaviors.append(behavior)

    def run_one_timestep(self):
        #TODO

    # Update all sensobs:
    # querying the relevant sensors for their values
    # pre-processing those values
    def update_all_sensobs(self):
        for sensob in self.sensobs:
            sensob.update()

    # Update all behaviors:
    # reading relevant sensob values and producing a motor recommendation
    def update_all_behaviours(self):
        #TODO

    # Invoke the arbitrator by calling arbitrator.choose action
    # choose a winning behavior
    # return that behavior’s motor recommendations and halt request flag
    def invoke_arbitrator(self):
        #TODO

    # Update motobs based on invoke_arbitrator()s motor recommendations
    # Motobs need to update settings of all motors
    def update_motobs(self):
        #TODO

    # Wait: allows the motor settings to remain active for a short period of time, e.g. one half second
    # producing activity in the robot, such as moving forward or turning
    def wait(self):
        #TODO

    # Resets all sensobs and/or associated sensors by calling the sensobs' own reset method
    def reset_sensob(self, sensob, reset_all):
        if reset_all:
            for sensob in self.sensobs:
                sensob.reset() # All sensors have a reset()-fuction, so assumed sensobs also have that
        else:
            sensob.reset()

