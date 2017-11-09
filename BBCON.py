import time
import sys


class BBCON:
    def __init__(self, arbitrator, motobs, sensobs, behaviours, active_behaviors):
        self.behaviors = behaviours
        self.active_behaviors = active_behaviors
        for behavior in active_behaviors:
            if behavior not in behaviours:
                self.add_behaviour(behavior)
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator

    def get_active_behaviors(self):
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
        if behavior not in self.behaviors:
            raise Exception('The behavior must be in behaviors to be active')
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    # Removes existing behavior from active to inactive list of behaviors
    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    # Update all sensobs:
    # querying the relevant sensors for their values
    # pre-processing those values
    def update_all_sensobs(self):
        for sensob in self.sensobs:
            sensob.update()

    # Update all behaviors:
    # reading relevant sensob values and producing a motor recommendation
    def update_all_behaviours(self):
        for behavior in self.behaviors:
            behavior.update()

        for behavior in self.behaviors:
            if behavior in self.active_behaviors and not behavior.active_flag:
                self.deactivate_behavior(behavior)
            elif behavior not in self.active_behaviors and behavior.active_flag:
                self.activate_behavior(behavior)

    # Invoke the arbitrator by calling arbitrator.choose action
    # choose a winning behavior
    # return that behavior’s motor recommendations and halt request flag
    def invoke_arbitrator(self):
        return self.arbitrator.choose_action_deterministic()

    # Update motobs based on invoke_arbitrator()s motor recommendations
    # Motobs need to update settings of all motors
    def update_motobs(self):
        motor_recom, halt_req = self.invoke_arbitrator()
        if halt_req:
            self.halt()
        else:
            k = 0
            for motob in self.motobs:
                motob.update_motor(motor_recom[k])
                k += 1

    def halt(self):
        for motob in self.motobs:
            motob.stop()
        sys.exit()

    # Wait: allows the motor settings to remain active for a short period of time, e.g. one half second
    # producing activity in the robot, such as moving forward or turning
    def wait(self):
        time.sleep(0.5)

    # Resets all sensobs and/or associated sensors by calling the sensobs' own reset method
    def reset_sensob(self):
        for sensob in self.sensobs:
            sensob.reset()

    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviours()
        self.arbitrator.choose_action_deterministic()
        self.update_motobs()
        self.wait()
        self.reset_sensob()

