# Setup and Development Documentation for myCobot 280 M5

[ER myCobot 280 M5](https://www.elephantrobotics.com/en/mycobot-en/)

## Documentation
- [Documentation](https://docs.elephantrobotics.com/docs/gitbook-en/)
    - [Cobot Hardware Setup for First Time Use](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.3-quick_start.html)
- [Video Tutorials](https://www.elephantrobotics.com/en/support-280-m5-en/)

## Basic Drivers and myStudio

### Basic Drivers

[Driver Diagram](https://docs.elephantrobotics.com/docs/gitbook-en/resourse/4-BasicApplication/4.1/4.1-mystudio1.jpg)

[How to Comform Which Basic Chip is in the Robot](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip)

Basic Driver for myCobot 280 M5: CP210x
- [Windows 10](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_Windows.zip)
- [Linux](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_Linux.zip)
- [MacOS](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_MacOS.zip)

New Basic Driver for myCobot 280 M5: **CH9102** CP34X
- [Windows 10](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_CDC_Windows.exe)
- [Windows Server](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_SER_Windows.exe)
- [MaxOS](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_MacOS.dmg)

Atom Serial Port Driver:
- [Windows 10](https://download.elephantrobotics.com/software/drivers/CDM21228_Setup.zips)

### [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)

myStudio is a "one-stop application platform for myRobot/myCobot and other robots."
* Handles firmware installations and updates
* Contains robot tutorials on use, maintenance, and repair

#### Downloads:
- [Official Download from Elephant Robotics](https://www.elephantrobotics.com/en/downloads/)


#### Steps to Run a Program:
* Make sure you have all drivers installed onto your computer 

_Note to Self: determine if the CP34X driver will run on its own. Had to install both before I got it to work. - Haley_

* Make sure the miniRobot firmware running on Basic (the base of the cobot) is up-to-date
    * Flash the newest release via myStudio
* On the Basic (the computer at the base of the cobot), navigate to the "Transponder" screen. 
* You are now ready to run your desired program.

#### Running on Bluetooth

myCobot BLE <- bluetooth server

## Development Languages

### [myBlockly](https://docs.elephantrobotics.com/docs/gitbook-en/5-ProgramingApplication-myblockly-uiflow-mind/5.1-myblockly/)
myBlockly is a "Puzzle programming [drag-and-drop/block-based programming] software based on python enviornments and pymycobot dependent libraries."
* Requires a completely setup python enviornment
* Also generates python script based on blockly code

#### Downloads 
- [Official Download from Elephant Robotics](https://www.elephantrobotics.com/en/downloads/)
- [From GitHub](https://github.com/elephantrobotics/myblockly-package/releases/tag/v0.0.6)

#### Notes
_Blockly code isn't running on the cobot despite the Python code running just fine. Weird. - Haley_

---

### [UIFlow](https://docs.elephantrobotics.com/docs/gitbook-en/5-ProgramingApplication-myblockly-uiflow-mind/5.2-UIFlow/)
UIFlow is a "programming tool specifically designed for the M5 hardware system using [Blockly](https://developers.google.com/blockly) and Python code".
- Typically used for primary/secondary schools (?) and IoT devices

[Web-Based IDE](https://flow.m5stack.com/)

#### Downloads 
- [Official Windows 64-bit Desktop Application Download from Elephant Robotics](https://static-cdn.m5stack.com/resource/software/UIFlow-Desktop-IDE.zip)

#### Documentation
- Official Documentation is in Chinese, but has some starter videos on the [Web IDE](https://flow.m5stack.com/).
    - [For the M5StickC](https://shop.m5stack.com/products/stick-c?variant=17203451265114)
        - [Documentation (Chinese)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/M5StickC_Guide.pdf)
    - [For the M5GO IoT Device](https://shop.m5stack.com/products/m5go-iot-starter-kit-stem-education?variant=16804754260058)
        - [Documentation (Chinese)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/UIFlow-Book-zh_cn.pdf)

---

### [RoboFlow Operating System](https://docs.elephantrobotics.com/docs/gitbook-en/6-ApplicationBaseRoboFlow/)

- Built to be run on teaching pendants for Elephant Robotics cobots.

#### Downloads:
- [Official Download from Elephant Robotics](https://www.elephantrobotics.com/en/downloads/)

#### Documentation
- [Operation and Programming Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/Operation-and-Programming-Manual-EN.pdf)
- RoboFlowScript: C-based programming language to "control the robot" (not completely described)
    - [RoboFlowScript Programming Language Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/1-RoboFlowScript_Manual.pdf)
- Python API for Remote Robot Control
    - [RoboFlow Python API](https://static.elephantrobotics.com/wp-content/uploads/2019/06/2-RoboFlow-API-python.pdf)
    - [RoboFlow Socket Communication Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/3-RoboFlow-CommunicationSocket.pdf): Documentation for the Python socket commands

---

### Python

* [Installing the `pymycobot` library](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.1_download.html#714-preparations)

#### Downloads:
- [pymycobot Github](https://github.com/elephantrobotics/pymycobot)


#### Documentation
 * [`pymycobot` library documentation from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/)
 * [Python API for myCobot](https://pypi.org/project/pymycobot/)

Example Library Use in Python:
```python
from pymycobot import MyCobot, Angle, Coord, utils
```

Example Use of Coordinates and Joing Angles: Cobot Sits and Stands Up Again
```python
from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('COM3', 115200)
mc.power_on()
print("cobot is now active")

print("moving bot via coordinates")

coords = mc.get_coords()
print(coords)

mc.send_coords([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 80, 1)
time.sleep(5)

coords = mc.get_coords()
print(coords)

print("moving bot via angles")

angles = mc.get_angles()
print(angles)

mc.send_angles([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 80)
time.sleep(5)

angles = mc.get_angles()
print(angles)
```

#### Notes:
- The Python API is not complete.
- Servos will lock but be manuverable after every movement command.
    - Servos can be manually unlocked via `mc.release_all_servos()`
    - Servos will move back to its original position in this state

---

### C#

* Recommends using VSCode 2019
    * _Got it running in Visual Studio 2022 with no drivers - Haley_
* [Source Code](https://github.com/elephantrobotics/Mycobot.csharp)
* [Dynamic Library](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html)
* [Recommended Steps for Running in Windows](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html#922-running-in-windows)

#### Working with Unity
- Player API compatibility level must be changed to either ".NET framework" or ".NET 2.0" to recognize System.IO.Ports. 
    - System.IO.Ports is what Elephant Robotics use to open the serial port
    - https://forum.unity.com/threads/cant-use-system-io-ports.141316/
- Import the MyCobot.cs script from the github release (source code above).
- Add two dependencies to your script:
    - To use the cobot: `using Mycobot.csharp`
    - To sleep: `using System.Threading`

Current Unity Problem: Unity not communicating with the cobot
- Serial Port is opening correctly
- Angles not being sent

Researching Solutions
- Switch to IL2CPP scripting backend instead of Mono
    - No Response
- Figure out how to include .NET 2.0 libraries
    - Same error as before; cant see the System.IO namespace

#### Notes:
- Must still navigate to the "Transponder" page to properly send angles/coord. to the cobot; however, it automatically reboots the computer (Basic) after each use. This means you have to navigate to the "Transponder" page every time you want to run your program.
    - This doesnt happen in Python.
    - Is there a way to turn this off?
    - Looked in the [Microsoft Doc](https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-6.0) and the reboot signal doesnt seem to be coming from here



---

### [ROS](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/)

* Install Firmware using [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)
* Only need to build a ROS enviornment for the MyCobot 280-M5

[ROS Wiki](http://wiki.ros.org/Documentation)

#### Setting Up ROS and myCobot:
1. Build your ROS Enviornment 
    * [ROS Enviornment Building Instructions by Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#1-ros-environment-building)
        * All ROS versions are supported
            - Ubuntu 16.04 / ROS Kinetic
            - Ubuntu 18.04 / ROS Melodic
            - Ubuntu 20.04 / ROS Noetic
        * ROS2
            - Ubuntu 20.04 / ROS Foxy
    * [Instructions from ROS Wiki](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
2. Install the MoveIt function packages
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#1-ros-environment-building)
    * [Install/Build Instructions from ROS](https://moveit.ros.org/install/)
3. Create a ROS workspace
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#21-precondition)
4. Install `mycobot_ros`
    * [GitHub Repository](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#2-mycobotros-installation)
    * [Installing the Package](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#22-installing-the-package)
        - Recommends using `pip`

#### 3D Visualization using `rviz`

* Installing `rviz`
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/)
    * [Official ROS Documentation](http://wiki.ros.org/rviz)

Configure your ROS enviornment and run the following to test the visualization for myCobot 280-M5:
```
roslaunch src/mycobot_ros/mycobot_280/launch/test.launch
```

#### Using `mycobot_ros`
* [Arm Control and Following](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1242-control-and-following-of-the-robot-arm)
* [Simple GUI Control Interface](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1244-gui-control)
    * [Keyboard Control](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#12441-keyboard-control)
* [Camera Control](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1245-vision)

#### Using `mycobot_ros` and `MoveIt`
* [Documentation on integrated MoveIt Functions](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.5-Moveit/)

---

**M5 Series Precondition for Use:** \
    "M5 series version the bottom Basic is programmed to miniRobot , select the Transponder function, and the end ATOM is programmed to the latest version of atomMain (the factory default has been programmed)"

_Not sure what they are trying to say here. - Haley_
