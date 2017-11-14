from BBCON import BBCON
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton


def main():
    button = ZumoButton()
    reflectance_ob = Reflectanceob()
    distance_ob = Distanceob()
    sensobs = [distance_ob, reflectance_ob]
    behavior_follow_lines = FollowLines(sensobs=[reflectance_ob])
    behavior_drive = DriveAround()
    behaviors = [behavior_drive, behavior_follow_lines]

    count = 0

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive, behavior_follow_lines])
    button.wait_for_press()
    while count < 100:
        bbcon.run_one_timestep()
        count += 1
