class Behavior:
    def __init__(self, bbcon, sensobs, priority, active_flag):
        self.bbcon = bbcon  # Pointer to BBCON-object
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

    def get_sensobs(self):
        return self.sensobs

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
    def __init__(self, bbcon, priority=1, active_flag=True, sensobs=[]):
        super().__init__(bbcon=bbcon, priority=priority, sensobs=sensobs, active_flag=active_flag)
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
    def __init__(self, bbcon, priority=1, active_flag=True, sensobs=[]):
        super().__init__(bbcon=bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.active_distance = 50
        self.stop_distance = 20
        self.min_red = 0.3
        self.motor_recommendations = []

    def consider_activation(self):
        # if object is closer than stop discance in cm
        # must remember that sensobs[0] contains distance
        if self.sensobs[0].get_sensor_value() <= self.active_distance:
            self.active_flag = True
            self.bbcon.add_sensob(self.sensobs[1])

    def consider_deactivation(self):
        # if object is farther away than stop distance, deactivates behavior
        if self.sensobs[0].get_sensor_value() > self.stop_distance:
            self.active_flag = False
            self.bbcon.remove_sensob(self.sensobs[1])

    def sense_and_act(self):
        percent_red = self.sensobs[1].get_sensor_value()
        if percent_red > self.min_red and self.sensobs[0].get_sensor_value() <= self.stop_distance:
            self.match_degree = percent_red
            self.motor_recommendations = [('S', 0)]
        else:
            self.match_degree = 0


class Stop(Behavior):
    def __init__(self, bbcon, priority=1, active_flag=True, sensobs=[]):
        super().__init__(bbcon=bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
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
    def __init__(self, bbcon, priority=0.5, active_flag=True, sensobs=[]):
        super().__init__(bbcon=bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.count = 0

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        print("Driving")
        self.motor_recommendations = ['F', 20]
        self.count += 1
        print("Count: ", self.count)
        self.match_degree = 0.1


class FollowSide(Behavior):
    def __init__(self, bbcon, sensobs=[], priority=0.8, active_flag=True):
        super().__init__(bbcon=bbcon, sensobs=sensobs, priority=priority, active_flag=active_flag)
        self.motor_recommendations = []

    def consider_deactivation(self):
        self.active_flag = True

    def consider_dactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        data = self.sensobs[0].get_sensor_value()
        print("Data1: ", data[0])
        print("Data2: ", data[1])
        if data[0] and data[1]:
            self.motor_recommendations = ['B', 30]
            self.match_degree = 0.5
        elif data[0]:
            self.motor_recommendations = ['L', 30]
            self.match_degree = 0.5
        elif data[1]:
            self.motor_recommendations = ['R', 30]
            self.match_degree = 0.5
        else:
            self.match_degree = 0