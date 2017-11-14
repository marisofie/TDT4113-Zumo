from BBCON import BBCON
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton


def main():
    button = ZumoButton()
    ir_prox_ob = IRProximityob()

    count = 0

    bbcon = BBCON()

    behavior_follow_side = FollowSide(bbcon=bbcon, sensobs=[ir_prox_ob])
    behavior_drive = DriveAround(bbcon=bbcon)

    bbcon.add_behavior(behavior_follow_side)
    bbcon.add_behavior(behavior_drive)
    bbcon.add_sensob(ir_prox_ob)
    bbcon.activate_behavior(behavior_follow_side)
    bbcon.activate_behavior(behavior_drive)

    button.wait_for_press()
    while count < 100:
        bbcon.run_one_timestep()
        count += 1


def main2():
    button = ZumoButton()
    distance_ob = Distanceob()
    camera_ob = Cameraob()

    count = 0

    bbcon = BBCON()

    behavior_stop_red = StopRed(bbcon=bbcon, sensobs=[distance_ob, camera_ob])
    behavior_drive = DriveAround(bbcon=bbcon)
    bbcon.add_behavior(behavior_stop_red)
    bbcon.add_behavior(behavior_drive)
    bbcon.add_sensob(distance_ob)
    bbcon.add_sensob(camera_ob)
    bbcon.activate_behavior(behavior_stop_red)
    bbcon.activate_behavior(behavior_drive)

    button.wait_for_press()
    while count < 100:
        bbcon.run_one_timestep()
        count += 1


def main3():
    button = ZumoButton()
    distance_ob = Distanceob()
    camera_ob = Cameraob()
    ir_prox_ob = IRProximityob()

    count = 0

    bbcon = BBCON()

    behavior_stop_red = StopRed(bbcon=bbcon, sensobs=[distance_ob, camera_ob])
    behavior_follow_side = FollowSide(bbcon=bbcon, sensobs=[ir_prox_ob])
    behavior_drive = DriveAround(bbcon=bbcon)
    bbcon.add_behavior(behavior_stop_red)
    bbcon.add_behavior(behavior_drive)
    bbcon.add_behavior(behavior_follow_side)
    bbcon.add_sensob(distance_ob)
    bbcon.add_sensob(camera_ob)
    bbcon.add_sensob(ir_prox_ob)
    bbcon.activate_behavior(behavior_follow_side)
    bbcon.activate_behavior(behavior_stop_red)
    bbcon.activate_behavior(behavior_drive)

    button.wait_for_press()
    while count < 100:
        bbcon.run_one_timestep()
        count += 1
