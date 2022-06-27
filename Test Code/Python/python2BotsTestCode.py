from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord, Angle
import serial
import time

#port = serial.Serial(port='COM3', baudrate=115200)
#print(port.isOpen())

print("   Activating Cobot...")
mc = MyCobot('COM3', 115200)
mc2 = MyCobot('COM5', 115200)
mc.power_on()
mc2.power_on()
time.sleep(5)
print("   Cobot is now active.")

#print("releasing servos")
#mc.release_all_servos()

print("changing color to red")
mc.set_color(255, 0, 0)
mc2.set_color(255, 0, 0)

"""
time.sleep(3)
print("changing color to green")
mc.set_color(0, 255, 0)
time.sleep(3)
print("changing color to blue")
mc.set_color(0, 0, 255)
time.sleep(3)
"""

currAngles = mc.get_angles()
print("Gertrude's Initial Position:", currAngles)
currAngles = mc2.get_angles()
print("Sir's Initial Position:", currAngles)
time.sleep(2)
print("\n   Moving Bot")

"""
if len(currAngles) > 0:
    currAngle = currAngles[4]
    for x in range(0, 90):
        mc.send_angle(Angle.J5.value, currAngle + x, 80)
else:
    mc.send_angle(Angle.J5.value, 180, 80)
    time.sleep(5)
    mc.send_angle(Angle.J5.value, -90, 80)
    time.sleep(5)
    mc.send_angle(Angle.J5.value, 90, 80)
    time.sleep(5)
"""

mc.send_angles([0, 0, 0, 0, 0, 0], 100)
mc2.send_angles([0, 0, 0, 0, 0, 0], 100)
time.sleep(3)
"""
mc.send_angle(Angle.J1.value, -140, 80)
mc2.send_angle(Angle.J1.value, -140, 80)
time.sleep(5)
print("Gertrude Reset Position:", mc.get_angles())
print("Sir Reset Position:", mc2.get_angles())
mc.send_angle(Angle.J1.value, 140, 80)
mc2.send_angle(Angle.J1.value, 140, 80)
time.sleep(5)

"""
print("Gertrude - After sending deg:", mc.get_angles())
print("Sir - After sending deg:", mc2.get_angles())

"""
mc.send_angle(Angle.J1.value, 0, 80)
time.sleep(5)
print("After sending 0 deg:", mc.get_angles())
mc.send_angle(Angle.J1.value, 190, 80)
time.sleep(5)
print("After sending 190 deg:", mc.get_angles())
"""
time.sleep(3)
print("changing color to green")
mc.set_color(0, 255, 0)
mc2.set_color(0, 255, 0)

mc.power_off()
mc2.power_off()