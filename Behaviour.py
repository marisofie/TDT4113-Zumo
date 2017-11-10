import random
from Sensob import Reflectanceob


class Behavior:

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

    # Test if the behavior should be deactiveted
    def consider_deactivation(self):
        pass

    # Test if the behaviour should be activated
    def consider_activation(self):
        pass

    # The core computations performed by the behavior that use sensob readings to produce
    # motor recommendations (and halt requests).
    # Must update motor recommendations.
    def sense_and_act(self):
        pass
    
    # Updates the behavior. The main call to the behavior
    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()
            self.set_weight()


class StopRed(Behavior):

    def __init__(self, priority=1, active_flag=True, bbcon=None, sensobs=[]):
        super().__init__(bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.stop_distance = 5
        self.min_red = 0.3
        self.motor_recommendations = []

    def consider_activation(self):
        # if object is closer than 5cm
        # must remember that sensobs[0] contains distance
        percent_red = self.sensobs[1].get_sensor_value()
        if self.sensobs[0].value <= self.stop_distance and percent_red > self.min_red:
            self.active_flag = True

    def consider_deactivation(self):
        # if object is farther away than 5cm, deactivates behaviour
        percent_red = self.sensobs[1].get_sensor_value()
        if self.sensobs[0].get_sensor_value() > self.stop_distance or percent_red < self.min_red:
            self.active_flag = False
            self.motor_recommendations = []

    def sense_and_act(self):
        percent_red = self.sensobs[1].get_sensor_value()
        if percent_red < self.min_red:
            self.match_degree = 0
        else:
            self.match_degree = percent_red
        self.motor_recommendations = [('S', 0)]


# makes the robot drive around until sensors get something.
class DriveAround(Behavior):

    def __init__(self, priority=1, active_flag=True, bbcon=None, sensobs=None):
        super().__init__(bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        directions = ['R', 'L', 'F', 'B']
        direction = directions[random.randint(0, 3)]
        speed = random.randint(0, 100)
        self.motor_recommendations = [(direction, speed)]
        self.match_degree = 0.1


class FollowLines(Behavior):

    def __init__(self, bbcon, sensobs=Reflectanceob(), priority=1, active_flag=True):
        super().__init__(bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.trigger_value = 0.2

    # Deactivate if no black line is found
    def consider_deactivation(self):
        data = self.sensobs.get_sensor_value()[0]
        for value in data:
            if value < self.trigger_value:
                return False
        self.active_flag = False
        return True

    # Activate if black line is found
    def consider_activation(self):
        data = self.sensobs.get_sensor_value()[0]
        for value in data:
            if value < self.trigger_value:
                self.active_flag = True
                return True
        return False

    def sense_and_act(self):
        data = self.sensobs.get_sensor_value()[0]
        if data[0] < self.trigger_value or data[1] < self.trigger_value:
            self.motor_recommendations = ['L']
        elif data[4] < self.trigger_value or data[5] < self.trigger_value:
            self.motor_recommendations = ['R']
        elif data[2] < self.trigger_value or data[3] < self.trigger_value:
            self.motor_recommendations = ['F']






