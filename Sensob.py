class Sensob:

    def __init__(self, sensors):
        self.sensors = sensors
        self.values = []

    def update(self):
        for s in self.sensors:
            s.update()
            self.values[self.sensors.index(s)] = s.get_value

    def get_value(self):
        return self.values

    def reset(self):
        for s in self.sensors:
            s.reset()


#Kanskje vi lager flere subklasser senere når vi vet hva vi vil at roboten skal gjøre. F. eks. med kamera