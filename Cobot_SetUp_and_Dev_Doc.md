# Setup and Development Documentation for myCobot 280 M5

[ER myCobot 280 M5](https://www.elephantrobotics.com/en/mycobot-en/)

## About

"myCobot is the world's smallest and lightest six-axis collaborative robot, jointly produced by [Elephant Robotics](https://www.elephantrobotics.com/en/our-company/) and [M5STACK](https://m5stack.com/about-us). It is more than a productivity tool full of imaginations, can carry on the secondary development according to the demands of users to achieve personalized customization."
* The robot itself was built using modular components from M5Stack and other providers:
    * [LCD (BASIC)](https://shop.m5stack.com/collections/m5-controllers/products/esp32-basic-core-iot-development-kit-v2-6)
        * [M5Go Core User Manual](https://flow.m5stack.com/download/M5GO_User_Manual_en.pdf)
            * Wireless and RF Integrated Circuit Chip: [ESP32-DOWDQ6-V3](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
    * [LCD (ATOM)](https://shop.m5stack.com/products/atom-matrix-esp32-development-kit?_pos=25&_sid=b13b754ab&_ss=r)
    * [Joint 5 Servo](https://www.aliexpress.com/item/3256801491791245.html?gatewayAdapt=4itemAdapt) 
* The robot was assembled by Elephant Robotics.
* Target Audience: Schools and Classrooms

## Official Documentation
- [Documentation](https://docs.elephantrobotics.com/docs/gitbook-en/)
    - [Cobot Hardware Setup for First Time Use](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.3-quick_start.html)
- [Video Tutorials](https://www.elephantrobotics.com/en/support-280-m5-en/)
- [User Manual](https://www.elephantrobotics.com/wp-content/uploads/2021/03/myCobot-User-Mannul-EN-V20210318.pdf)

## Table of Contents
1. [myCobot Drivers](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#basic-drivers)
2. [myStudio and How to Download It](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#mystudio)
3. [Steps to Run a Program](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#steps-to-run-a-program)
4. [Details on Rotational Movement](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#rotational-movement)
5. [Details on Coordinate-Based Movement](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#coordinate-movements)
6. [Software Development Tools](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#development-tools)
   1. [myBlockly](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#myblockly)
   2. [UIFlow](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#uiflow)
   3. [RoboFlow](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#roboflow-operating-system)
   4. [Python](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#python)
   5. [C#](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#c)
   6. [ROS](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#ros)
   7. [ROS2](https://github.com/vcuse/elefante/blob/main/Cobot_SetUp_and_Dev_Doc.md#ros2)

---
---

## Basic Drivers

![Driver Diagram](https://docs.elephantrobotics.com/docs/gitbook-en/resourse/4-BasicApplication/4.1/4.1-mystudio1.jpg)

[How to Confirm Which Basic Chip is in the Robot](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip)[^1]

Basic Driver for myCobot 280 M5: CP210x **(Recommended on Linux)**
- [Windows 10](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_Windows.zip)
- [Linux](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_Linux.zip)
- [MacOS](https://www.elephantrobotics.com/software/drivers/CP210x_VCP_MacOS.zip)

New Basic Driver for myCobot 280 M5: CH9102
- [Windows 10](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_CDC_Windows.exe)
- [Windows Server](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_SER_Windows.exe)
- [MaxOS](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_MacOS.dmg)

Atom Serial Port Driver:
- [Windows 10](https://download.elephantrobotics.com/software/drivers/CDM21228_Setup.zips)

[^1]: Windows may automatically install the best driver for you. On Linux, it is recommended to use the CP210x driver.

## [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)

myStudio is a "one-stop application platform for myRobot/myCobot and other robots."
* Handles firmware installations and updates
* Contains robot tutorials on use, maintenance, and repair

#### Downloads:
- [Download from GitHub](https://github.com/elephantrobotics/myStudio)
    - [Latest Release](https://github.com/elephantrobotics/myStudio/releases/)


## Steps to Run a Program:
1. Download and install myStudio onto your computer.
2. Make sure you have all drivers installed onto your computer.
3. Make sure the miniRobot firmware running on Basic (the base of the cobot) is up-to-date
    * Flash the newest release via myStudio
    * Newest release: **miniRobot v2.0**
4. Make sure the firmware for ATOM (the top of the cobot) is up-to-date
    * Flash the newest release via myStudio
    * Newest release: **ATOM v5.1**
5. On the Basic (the computer at the base of the cobot), navigate to the "Transponder" screen. 

### Connecting to the Cobot via Serial Port

1. Connect the cobot to your computer using the USB-C on the left-side of the cobot's LCD.
2. On the "Transponder" screen, select "USB UART". 
3. Check the status of ATOM.
    * If the BASIC can successfully connect to ATOM, the "USB UART" page will say "Atom : ok".
    * If the BASIC cannot successfully connect to ATOM, the "USB UART" page will say "Atom : no".
4. The cobot is now ready to accept instructions.

### Controlling the Cobot Arm via TCP/IP

The myCobot 280 M5 attempts to connect to the following network, by default:
* SSID: MyCobotWiFi2.4G
* Password: mycobot123

**Caution: The cobot cannot connect to any WiFi that has an SSID that contains a space.**

#### Connecting to WiFi Using Arduino ESP32

This method uses the Arduino IDE with the built-in [Wifi library](https://www.arduino.cc/reference/en/libraries/wifi/). 

_If anything, this method proves that the ESP32 IC chip is working correctly. - Haley_

Steps:
1. Install the Arduino IDE.
2. Install the M5Core board library.
3. Use the `connect_and_send_packets` script to connect to WiFi and start sending TCP packets.
4. Burn the sketch to the cobot's Basic.
    * The cobot connects to WiFi as "esp32-67D174"
    * _I had to use the "Wireless Network Watcher" to determine the IP address of the cobot. The cobot did not appear through any command line commands. - Haley_
5. Use the `tcp_server.py` script to recieve the packets.

`connect_and_send_packets` Arduino Sketch
`tcp_server.py` - Recieves TCP packets

[This example](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/wifi.html#wi-fi-sta-example) shows how this library may be used to set up a TCP connection.

#### Connecting to WiFi using Elephant Robotic's APIs

##### Setting Up WiFi Network Connection Using Python3:
1. Connect to the cobot via Serial Port. (See instructions above.)
2. Create a new Python script and use the code below. Substitute the port ID with that of your cobot and the SSID and password with that of your desired network.
3. Run the script below, or the `connect_to_wifi()` or `connect_to_vcuse()` functions in `vcupycobot`. 

To Setup the Network:
```python
from pymycobot.mycobot import MyCobot
import time

# powers on the cobot
mc = MyCobot('cobot_port_id', 115200)
mc.power_on()
time.sleep(5)

# attempts to setup the network credentials
mc.set_ssid_pwd("wifi_ssid", "wifi_password")

# powers off the cobot
mc.power_off()
```

* To check if the network is set up properly, replace the function call `mc.set_ssid_pwd()` with `mc.get_ssid_pwd()`.

##### Connecting to WiFI:
1. On the "Transponder" screen, select "WLAN Server".
2. The cobot should now attempt to connect to your choosen WiFi.
    * If you have successfully setup the cobot's network connection, you should see your wifi's SSID at the top of the screen.
    * If unsuccessful, the top of the screen will read "MyCobotWiFi2.4G".
3. If the cobot is unable to connect to WiFi, for any reason, you should see the following message:
    * "WIFI Connect Failed      ssid or password error"
4. 

_Note: The instructions below only describe how to connect to WiFi using Python3 and a myCobot Pi. M5 instructions are minimal._

[Instructions on how to connect to the cobot wirelessly via TCP/IP](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.6_TCPIP.html)

_ There are functions built into `pymycobot` (the Python module) to set up the cobot's wifi connect; however, there is no documentation on them. When testing, it is inconclusive whether the functions are actually configuring the network connection for continuous use. I have reached out to support to ask about this. Wish me luck! - Haley _

### Running on Bluetooth:

There are two methods to connect to the cobot using Bluetooth:

Using the `myCobot BLE` server:
1. Flash the myCobot bluetooth server, `myCobot BLE`, to your cobot's BASIC using myStudio.
2. On your bluetooth-enabled controller (your computer, mobile device, etc.), activate bluetooth and pair the device to the cobot. 
    * Your cobot will broadcast itself as `MyCobot`.

Using `miniRobot v2.0`:
1. On the "Transponder" screen, select "Bluetooth". 
2. The cobot is now broadcasting itself on Bluetooth. 
    * The cobot will broadcast itself as `mycobot280-m5`.
3. On your controller device, activate bluetooth and request to pair with the cobot. 
4. Verify that the bluetooth code displayed on your controller device is the same as the one displayed on the cobot's LCD.
    * Once you have confirmed that they are the same, select the `pair` or `confirm` option on both devices.

#### [myCobot Phone Controller App](https://github.com/elephantrobotics/myCobot/tree/main/Software/phone%20controller)
* Unfortunately, this controller is only a preview. All assets on the app work; however, the app itself is unable to connect to the cobot via Bluetooth - including when the phone itself is successfully connected to the cobot.
* Excellent app design. If we could get this working, that'd be neat.

_No more information was available on how to send instructions via Bluetooth. - Haley_

## Rotational Movement

The myCobot 280 M5 has 6 joints, labeled 1 through 6, that control the robots movement via the use of 360 degree servos.

According to Elephant Robotics Documentation, each joint's range of rotational degrees of movement is as follows: -160 deg. to 160 deg. or -165 deg to 165 deg; however, see the findings below for the true limits and rotational descriptions for each joint.

### Rotational Limits:
- Rotational Limit on Angles: 190 deg or -190 deg
    - 190 degrees = 180 degrees
    - -190 degrees = -180 degrees
- Positive and negative rotational positions are split down the origin. 
    - From 0 degrees to 179 degrees; then, from -179 degrees back to 0 degrees
    - The notch in the joint lines up when the joint in at the origin (0 degrees).
- Rotational Limits per joint:
    - On Joints 1 and 5, there is a block restricting the servos movement at 180 degrees/-180 degrees. Once this block is hit, the joint will stop movement.
    - Joints 2, 3, and 4 are restricted by other joints. 
        - Joint 2's rotational limits: -140 degrees to 140 degrees
            - Exact Limits: -133 degrees to 145 degrees
        - Joint 3's rotational limits: -160 degrees to 160 degrees
            - Exact Limits: -175 degrees to 133 degrees
        - Joint 4's rotational limits: -165 degrees to 150 degrees
            - Exact Limits: 73 degrees to 24 degrees (?)
    - There is no block nor are there restrictions on Joint 6.

#### Diagram of Joint 1
![Joint 1 Diagram](https://github.com/vcuse/elefante/blob/main/Images/Joint%201.jpg)

#### Diagram of Joint 2
![Joint 2 Diagram](https://github.com/vcuse/elefante/blob/main/Images/Joint%202.png)

#### Diagram of Joints 3 and 4
![Joint 3/4 Diagram](https://github.com/vcuse/elefante/blob/main/Images/Joint%203_4.png)

#### Diagram of Joint 5
![Joint 5 Diagram](https://github.com/vcuse/elefante/blob/main/Images/Joint%205.png)

#### Diagram of Joint 6
![Joint 6 Diagram](https://github.com/vcuse/elefante/blob/main/Images/Joint%206.png)

### Min and Max Angles According to the Python API:
* Joint 1
    * Min: -1550 degrees 
    * Max: 1550 degrees 
* Joint 2
    * Min: -1650 degrees
    * Max: 1650 degrees
* Joint 3
    * Min: -1650 degrees
    * Max: 1650 degrees
* Joint 4
    * Min: -1650 degrees
    * Max: 1650 degrees
* Joint 5
    * Min: -1750 degrees
    * Max: 1750 degrees
* Joint 6
    * Min: -17500 degrees
    * Max: 21608 degrees

### Notes:
* Despite all movement commands operating in degrees between -180, 0, and 180 *or less*, the functions that return the minimum and maximum angles possible return coterminal angle values (?).
    * Adding onto this, some joints cannot move a complete 360 degrees.

## Coordinate Movements

(TBA)

--- 
---

# Development Tools

## [myBlockly](https://docs.elephantrobotics.com/docs/gitbook-en/5-ProgramingApplication-myblockly-uiflow-mind/5.1-myblockly/)
myBlockly is a "Puzzle programming [drag-and-drop/block-based programming] software based on python enviornments and pymycobot dependent libraries."
* Requires a completely setup Python enviornment
* Also generates Python script based on blockly code

#### Downloads 
- [Official Download from Elephant Robotics](https://www.elephantrobotics.com/en/downloads/)
- [From GitHub](https://github.com/elephantrobotics/myblockly-package/releases/tag/v0.0.6)

#### Notes
_Blockly code isn't running on the cobot despite the Python code running just fine. Weird. - Haley_

---

## [UIFlow](https://docs.elephantrobotics.com/docs/gitbook-en/5-ProgramingApplication-myblockly-uiflow-mind/5.2-UIFlow/)
UIFlow is a "programming tool specifically designed for the M5 hardware system using [Blockly](https://developers.google.com/blockly) and Python code".
- Typically used for primary/secondary schools to be able to develop apps for the M5Core

[Web-Based IDE](https://flow.m5stack.com/)

### Downloads 
- [Official Windows 64-bit Desktop Application Download from Elephant Robotics](https://static-cdn.m5stack.com/resource/software/UIFlow-Desktop-IDE.zip)

### Documentation
- Official Documentation is in Chinese, but has some starter videos on the [Web IDE](https://flow.m5stack.com/).
    - [For the M5StickC](https://shop.m5stack.com/products/stick-c?variant=17203451265114)
        - [Documentation (Chinese)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/M5StickC_Guide.pdf)
    - [For the M5GO IoT Device](https://shop.m5stack.com/products/m5go-iot-starter-kit-stem-education?variant=16804754260058)
        - [Documentation (Chinese)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/UIFlow-Book-zh_cn.pdf)

---

## [RoboFlow Operating System](https://docs.elephantrobotics.com/docs/gitbook-en/6-ApplicationBaseRoboFlow/)

- Built to be run on teaching pendants for Elephant Robotics cobots.

### Downloads:
- [Official Download from Elephant Robotics](https://www.elephantrobotics.com/en/downloads/)

### Documentation
- [Operation and Programming Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/Operation-and-Programming-Manual-EN.pdf)
- RoboFlowScript: C-based programming language to "control the robot" (not completely described)
    - [RoboFlowScript Programming Language Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/1-RoboFlowScript_Manual.pdf)
- Python API for Remote Robot Control
    - [RoboFlow Python API](https://static.elephantrobotics.com/wp-content/uploads/2019/06/2-RoboFlow-API-python.pdf)
    - [RoboFlow Socket Communication Manual](https://static.elephantrobotics.com/wp-content/uploads/2019/06/3-RoboFlow-CommunicationSocket.pdf): Documentation for the Python socket commands

---

## Python

* [Installing the `pymycobot` library](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.1_download.html#714-preparations)

### Downloads:
- [`pymycobot` Github](https://github.com/elephantrobotics/pymycobot)
    - [Latest Release](https://github.com/elephantrobotics/pymycobot/releases/)
    - Use `pip` or `pip3` to install `pymycobot` to your enviornment.

### Documentation
 * [`pymycobot` library documentation from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/)
 * [Python API for myCobot](https://pypi.org/project/pymycobot/)
 * [`pymycobot` GitHub ReadMe](https://github.com/elephantrobotics/pymycobot/blob/main/README.md)

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

Example use of rotating the joint incrementally:
```python
from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('COM3', 115200)
mc.power_on()
time.sleep(5)

for x in range(0, 90):
    mc.send_angle(Angle.J1.value, x, 80)

mc.power_off()
```


#### Notes:
- Tested on **pymycobot v2.7.5**
- The Python API does not completely include or describe all the available functions in the API.
- While `mc.power_on()` Servos will lock but be manuverable after every movement command.
    - Servos can be manually unlocked via `mc.release_all_servos()`
    - Servos will move back to its original position in this state
- Servos become fully manuverable again after the `mc.power_off()` is run.

For Best Results:
- Wait at least 5 seconds for the cobot to connect to the serial port.
- To move from one angle to another, we recommend instead moving in one-angle increments to the next angle until the cobot reaches its destimation.
    - If you wish to not use this appraoch, wait 5 seconds after sending angles and coordinates across a difference of movement. 

---

## C#

* Recommends using VSCode 2019
* [Source Code](https://github.com/elephantrobotics/Mycobot.csharp)
* [Dynamic Library](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html)


Tested with the Following Environment:
* Visual Studio 2022
* .NET SDK 5.0.409
* .NET SDK 6.0.301
* [Mycobot.csharp v1.2](https://github.com/elephantrobotics/Mycobot.csharp/releases)

### [Recommended Steps for Set-Up](https://docs.elephantrobotics.com/docs/gitbook-en/9-ApplicationBaseCSharp/9.2-build.html#922-running-in-windows)

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
- Must still navigate to the "Transponder" page to properly send angles/coord. to the cobot; however, it automatically reboots the computer (Basic) after each use. 
    - This doesnt happen in Python.
    - Is there a way to turn this off?
    - Looked in the [Microsoft Doc](https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-6.0) and the reboot signal doesnt seem to be coming from here
- The .NET libraries provided with Elephant Robotics' [latest release](https://github.com/elephantrobotics/Mycobot.csharp/releases/tag/v1.2) were oddly unnecessary to run the Cobot on C# alone.

---

## [ROS](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/)

* Install Firmware using [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)
* Only need to build a ROS enviornment for the MyCobot 280-M5

[ROS Wiki](http://wiki.ros.org/Documentation)

### Setting Up ROS and myCobot:
1. Build your ROS Enviornment 
    * [ROS Enviornment Building Instructions by Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.1-ROS1/12.1.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#12122-environment-installation)
        * ROS versions supported:
            - Ubuntu 16.04 / [ROS Kinetic](http://wiki.ros.org/kinetic)
            - Ubuntu 18.04 / [ROS Melodic](http://wiki.ros.org/melodic)
            - Ubuntu 20.04 / [ROS Noetic](http://wiki.ros.org/noetic)
    * [Instructions from ROS Wiki](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
2. Install the MoveIt function packages
    * [Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.1-ROS1/12.1.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#11-installing-ros)
    * [Install/Build Instructions from ROS](https://moveit.ros.org/install/)
3. Create a ROS workspace
    * [ROS Workspace Instructions from Elephant Robotics](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html#21-precondition)
4. Download `mycobot_ros`
    * [`mycobot_ros` on GitHub](https://github.com/elephantrobotics/mycobot_ros)

### 3D Visualization using `rviz`

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

### Using `mycobot_ros`
* [Arm Control and Following](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1242-control-and-following-of-the-robot-arm)
* [Simple GUI Control Interface](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1244-gui-control)
    * [Keyboard Control](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#12441-keyboard-control)
* [Camera Control](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.4-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#1245-vision)

### Using `mycobot_ros` and `MoveIt`
* [Documentation on integrated MoveIt Functions](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.5-Moveit/)

---

## ROS2

* Install Firmware using [myStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/)
* Only need to build a ROS enviornment for the MyCobot 280-M5
* Tested on ROS Foxy for Ubuntu LTS 20.04

ROS2 Versions Supported:
* Ubuntu 20.04 / [ROS Foxy](https://docs.ros.org/en/foxy/index.html)
* Ubuntu 20.04 / [ROS Galactic](https://docs.ros.org/en/galactic/index.html)
* Ubuntu 22.04 / [ROS Humble](https://docs.ros.org/en/humble/index.html)

[ROS Wiki](http://wiki.ros.org/Documentation)

### Setting Up ROS and myCobot:

1. Build your ROS Enviornment
    * Follow the installation instructions for your choosen ROS distribution.
    * This can be done from source or using the binaries.
2. Install the MoveIt function packages
    * [Install & Build Instructions](https://github.com/ros-planning/moveit2) 
3. Download and build your myCobot ROS2 workspace
    * [Workspace Instructions from Elephant Robotics](https://github.com/elephantrobotics/mycobot_ros2/blob/humble/README.md)

### 3D Visualization and Cobot Control using `rviz`

https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/ 

### Steps for Use:
1. Navigate to your myCobot ROS workspace.
2. Adjust the original Python scripts to reference your cobot's serial port.
    1. The original Python scripts reference the `/dev/ttyUSB0` serial port; however, your cobot may be different.
    2. Navigate to the `dev` directory on your system to check which port your cobot is calling itself.
        * Previous Ports: `/dev/ttyUSB0`, `/dev/ttyAMC0`
    3. The original Python scripts are located in your workspace under `install/mycobot_280/lib/python3.8/site-packages/mycobot_280/`.
3. Remember to source both your ROS distrobution and your workspace.
    * From the root of your myCobot workspace:
    ```
        source /opt/ros/{distribution_name}/setup.bash
        source ./install/setup.bash
    ```

### Test Script

The following command will open `rviz` and display a model of the cobot. 
```
    ros2 launch mycobot_280 test.launch.py
```

### Elephant Robotics User Interfaces

#### [Slider Control](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#122721-slider-control)
* Control the cobot through the use of the slider component.
* You should see the cobot mirror the model's movement in `rviz`.

#### [Model Following](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#122722-model-follow)
* The cobot model in `rviz` will follow the movement of your cobot in real-time. 
* Requires a separate script to move the cobot.

#### [GUI for Rotational and Coordinate-Based Movement](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#12274-gui-control)
* "A simple GUI control interface" that supports movement by angular and coordinate-based movement. 
* The interface is in Chinese.
    * (Put translated interface here.)

Notes: 
* Currently not working as intended. 
    * The `rviz` model is not building properly.
    * Movement signals are not being sent to the cobot. 
* More testing/debugging needed.

#### [Keyboard Controller for Coordinate-Based Movement](https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.7-rivz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/#122741-keyboard-control)
* 

Notes: 
* Currently not working as intended. 
    * The `rviz` model is not building properly.
    * Movement signals are not being sent to the cobot OR its not taking input properly.
* More testing/debugging needed.

--- 

# Frequently Encountered Issues

Below is a list of freqently encounters problems when working with the myCobot 280 M5. If a solution has been found, it is logged here with the issue.

## Hardware Issues

### ATOM Issues

#### Issue 1:
While connected via serial port (USB), the ATOM LED lights do not respond to Python commands to change color.

**Solutions**:
- _Currently looking for solutions._

### Connection Issues

#### Issue 1: 
While connected via serial port (USB), the cobot is able to recieve angles sent via code; but, the cobot does not report its own angles (i.e.: its current position).

**Solutions**:
- Reset the BASIC by pressing the red button on the left side of the BASIC (right above the USB-C port).
- Hard reset the cobot by unplugging the USB connection and power adapter from the cobot. Wait 7 seconds, then plug back in the power adapter and USB connection.

## Software Issues