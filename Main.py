from BBCON import BBCON
from Behavior import *
from Sensob import *


def main():
    sensobs = [Distanceob()]
    behavior_stop = Stop(sensobs=sensobs)
    behavior_drive = DriveAround()
    behaviors = [behavior_stop, behavior_drive]

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive])

    while bbcon.current_timestamp < 10000:
        bbcon.run_one_timestep()
