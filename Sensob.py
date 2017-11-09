# Interface between one or more sensors and the behaviours

from basic_robot.camera import *
from basic_robot.ultrasonic import *
from basic_robot.reflectance_sensors import *


class Sensob:

    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None

    def update(self):
        data = []
        for sensor in self.sensors:
            sensor.update()
            self.data.append(sensor.get_value())
            data.append(sensor.get_value())
        self.process_data(data)

    def process_data(self, data):
        pass
        self.value = data[0]

    def get_sensor_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


# Subclasses

# Camera object used to detect the color red
class Cameraob(Sensob):
    def __init__(self):
        camob = Camera()
        super().__init__([camob])
        self.camob = Camera()
        super().__init__([self.camob])

        # Bounds of the color red in RGB
        self.upper = (256, 40, 40)
        self.lower = (50, 0, 0)

    # Measures the percentage of pixels that are in the red spectrum
    def process_data(self, data):
        pass
        redCount = 0
        img = data[0]
        for pixel in img:
            tempCount = 0
            for i in range(3):
                if self.lower[i] < pixel[i] < self.upper[i]:
                    tempCount += 1
            if tempCount == 3:
                redCount += 1
        self.value = redCount / self.camob.get_size()


# Object used to  measure distance in cm
class Distanceob(Sensob):
    def __init__(self):
        self.distanceob = Ultrasonic()
        super().__init__([self.distanceob])


# Object used to follow a black line
class Reflectanceob(Sensob):
    def __init__(self):
        self.Reflectanceob = ReflectanceSensors()
        super().__init__([self.Reflectanceob])








