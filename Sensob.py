# Interface between one or more sensors and the behaviours

from basic_robot.camera import *

class Sensob:

    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None

    def update(self):
        data = []
        for sensor in self.sensors:
            sensor.update()
            self.data.append(sensor.get_value())
        self.process_data(data)

    def process_data(self, data):
        pass

    def get_sensor_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


# Subclasses

class Cameraob(Sensob):
    def __init__(self):
        camob = Camera()
        super().__init__([camob])


    def process_data(self, data):
        pass







