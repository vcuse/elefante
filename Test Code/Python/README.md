# VCU SE LAB - Python Files

### `basic_lead_through.py`

- **Description**: 
- **Author**: Haley Currence
- **Version**: 1.0

### `led_test.py`

- **Description**: 
- **Author**: Elephant Robotics

### `program_generator_automatic.py`

- **Description**: 
- **Author**: Haley Currence
- **Version**: 1.0

### `program_generator_manual.py`

- **Description**: 
- **Author**: Haley Currence
- **Version**: 1.0

### `python2BotsTestCode.py`

- **Description**: 
- **Author**: Haley Currence
- **Version**: 1.0

### `robot_dance.py`

- **Description**: 
- **Author**: Elephant Robotics

## vcupycobot - VCU SE Lab's MyCobot Module

This module contains helpful functions that build off of the original `pymycobot` model provided by Elephant Robotics. The goal of these functions is to make the cobot easier to program, and to provide helpful developer functionality that is missing from the original module.

### example_function
- **Description**: Description Here
- **Parameters**: 
    - Parameter Descriptions Here
- **Returns**: Return Value Descriptions Here
- **Usage Examples**:
    - Usage Examples Here

---

### check_cobot_connection()
- **Description**: Checks if the cobot is "on". If the cobot is not "on", it turns on the cobot.
- **Parameters**: 
    - N/A
- **Returns**: 
    - N/A
- **Usage Examples**:
    - `vcupycobot.check_cobot_connection()`

### angle_in_position(cobot : MyCobot, joint_id : int, expected_angle : int)
- **Description**: Description Here
- **Parameters**: 
    - Parameter Descriptions Here
- **Returns**: Return Value Descriptions Here
- **Usage Examples**:
    - Usage Examples Here

### angles_in_position(cobot : MyCobot, expected_angles : list)
- **Description**: Checks to see if the angular position of each of the joints of the indicated cobot matches the angles indicated by the list of expected angles. 
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

### send_angle_smoothly(cobot : MyCobot, joint_id : int, start : int, end : int, speed : int)
- **Description**: Sends a procession of angles to the cobots in succession to the specified joint from the indicated starting angular position to the indicated ending angular position. This method produces a more graceful angular movement instead of the quick movements that can be produced by the `pymycobot` modules' `send_angle` function. 
    - If the current angle of the specified joint does not match the starting angle, the cobot will move to the starting angle.
- **Parameters**:
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `joint_id : int` - The identification number of the joint you intend to move. Accepts ID numbers 1 - 6. 
    - `start : int` - The expected starting angle of the cobot's joint, the value being between -180 degrees and 180 degrees.
    - `end : int` - The expected ending angle of the cobot's joint, the value being between -180 degrees and 180 degrees.
    - (Optional) `speed : int` - The speed at which the cobot's joint will move to reach each of the consecutive angles. Default value of 100.
- **Returns**:
    - `0` if the joint could reach the end angle successfully
    - `-1` if the joint could not reach the end angle successfully
- **Usage Examples**:
    - `vcupycobot.send_angle_smoothly(mc, 1, 0, 180)`
    - `vcupycobot.send_angle_smoothly(mc, 1, -180, 180, 50)`

### send_angles_smoothly(cobot : MyCobot, start_angles : list, end_angles : list)
- **Description**: Sends a procession of angles to the cobots in succession from the indicated starting angular positions to the indicated ending angular positions. This method produces a more graceful angular movement instead of the quick movements that can be produced by the `pymycobot` modules' `send_angles` function. 
    - If the current angle of the cobot does not match the starting angles, the cobot will move to the starting angles.
- **Parameters**:
    - `cobot : MyCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `start_angles : list` - The expected starting angle of the cobot's joint, the value being between -180 degrees and 180 degrees.
    - `end_angles : list` - The expected ending angle of the cobot's joint, the value being between -180 degrees and 180 degrees.
- **Returns**:
    - `0` if the cobot could reach the end angle successfully
    - `-1` if the cobot could not reach the end angle successfully
- **Usage Examples**:
    - `vcupycobot.send_angles_smoothly(mc, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1])`
    - `vcupycobot.send_angles_smoothly(cobot, cobot.get_angles(), [-36, 20, 0, 18, 68, -180])`

### move_to_origin(cobot : MyCobot, speed : int)
- **Description**: Moves the cobot to its origin. The origin of each cobot's angles is 0 degrees (where the knotches in each joint line up). 
- **Parameters**:
    - `cobot : myCobot` - An instance of a MyCobot object corresponding to a cobot connected via serial port.
    - `speed : int` - The speed at which the cobot will move to reach the origin, from 0 to 100.
- **Returns**:
    - N/A
- **Usage Examples**:
    - `vcupycobot.move_to_origin(100)`
    - `vcupycobot.move_to_origin(50)`

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