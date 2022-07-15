from pymycobot import MyCobot
import time


def check_cobot_connection(cobot : MyCobot):
    if not cobot.is_power_on():
        cobot.power_on()
        time.sleep(5)


def angles_in_position(cobot : MyCobot, expected_angles : list):
    curr_angles = cobot.get_angles()

    if len(curr_angles) == 0 or len(expected_angles) == 0:
        raise ValueError()

    converted_angles = []
    for angle in curr_angles:
        converted_angles.append(int(angle))

    for i in range(len(converted_angles)):
        if converted_angles[i] < (expected_angles[i]-3) or converted_angles[i] > (expected_angles[i]+3):
            return False

    return True


def send_angle_smoothly(cobot : MyCobot, joint_id : int, start : int, end : int):
    check_cobot_connection()

    for angle in range(start, end+1):
        cobot.send_angle(joint_id, angle, 100)
        time.sleep(0.1)

    return 0


def move_angles_smoothly(cobot : MyCobot, start_angles : list, end_angles : list):
    prev_angles = start_angles.copy()

    while not angles_in_position(end_angles, cobot):
        next_angles = []

        for i in range(len(prev_angles)):
            if prev_angles[i] > end_angles[i]:
                next_angles.append(prev_angles[i] - 2)
            elif prev_angles[i] < end_angles[i]:
                next_angles.append(prev_angles[i] + 2)
            else:
                next_angles.append(prev_angles[i])

        if len(next_angles) != 6:
            return -1

        cobot.send_angles(next_angles, 100)
        time.sleep(0.1)

        prev_angles = next_angles.copy()

    return 0


def move_to_origin(cobot : MyCobot, speed : int):
    cobot.send_angles([0, 0, 0, 0, 0, 0], speed)
    time.sleep(2)


def compare_angle_lists(angle_list_a : list, angle_list_b : list):
    if len(angle_list_a) != len(angle_list_b):
        return False
    elif len(angle_list_a) != 6 or len(angle_list_b) != 6:
        return False

    for i in range(6):
        if angle_list_a[i] != angle_list_b[i]:
            return False

    return True