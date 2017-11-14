import random
from Sensob import Reflectanceob


class Behavior:

    def __init__(self, sensobs, priority, active_flag):
        #self.bbcon = bbcon  # Pointer to the bbcon object
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

    # Test if the behavior should be activated
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


# when the program has been running for 5 minutes, the robot stops.
class RobotDone(Behavior):

    def __init__(self, priority=1, active_flag=True, sensobs=[]):
        super().__init__(priority, sensobs, active_flag)
        self.stop_time = 30000

    def consider_activation(self):
        if self.bbcon.current_timestamp >= self.stop_time:
            self.halt_request = True

    def consider_deactivation(self):
        if self.bbcon.current_timestamp < self.stop_time:
            self.halt_request = False

    def sense_and_act(self):
        self.match_degree = 1
        self.motor_recommendations = [('S', 0)]


class StopRed(Behavior):

    def __init__(self, priority=1, active_flag=True, sensobs=[]):
        super().__init__(sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.active_distance = 10
        self.stop_distance = 5
        self.min_red = 0.3
        self.motor_recommendations = []

    def consider_activation(self):
        # if object is closer than 10cm
        # must remember that sensobs[0] contains distance
        if self.sensobs[0].value <= self.active_distance:
            self.active_flag = True

    def consider_deactivation(self):
        # if object is farther away than 10cm, deactivates behavior
        if self.sensobs[0].get_sensor_value() > self.stop_distance:
            self.active_flag = False

    def sense_and_act(self):
        percent_red = self.sensobs[1].get_sensor_value()
        if percent_red > self.min_red and self.sensobs[0].get_sensor_value() <= self.stop_distance:
            self.match_degree = percent_red
            self.motor_recommendations = [('S', 0)]
        else:
            self.match_degree = 0


class Stop(Behavior):

    def __init__(self, priority=1, active_flag=True, sensobs=[]):
        super().__init__(sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.active_distance = 10
        self.stop_distance = 5
        self.motor_recommendations = []

    def consider_activation(self):
        # if object is closer than 10cm
        # must remember that sensobs[0] contains distance
        print(self.sensobs[0].get_sensor_value())
        if self.sensobs[0].get_sensor_value() <= self.active_distance:
            self.active_flag = True
            print("Stop object active")

    def consider_deactivation(self):
        # if object is farther away than 10cm, deactivates behavior
        print(self.sensobs[0].get_sensor_value())
        if self.sensobs[0].get_sensor_value() > self.stop_distance:
            self.active_flag = True
            print("Stop object not active")

    def sense_and_act(self):
        if self.sensobs[0].get_sensor_value() <= self.stop_distance:
            self.match_degree = 0.5
            self.motor_recommendations = ['S', 0]
        else:
            self.match_degree = 0


# makes the robot drive around until sensors get something.
class DriveAround(Behavior):

    def __init__(self, priority=0.5, active_flag=True, sensobs=None):
        super().__init__(sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.count = 0

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        print("Driving")
        directions = ['R', 'L', 'F', 'B']
        direction = directions[random.randint(0, 3)]
        speed = 25
        self.motor_recommendations = [direction, speed]
        self.count += 1
        print("Count: ", self.count)
        self.match_degree = 0.1


class FollowLines(Behavior):

    def __init__(self, sensobs, priority=1, active_flag=True):
        super().__init__(sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.trigger_value = 0.2

    # Deactivate if no black line is found
    def consider_deactivation(self):
        data = self.sensobs[0].get_sensor_value()
        for value in data:
            if value < self.trigger_value:
                return False
        self.active_flag = False
        return True

    # Activate if black line is found
    def consider_activation(self):
        data = self.sensobs[0].get_sensor_value()
        for value in data:
            if value < self.trigger_value:
                self.active_flag = True
                return True
        return False

    def sense_and_act(self):
        data = self.sensobs[0].get_sensor_value()
        if data[0] < self.trigger_value or data[1] < self.trigger_value:
            self.motor_recommendations = ['L']
        elif data[4] < self.trigger_value or data[5] < self.trigger_value:
            self.motor_recommendations = ['R']
        elif data[2] < self.trigger_value or data[3] < self.trigger_value:
            self.motor_recommendations = ['F']






