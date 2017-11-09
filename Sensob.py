# Interface between one or more sensors and the behaviours


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


#Kanskje vi lager flere subklasser senere når vi vet hva vi vil at roboten skal gjøre. F. eks. med kamera