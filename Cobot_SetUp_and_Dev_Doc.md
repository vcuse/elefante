# Setup and Development Documentation for myCobot 280 M5

[ER myCobot 280 M5](https://www.elephantrobotics.com/en/mycobot-en/)

## About

(TBA)

## Official Documentation
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
- [Download from GitHub](https://github.com/elephantrobotics/myStudio)
    - [Latest Release](https://github.com/elephantrobotics/myStudio/releases/)


#### Steps to Run a Program:
1. Make sure you have all drivers installed onto your computer.
    * _May not be necessary. Both Python and C# can be run on the cobot without having drivers installed on Windows. - Haley_
2. Make sure the miniRobot firmware running on Basic (the base of the cobot) is up-to-date
    * Flash the newest release via myStudio
    * Newest release: **miniRobot v2.0**
3. On the Basic (the computer at the base of the cobot), navigate to the "Transponder" screen. 

##### Connecting to the Cobot via Serial Port

##### Controlling the Cobot Arm via TCP/IP

[Instructions on how to connect to the cobot wirelessly via TCP/IP](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.6_TCPIP.html)

##### Running on Bluetooth:

myCobot BLE <- bluetooth server


## Rotational Movement

Elephant Robotics Documentation: Each Joint's Rotational Degrees of Movement: -160 deg. to 160 deg. or -165 deg to 165 deg

_TODO: Retest these findings on new miniRobot version and C#. - Haley_

In Python:
- Rotational Limit on Angles: 190 deg or -190 deg
    - 190 degrees = 180 degrees
    - -190 degrees = -180 degrees
- Negative angles sent rotate the cobot clockwise.
- Positive angles sent rotate the clock counter-clockwise.
- Positive and negative rotational positions are split down the origin. 
    - From 0 degrees to 179 degrees; then, from -179 degrees back to 0 degrees
- Unfortunately, the cobot is not aware of its current rotational position.
    - _Currently testing this section. - Haley_
    - On Joints 1 and 5, there is a block restricting the servos movement at -3 degrees. Once this block is hit, the joint will stop movement.
    - On Joint 1:
        - Rotational movement is locked to the positive range of rotational movement.
        - When the user attempts to rotate the cobot into a negative rotational position (-90 degrees, for example), the cobot attempts to reach that position by rotating counter-clockwise.
    - Joints 2, 3, and 4 are restricted by other joints. 
        - Joint 2's rotational limits: -140 degrees to 140 degrees
        - Joint 3's rotational limits: -160 degrees to 160 degrees
        - Joint 4's rotational limits: -165 degrees to 150 degrees (weird)
    - Joint 5
        - (testing)
    - There is no block nor are there restrictions on joint 6.

## Coordinate Movements

## Development Languages

### [myBlockly](https://docs.elephantrobotics.com/docs/gitbook-en/5-ProgramingApplication-myblockly-uiflow-mind/5.1-myblockly/)
myBlockly is a "Puzzle programming [drag-and-drop/block-based programming] software based on python enviornments and pymycobot dependent libraries."
* Requires a completely setup Python enviornment
* Also generates Python script based on blockly code

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
    - [Latest Release](https://github.com/elephantrobotics/pymycobot/releases/)

#### Documentation
 * [`pymycobot` library documentation from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/)
 * [Python API for myCobot](https://pypi.org/project/pymycobot/)

Example Library Use in Python:
```python
from pymycobot import MyCobot, Angle, Coord, utils
```

Example Use of Coordinates and Joing Angles: The Cobot Sits and Stands Up Again
```python
from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('COM3', 115200)
mc.power_on()

#For the best results, wait for 5s after opening the serial port.
time.sleep(5)

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

mc.power_off()
```

#### Notes:
- Tested on **pymycobot v2.7.5**
- The Python API is not complete.
- While `mc.power_on()` Servos will lock but be manuverable after every movement command.
    - Servos can be manually unlocked via `mc.release_all_servos()`
    - Servos will move back to its original position in this state
- Servos become fully manuverable again after the `mc.power_off()` is run.

For Best Results:
- Wait 5 seconds for the cobot to connect to the serial port.
- Wait 5 seconds after sending angles and coordinates.

---

### C#

* Recommends using VSCode 2019
* [Source Code](https://github.com/elephantrobotics/Mycobot.csharp)
* [Dynamic Library](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html)


Tested with the Following Environment:
* Visual Studio 2022
* .NET SDK 5.0.409
* .NET SDK 6.0.301
* [Mycobot.csharp v1.2](https://github.com/elephantrobotics/Mycobot.csharp/releases)

#### [Recommended Steps for Set-Up](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html#922-running-in-windows)

1. Setup Your C# Environment
    * Download and install the [.NET core](https://dotnet.microsoft.com/en-us/download) and [.NET framework](https://dotnet.microsoft.com/en-us/download/dotnet-framework) from Microsoft.
        * *Skip this step if you already have C# installed or have installed C# through Unity on your device.*
    * Elephant Robotics also provides these libraries as a part of their [latest release](https://github.com/elephantrobotics/Mycobot.csharp/releases/tag/v1.2). *See the notes below before downloading.*
        * For Windows Users: 
            * Download `net.core.zip` and `net.framework.zip`
        * For Linux Users: 
            * Download `MyCobot.csharp.tar.gz`
2. Download the Source Code from GitHub
    * The source code includes the API for running the cobot (`MyCobot.cs`) and a sample code for first-time use (`Program.cs`).
3. Open the Source Code and Open the Solution on VSCode or Visual Studio. 
4. Change the port number of the cobot in `Program.cs` to match the port number of your cobot.
    * For Windows Users:
        * Use the [Device Manager](https://help.fleetmon.com/en/articles/2010900-how-do-i-get-my-com-port-number-windows) to identify the Cobot's port number. 
    * For Linux Users: 
        * Elephant Robotics expects the cobot's port number to be `/dev/ttyAMA0`.
5. Run the project.

Example Use of Coordinates and Angles:
```C#
using System;
using System.Threading;

namespace Mycobot.csharp
{
    class Test
    {
        static void Main(string[] args)
        {
            MyCobot mc = new MyCobot("COM3");
            //Raspberry Pi robotic arm serial port name: /dev/ttyAMA0
            
            mc.Open();

            //After Windows opens the serial port, you need to wait for 5s.
            //After Windows opens the serial port, the BASIC at the bottom will restart.
            Thread.Sleep(5000);

            int[] coords = new[] {0, 0, 0, 0, 0, 0};
            mc.SendCoords(coords, 80, 1);
            Thread.Sleep(5000);
            var recCoords = mc.GetCoords();
            foreach (var v in recCoords)
            {
                Console.WriteLine(v);
            }


            int[] angles = new[] {0, 0, 0, 0, 0, 0};
            mc.SendAngles(angles, 80);
            var recAngles = mc.GetAngles();
            foreach (var v in recAngles)
            {
               Console.WriteLine(v);
            }

            mc.Close();
        }
    }
}
```

#### Running on a Raspberry Pi

* Follow the steps to setup a C# enviornment above, if you haven't already.
* The main difference in set-up and use is the port number of the cobot. On Raspberry Pi, Elephant Robotics expects the cobot's port number to be:
    * `/dev/ttyAMA0`

#### Working with Unity:
- Player API compatibility level must be changed to either ".NET framework" or ".NET 2.0" to recognize System.IO.Ports. 
    - System.IO.Ports is what Elephant Robotics use to open the serial port
    - https://forum.unity.com/threads/cant-use-system-io-ports.141316/
- Import the `MyCobot.cs` script from the GitHub source code.
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
- The .NET libraries provided with Elephant Robotics' [latest release](https://github.com/elephantrobotics/Mycobot.csharp/releases/tag/v1.2) were oddly unnecessary to run the Cobot on C# alone. More testing is needed to prove this.


---

### [ROS](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/)

* Install Firmware using [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)
* Only need to build a ROS enviornment for the MyCobot 280-M5

[ROS Wiki](http://wiki.ros.org/Documentation)

#### Setting Up ROS and myCobot:
1. Build your ROS Enviornment 
    * [ROS Enviornment Building Instructions by Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.1-ROS1/12.1.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#12122-environment-installation)
        * ROS versions supported:
            - Ubuntu 16.04 / ROS Kinetic
            - Ubuntu 18.04 / ROS Melodic
            - Ubuntu 20.04 / ROS Noetic
    * [Instructions from ROS Wiki](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
2. Install the MoveIt function packages
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.1-ROS1/12.1.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#11-installing-ros)
    * [Install/Build Instructions from ROS](https://moveit.ros.org/install/)
3. Create a ROS workspace
    * [ROS Workspace Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#21-precondition)
4. Download `mycobot_ros`
    * [`mycobot_ros` on GitHub](https://github.com/elephantrobotics/mycobot_ros)

#### 3D Visualization using `rviz`

[Official ROS Documentation on `rviz`](http://wiki.ros.org/rviz)

* Installing `rviz`
    * On ROS:
        * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.1-ROS1/12.1.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/)
        * [GitHub Repository](https://github.com/ros-visualization/rviz)
    * On ROS2:
        * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/)
        * [GitHub Repository](https://github.com/ros2/rviz)

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

### [ROS2]()

* Install Firmware using [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)
* Only need to build a ROS enviornment for the MyCobot 280-M5

[ROS Wiki](http://wiki.ros.org/Documentation)

#### Setting Up ROS and myCobot:
1. Build your ROS Enviornment 
    * [ROS Enviornment Building Instructions by Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.1-ROS2%E7%9A%84%E5%AE%89%E8%A3%85.html)
        * ROS2 Versions Supported: 
            - Ubuntu 20.04 / ROS Foxy
    * [Instructions from ROS Wiki](https://docs.ros.org/en/foxy/index.html)
2. Install the MoveIt function packages
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.6-moveit2%E7%9A%84%E5%AE%89%E8%A3%85.html)
    * [Install/Build Instructions from ROS](https://github.com/ros-planning/moveit2)
3. Create a ROS workspace
    * [Workspace Instructions from Elephant Robotics](https://github.com/elephantrobotics/mycobot_ros2/blob/humble/README.md)
4. Download `mycobot_ros2`
    * [`mycobot_ros2` on GitHub](https://github.com/elephantrobotics/mycobot_ros2)

#### 3D Visualization using `rviz`

[Official ROS Documentation on `rviz`](http://wiki.ros.org/rviz)

* Installing `rviz`
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/)
    * [GitHub Repository](https://github.com/ros2/rviz)
