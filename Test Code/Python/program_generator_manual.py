from pymycobot import MyCobot
import vcupycobot
import time

mc = MyCobot('COM3', 115200)
mc.power_on()
time.sleep(5)
mc.send_angles([0,0,0,0,0,0], 100)
time.sleep(2)

recorded_angles = []
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

        recorded_angles.append(new_angles)
        print("\tAngles", (index + 1), "Recorded -", recorded_angles[index])
        index += 1
    elif user_in == "no" or user_in == "done":
        break
    else:
        print("\tAngles Not Recorded")

mc.power_off()

# Generate new python file to follow the movement of recorded angles
file_name = input("Enter the File Name: ")
file_name = file_name + ".py"
with open(file_name, 'w') as f:
    f.write('''\
from pymycobot import MyCobot
import time
import vcupycobot

mc = MyCobot('COM3', 115200)
mc.power_on()
time.sleep(5)

vcupycobot.move_to_origin(mc, 100)

''')

    for angles in recorded_angles:
        out = f"vcupycobot.move_angles_smoothly(mc, mc.get_angles(), {angles})\n"
        f.write(out)

    f.write("\nmc.power_off()")