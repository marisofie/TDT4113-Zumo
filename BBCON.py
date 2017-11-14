import time
import timeit
import sys
from Motob import Motob
from Arbitrator import Arbitrator


class BBCON:
    def __init__(self, sensobs, behaviors, active_behaviors):
        self.behaviors = behaviors
        self.active_behaviors = active_behaviors
        for behavior in active_behaviors:
            if behavior not in behaviors:
                self.add_behavior(behavior)
        self.sensobs = sensobs
        self.motob = Motob()
        self.arbitrator = Arbitrator(self)
        self.current_timestamp = timeit.default_timer()

    def get_active_behaviors(self):
        return self.active_behaviors

    # Adds a newly-created behavior to he list of behaviors
    def add_behavior(self, behavior):
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
    def update_all_behaviors(self):
        for behavior in self.behaviors:
            behavior.update()

        print("Active behaviors: ", self.active_behaviors)

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
    def update_motob(self):
        motor_recom, halt_req = self.invoke_arbitrator()
        print(motor_recom)
        print(halt_req)
        if halt_req:
            self.halt()
        else:
            self.motob.update_motor(motor_recom)

    def halt(self):
        self.motob.stop()
        sys.exit()

    # Wait: allows the motor settings to remain active for a short period of time, e.g. one half second
    # producing activity in the robot, such as moving forward or turning
    def wait(self):
        time.sleep(1)

    # Resets all sensobs and/or associated sensors by calling the sensobs' own reset method
    def reset_sensob(self):
        for sensob in self.sensobs:
            sensob.reset()

    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviors()
        self.update_motob()
        #self.wait()
        self.reset_sensob()


