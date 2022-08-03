# Cobot Connection Client and Server

The goal of these scripts is to create a way around the wifi connection problems found within Elephant Robotic's `pymycobot` module and the MyCobot 280 M5. 

The connection server runs on the device connected to the cobot via serial port, and the client server runs on the device trying to reach the server over wifi. 

### Command Structure/Design

The server command design was inspired by CPU command design. 
- The first 3 bits of the command make up the command code, and correspond to some command on the cobot. 
- The rest of the bits are the parameters of that command.

| Command | Command Code |  Speed | Joint ID | Angle | Angles | Coordinate | Coordinates
| --- | --- | --- | --- | --- | --- | --- | --- |
| Set Movement Speed | 000 | Bits 3 through 10 | N/A | N/A | N/A | N/A | N/A |
| Move One Joint to an Angular Position | 001 | N/A | Bits 3 through 5 | Bits 6 through 14 | N/A | N/A | N/A |
| Move All Joints to Angular Positions | 010 | N/A | N/A | N/A | Bits 3 through 53 | N/A | N/A |
| Move One Joint to a Coordinate[^1] | 011 | N/A | N/A | N/A | N/A | N/A | N/A |
| Move All Joints to Coordinates[^1] | 100 | N/A | N/A | N/A | N/A | N/A | N/A |
| Unreserved | 101 | N/A | N/A | N/A | N/A | N/A | N/A |
| Unreserved | 110 | N/A | N/A | N/A | N/A | N/A | N/A |
| Unreserved | 111 | N/A | N/A | N/A | N/A | N/A | N/A |

### Speed

Speed is converted from decimal into a 8-bit binary number.

### Angles
Angles are converted from their decimal values into 9-bit binary numbers. A sign bit is used to determine if the angle is positive (0) or negative (1).

### Coordinates

(TBD)

[^1]: These commands are not yet implemented

--- 

## `connection_client.py`

This client was created to provide a user-friendly interface for the server connection. The server can accept commands without this interface.

## `connection_server.py`

The connection server is a TCP server that interprets the TCP messages sent to it based on the command structure detailed above. 

#### Execution Steps:
1. A command is recieved via TCP packets.
2. The command is decoded into a corresponding function in the `pymycobot` module and its associated parameters. 
3. The function is then executed on the connected cobot.

Message buffer inspired by:
- https://stackoverflow.com/questions/29023885/python-socket-readline-without-socket-makefile