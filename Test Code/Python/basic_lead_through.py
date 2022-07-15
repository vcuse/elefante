from pymycobot import MyCobot
import vcupycobot
import time

mc = MyCobot('COM3', 115200)
mc.power_on()
time.sleep(5)
mc.send_angles([0, 0, 0, 0, 0, 0], 100)
time.sleep(2)

angles = []
user_in = ""
index = 0

# Reads and stores the position of the cobot after user manipulation.
while user_in != "done" or user_in != "no":
    mc.release_all_servos()

    user_in = input("Record Angles? (Press Enter) ")
    if user_in == "":
        curr_angles = mc.get_angles()
        new_angles = []

        for angle in curr_angles:
            new_angles.append(int(angle))

        angles.append(new_angles)
        print("\tAngles", (index + 1), "Recorded -", angles[index])
        index += 1
    elif user_in == "no" or user_in == "done":
        break
    else:
        print("\tAngles Not Recorded")

# Commands the Cobot to follow the movement of the recorded angles
mc.send_angles([0, 0, 0, 0, 0, 0], 100)
time.sleep(5)

for angle in angles:

    if len(angle) == 0:
        continue

    while not vcupycobot.angles_in_position(angle, mc):
        mc.send_angles(angle, 100)
        time.sleep(2)

mc.power_off()