import basic_robot.motors as motors


class Motob:

    def __init__(self):
        self.motors = motors.Motors()
        self.value = None

    #updates the motors value and sends direction further
    def update_motor(self, value):
        self.value = value
        self.operationalize()

    #takes a recommendation and makes the motors do the operation.
    def operationalize(self):
        for recom in self.value:
            if recom[0] == 'F':
                self.motors.forward(speed=recom[1]*0.01) #multiply the degrees with 0.01 to get percent for speed
            elif recom[0] == 'B':
                motors.backward(speed=recom[1]*0.01)
            elif recom[0] == 'L':
                motors.left(speed=recom[1]*0.01)
            elif recom[0] == 'R':
                motors.right(speed=recom[1]*0.01)
            elif recom[0] == 'S':
                motors.stop()

    #makes the robot rotate, vector [-1, 1], [L, R].
    def rotate(self, vector):
        self.motors.set_value(vector)



