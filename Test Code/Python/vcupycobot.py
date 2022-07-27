from pymycobot import MyCobot
import time
import traceback

"""
### check_cobot_connection()
- **Description**: Checks if the cobot is "on". If the cobot is not "on", it turns on the cobot.
- **Parameters**: 
    - N/A
- **Returns**: 
    - N/A
- **Exceptions**:
    - Raises a connection exception when the cobot's angles cannot be read. (A symptom of not being connected to ATOM.)
- **Usage Examples**:
    - `vcupycobot.check_cobot_connection()`
"""
def check_cobot_connection(cobot : MyCobot):
    if not cobot.is_power_on():
        cobot.power_on()
        time.sleep(5)

    curr_angles = cobot.get_angles()

    if len(curr_angles) == 0:
        raise Exception("The current position of the cobot could not be read. Check your cobot's connection.")


"""
### angle_in_position(cobot : MyCobot, joint_id : int, expected_angle : int)
- **Description**: Checks to see if the angular position of each of the specified joint of the indicated cobot matches 
    the expected angle.
- **Parameters**: 
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `joint_id : int` - The identification number of the joint you intend to move. Accepts ID numbers 1 - 6. 
    - `expected_angle : int` - A list of 6 angular values, each value being between -180 degrees and 180 degrees.
- **Returns**:
    - A Boolean value: 
        - `True`, if the position of the joint matches the expected angle;
        - `False`, if the position of the joint does not match the expected angle.
- **Usage Examples**:
    - `while not vcupycobot.angle_in_position(mc, 1, angle):`
    - `if vcupycobot.angles_in_position(cobot, 2, 0):`
"""
def angle_in_position(cobot : MyCobot, joint_id : int, expected_angle : int):
    curr_angles = cobot.get_angles()

    if len(curr_angles) == 0:
        curr_angles = cobot.get_angles()
        if len(curr_angles) == 0:
            raise Exception("The current position of the cobot could not be read. Check your cobot's connection.")
    if expected_angle < -180 or expected_angle > 180:
        raise ValueError("The inputted angle is not within range.")

    curr_angle = int(curr_angles[joint_id-1])

    if curr_angle < (expected_angle-3) or curr_angle > (expected_angle+3):
        return False

    return True


"""
### angles_in_position(cobot : MyCobot, expected_angles : list)
- **Description**: Checks to see if the angular position of each of the joints of the indicated cobot matches the angles
    indicated by the list of expected angles. 
- **Parameters**:
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `expected_angles : list` - A list of 6 angular values, each value being between -180 degrees and 180 degrees.
- **Returns**: 
    - A Boolean value: 
        - `True`, if the position of the cobot matches the expected angles;
        - `False`, if the position of the cobot does not match the expected angles.
- **Usage Examples**:
    - `while not vcupycobot.angles_in_position(mc, angle):`
    - `if vcupycobot.angles_in_position(cobot, [0, 0, 0, 0, 0, 0]):`
"""
def angles_in_position(cobot : MyCobot, expected_angles : list):
    curr_angles = cobot.get_angles()

    if len(curr_angles) == 0:
        curr_angles = cobot.get_angles()
        if len(curr_angles) == 0:
            raise Exception("The current position of the cobot could not be read. Check your cobot's connection.")
    if len(expected_angles) == 0:
        raise ValueError(expected_angles + " does not contain 6 angles.")

    converted_angles = []
    for angle in curr_angles:
        converted_angles.append(int(angle))

    for i in range(len(converted_angles)):
        if converted_angles[i] < (expected_angles[i]-3) or converted_angles[i] > (expected_angles[i]+3):
            return False

    return True


"""
### send_angle_smoothly(cobot : MyCobot, joint_id : int, start : int, end : int, speed : int, delay : float)
- **Description**: Sends a procession of angles to the cobots in succession to the specified joint from the indicated 
    starting angular position to the indicated ending angular position. This method produces a more graceful angular 
    movement instead of the quick movements that can be produced by the `pymycobot` modules' `send_angle` function. 
    - If the current angle of the specified joint does not match the starting angle, the cobot will move to the starting 
        angle.
- **Parameters**:
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `joint_id : int` - The identification number of the joint you intend to move. Accepts ID numbers 1 - 6. 
    - `start : int` - The expected starting angle of the cobot's joint, the value being between -180 degrees and 180 
        degrees.
    - `end : int` - The expected ending angle of the cobot's joint, the value being between -180 degrees and 180 degrees.
    - (Optional) `speed : int` - The speed at which the cobot's joint will move to reach each of the consecutive angles.
        Default value of 100.
    - (Optional) `delay : float` - The delay, in seconds, between movement commands. Default value of 0.001 (1 ms).
- **Returns**:
    - `0` if the joint could reach the end angle successfully
    - `-1` if the joint could not reach the end angle successfully
- **Usage Examples**:
    - `vcupycobot.send_angle_smoothly(mc, 1, 0, 180)`
    - `vcupycobot.send_angle_smoothly(mc, 1, -180, 180, 50)`
"""
def send_angle_smoothly(cobot : MyCobot, joint_id : int, start : int, end : int, speed : int = 100, delay : float = 0.001):
    check_cobot_connection(cobot)

    try:
        if not angle_in_position(cobot, joint_id, start):
            while not angle_in_position(cobot, joint_id, start):
                cobot.send_angle(joint_id, start, 100)

        for angle in range(start, end+1):
            cobot.send_angle(joint_id, angle, speed)
            time.sleep(delay)
    except Exception as err:
        print("\t", end="")
        traceback.print_exc()
        return -1

    return 0


