# VCU SE LAB - Python Files

### `basic_lead_through.py`

- **Description**: Allows the user to record the position of the cobot after manual manipulation.
- **Arguments**: The cobot's port_id as a string. 
    - Examples: "COM3", "tty/devAMA0"
- **Author**: Haley Currence
- **Version**: 1.0

### `led_test.py`

- **Description**: Tests the ATOM LED.
- **Author**: Elephant Robotics

### `program_generator_automatic.py`

- **Description**: Records the position of the cobot automatically while the cobot is being manually manipulated. Once the user is done manipulating the cobot, the program generates a python script that moves the cobot through the recorded positions.
- **Arguments**: The cobot's port_id as a string. 
    - Examples: "COM3", "tty/devAMA0"
- **Author**: Haley Currence
- **Version**: 1.0

### `program_generator_manual.py`

- **Description**: While the cobot is being manually manipulated, the position of the cobot must be manually recorded via keyboard command. Once the user is done manipulating the cobot, the program generates a python script that moves the cobot through the recorded positions.
- **Arguments**: The cobot's port_id as a string. 
    - Examples: "COM3", "tty/devAMA0"
- **Author**: Haley Currence
- **Version**: 1.0

### `python2BotsTestCode.py`

- **Description**: Script written to test approaches to manipulating two cobots at once.
- **Author**: Haley Currence
- **Version**: 1.0

### `robot_dance.py`

- **Description**: Makes the robot dance.
- **Author**: Elephant Robotics

## `vcupycobot.py` - VCU SE Lab's MyCobot Module

This module contains helpful functions that build off of the original `pymycobot` module provided by Elephant Robotics. The goal of these functions is to make the cobot easier to program, and to provide helpful developer functionality that is missing from the original module.

[Read the `vcupycobot` API](https://github.com/vcuse/elefante/blob/main/Test%20Code/Python/vcupycobot_api.md)