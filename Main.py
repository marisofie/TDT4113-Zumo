from BBCON import BBCON
from Behavior import *
from Sensob import *
#from zumo_button import ZumoButton


def main():
    r_ob = Reflectanceob()
    d_ob = Distanceob()
    sensobs = [d_ob, r_ob]
    behavior_follow_lines = FollowLines(sensobs=[r_ob])
    behavior_drive = DriveAround()
    behaviors = [behavior_drive, behavior_follow_lines]
    #button = ZumoButton()

    count = 0

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive, behavior_follow_lines])
    #button.wait_for_press()
    while count < 50:
        bbcon.run_one_timestep()
        count += 1
