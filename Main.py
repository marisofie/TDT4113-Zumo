from BBCON import BBCON
from Behavior import *
from Sensob import *


def main():
    bbcon = BBCON(sensobs=[Distanceob()], behaviours=[Stop(), DriveAround()], active_behaviors=[DriveAround()])
    while bbcon.current_timestamp < 10000:
        bbcon.run_one_timestep()
