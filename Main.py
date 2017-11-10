from BBCON import BBCON
from Behavior import *
from Sensob import *
#from zumo_button import ZumoButton


def main():
    sensobs = [Distanceob()]
    behavior_stop = Stop(sensobs=sensobs)
    behavior_drive = DriveAround()
    behaviors = [behavior_stop, behavior_drive]
    #button = ZumoButton()

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive, behavior_stop])

    #button.wait_for_press()
    while True:

        bbcon.run_one_timestep()
