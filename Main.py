from BBCON import BBCON
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton


def main():
    button = ZumoButton()
<<<<<<< HEAD
    #reflectance_ob = Reflectanceob()
    #distance_ob = Distanceob()
    #camera_ob = Cameraob()
    ir_prox_ob = IRProximityob()
    sensobs = [ir_prox_ob]
    # behavior_follow_lines = FollowLines(sensobs=[reflectance_ob])
    #behavior_stop_red = StopRed(sensobs=[distance_ob, camera_ob])
    behavior_follow_side = FollowSide(sensobs=[ir_prox_ob])
    behavior_drive = DriveAround()
    behaviors = [behavior_drive, behavior_follow_side]

    count = 0

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive, behavior_follow_side])
=======
    reflectance_ob = Reflectanceob()
    distance_ob = Distanceob()
    sensobs = [distance_ob, reflectance_ob]
    behavior_follow_lines = FollowLines(sensobs=[reflectance_ob])
    behavior_drive = DriveAround()
    behaviors = [behavior_drive, behavior_follow_lines]

    count = 0

    bbcon = BBCON(sensobs=sensobs, behaviors=behaviors, active_behaviors=[behavior_drive, behavior_follow_lines])
>>>>>>> 0d19e7a4796c2f80f2257e65051bc3e1402ac1a1
    button.wait_for_press()
    while count < 100:
        bbcon.run_one_timestep()
        count += 1
