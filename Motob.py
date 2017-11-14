from motors import Motors

# Interface between a behavior and one or more Motobs


class Motob:

    def __init__(self):
        self.motors = Motors()
        self.value = None

    # Updates the motors value and sends direction further
    def update_motor(self, value):
        self.value = value
        print(self.value)
        self.operationalize()

    # Takes a recommendation and makes the motors do the operation.
    def operationalize(self):
        recom = self.value
        if recom[0] == 'F':
            self.motors.forward(speed=recom[1]*0.01, dur=1)    # multiply the degrees with 0.01 to get percent for speed
        elif recom[0] == 'B':
            self.motors.backward(speed=recom[1]*0.01, dur=1)
        elif recom[0] == 'L':
            self.motors.left(speed=recom[1]*0.01, dur=1)
        elif recom[0] == 'R':
            self.motors.right(speed=recom[1]*0.01, dur=1)
        elif recom[0] == 'S':
            self.motors.stop()

    # Makes the robot rotate, vector [-1, 1], [L, R].
    def rotate(self, vector):
        self.motors.set_value(vector)

    # Optional stop method, duplicate in operationalize()
    def stop(self):
        self.motors.stop()



