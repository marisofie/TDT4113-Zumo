# Interface between one or more sensors and the behaviors

from camera import *
from reflectance_sensors import *
from irproximity_sensor import *
from ultrasonic import *
from imager2 import Imager


class Sensob:
    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None
        self.behaviors = []

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def get_behaviors(self):
        return self.behaviors

    def update(self):
        data = []
        for sensor in self.sensors:
            sensor.update()
            data.append(sensor.get_value())
        print("Data: ", data)
        self.process_data(data)

    def process_data(self, data):
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
        self.camob = Camera()
        super().__init__([self.camob])

        # Bounds of the color red in RGB
        self.upper = (256, 40, 40)
        self.lower = (50, 0, 0)

    # Measures the percentage of pixels that are in the red spectrum
    def process_data(self, data):
        print("Datatype: ", data)
        red_count = 0
        image = Imager(image=data[0])
        pixel_list = []
        for x in range(image.xmax):
            for y in range(image.ymax):
                pixel_list.append(image.get_pixel(x, y))
        for pixel in pixel_list:
            temp_count = 0
            for i in range(3):
                if self.lower[i] < pixel[i] < self.upper[i]:
                    temp_count += 1
            if temp_count == 3:
                red_count += 1
        self.value = red_count / self.camob.get_size()


# Object used to  measure distance in cm, data = [12]
class Distanceob(Sensob):
    def __init__(self):
        self.distanceob = Ultrasonic()
        super().__init__([self.distanceob])


# Object used to follow a black line, data = [[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]
class Reflectanceob(Sensob):
    def __init__(self):
        self.Reflectanceob = ReflectanceSensors(True)
        super().__init__([self.Reflectanceob])


class IRProximityob(Sensob):
    def __init__(self):
        self.IRProximityob = IRProximitySensor()
        super().__init__([self.IRProximityob])

if __name__ == '__main__':
    while True:
        camSensob = Cameraob()
        camSensob.update()