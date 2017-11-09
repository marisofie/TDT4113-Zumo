import time
class BBCON:

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = None

        self.current_timestep = 0

    def get_active_behaviours(self):
        return self.active_behaviors

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
        self.update_all_sensobs()
        self.update_all_behaviours()
        self.arbitrator.choose_action_deterministic()
        self.update_motobs()
        self.wait()
        self.reset_sensob()

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
        self.arbitrator.choose_action()

    # Update motobs based on invoke_arbitrator()s motor recommendations
    # Motobs need to update settings of all motors
    def update_motobs(self):
        info = self.invoke_arbitrator()
        if info[1]:
            self.halt()
        else:
            motor_recom = info[0]
            k = 0
            for motob in self.motobs:
                motob.update_motor(motor_recom[k])
                k += 1

    def halt(self):
        for motob in self.motobs:
            motob.stop()

    # Wait: allows the motor settings to remain active for a short period of time, e.g. one half second
    # producing activity in the robot, such as moving forward or turning
    def wait(self):
        time.sleep(0.5)

    # Resets all sensobs and/or associated sensors by calling the sensobs' own reset method
    def reset_sensob(self):
        for sensob in self.sensobs:
            sensob.reset()