"""
### send_angles_smoothly(cobot : MyCobot, start_angles : list, end_angles : list, speed : int, delay : float)
- **Description**: Sends a procession of angles to the cobots in succession from the indicated starting angular 
    positions to the indicated ending angular positions. This method produces a more graceful angular movement instead 
    of the quick movements that can be produced by the `pymycobot` modules' `send_angles` function. 
    - If the current angle of the cobot does not match the starting angles, the cobot will move to the starting angles.
- **Parameters**:
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `start_angles : list` - The expected starting angle of the cobot's joint, the value being between -180 degrees 
        and 180 degrees.
    - `end_angles : list` - The expected ending angle of the cobot's joint, the value being between -180 degrees and 
        180 degrees.
    - (Optional) `speed : int` - The speed at which the cobot's joint will move to reach each of the consecutive angles.
        Default value of 100.
    - (Optional) `delay : float` - The delay, in seconds, between movement commands. Default value of 0.1 (100 ms).
- **Returns**:
    - `0` if the cobot could reach the end angle successfully
    - `-1` if the cobot could not reach the end angle successfully
- **Usage Examples**:
    - `vcupycobot.send_angles_smoothly(mc, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1])`
    - `vcupycobot.send_angles_smoothly(cobot, cobot.get_angles(), [-36, 20, 0, 18, 68, -180])`
"""
def send_angles_smoothly(cobot : MyCobot, start_angles : list, end_angles : list, speed : int = 50, delay : float = 0.01):
    check_cobot_connection(cobot)

    try:
        if not angles_in_position(cobot, start_angles):
            while not angles_in_position(cobot, start_angles):
                cobot.send_angle(start_angles, speed)

        prev_angles = start_angles.copy()

        while not angles_in_position(cobot, end_angles):
            next_angles = []

            for i in range(len(prev_angles)):
                if prev_angles[i] > end_angles[i]:
                    next_angles.append(prev_angles[i] - 1)
                elif prev_angles[i] < end_angles[i]:
                    next_angles.append(prev_angles[i] + 1)
                else:
                    next_angles.append(prev_angles[i])

            if len(next_angles) != 6:
                return -1

            cobot.send_angles(next_angles, speed)
            time.sleep(delay)

            prev_angles = next_angles.copy()
    except Exception as err:
        print("\t", end="")
        traceback.print_exc()
        return -1

    return 0


"""
### move_to_origin(cobot : MyCobot, speed : int)
- **Description**: Moves the cobot to its origin. The origin of each cobot's angles is 0 degrees (where the knotches in 
    each joint line up). 
- **Parameters**:
    - `cobot : myCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `speed : int` - The speed at which the cobot will move to reach the origin, from 0 to 100.
- **Returns**:
    - N/A
- **Usage Examples**:
    - `vcupycobot.move_to_origin(100)`
    - `vcupycobot.move_to_origin(50)`
"""
def move_to_origin(cobot : MyCobot, speed : int):
    cobot.send_angles([0, 0, 0, 0, 0, 0], speed)
    time.sleep(2)


"""
### compare_angle_lists(angle_list_a : list, angle_list_b : list)
- **Description**: Compares two list of angular values.
- **Parameters**:
    - `angle_list_a : list` - A list of angles.
    - `angle_list_b : list` - A list of angles.
- **Returns**:
    - `True` if both lists are the same.
    - `False` if both lists are different or either list does not contain 6 angles.
- **Usage Examples**:
    - `vcupycobot.compare_angle_list([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])` - returns `True`
    - `vcupycobot.compare_angle_list(mc.get_angles(), [])` - returns `False`
"""
def compare_angle_lists(angle_list_a : list, angle_list_b : list):
    if len(angle_list_a) != len(angle_list_b):
        return False
    elif len(angle_list_a) != 6 or len(angle_list_b) != 6:
        return False

    for i in range(6):
        if angle_list_a[i] != angle_list_b[i]:
            return False

    return True

"""
In Progress
"""
def setup_connection_vcu_lan():
    return 0

