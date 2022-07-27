from pymycobot import MyCobot
import vcupycobot
import keyboard
import time
import sys

def record_angles(cobot : MyCobot):
    cobot.release_all_servos()

    curr_angles = cobot.get_angles()
    new_angles = []

    for angle in curr_angles:
        new_angles.append(int(angle))

    print("\tAngle Recorded -", new_angles)
    return new_angles

def main(port_id : str):
    mc = MyCobot('COM3', 115200)
    vcupycobot.check_cobot_connection(mc)
    vcupycobot.move_to_origin()

    recorded_angles = []

    # Continuously reads and stores the position of the cobot after user manipulation.
    print("\tRecording Angles Now. (Press \"Enter\" to stop.)")
    while True:
        recorded_joints = record_angles(mc)

        if len(recorded_angles) == 6:
            print("\tAngles Recorded -", recorded_angles)
            recorded_angles.append(recorded_joints)

        time.sleep(0.1)

        if keyboard.is_pressed('enter'):
            break

    mc.power_off()

    if len(recorded_angles) == 0:
        raise Exception("\nNo Angles Were Recorded. (Check your connection to the cobot.)")

    # Cleans up duplicate angles in the list
    curr_list = recorded_angles[0]
    for angle_list in recorded_angles[1:]:
        if vcupycobot.compare_angle_lists(curr_list, angle_list):
            recorded_angles.remove(curr_list)
        else:
            curr_list = angle_list


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

        for angle in recorded_angles:
            out = f"vcupycobot.send_angles_smoothly(mc, mc.get_angles(), {angle})\n"
            f.write(out)

        f.write("\nmc.power_off()")

if __name__ == "__main__":
    main(sys.argv[1])