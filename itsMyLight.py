
from pymycobot import MyCobot, Angle, Coord
import time
import RPi.GPIO as GPIO

# Servo 1 min and max angles
s1_max_angle = 179 # actual 173.84
s1_min_angle = -179 # actual -171.12
lightIn = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mycobot = MyCobot('/dev/ttyAMA0',1000000)

# Reset
# mycobot.send_angles([0,0,0,0,0,0], 50)

# Testing coordinates

#mycobot.send_coords([100, 140, 100, 0, 0, 0], 70, 0)
# time.sleep(3)
while(1):
    command = ""
    command = input("m or else: ")
    if command == "m":
        # mycobot.release_all_servos()
        mycobot.send_angles([0, 0, 0, 0, 0, 0], 50)
    elif command == "a":
        angles = mycobot.get_angles()
        print(angles)
    elif command == "c":
        coor = mycobot.get_coords()
        print(coor)
    elif command == "s":
        mycobot.send_angles([90, 90, 90, 0, 0, 0], 50)
    elif command == "l":
        while(1):
            print(GPIO.input(lightIn))
            if GPIO.input(lightIn) == 0:
                mycobot.set_color(255, 0, 0)
                mycobot.send_coords([-132.2, -157.8, 23.3, 171.98, -0.05, 153.68], 90, 0)
            else:
                mycobot.set_color(0, 0, 255)
                mycobot.send_angles([0, 0, 0, 0, 0, 0], 50)
    else:
        mycobot.send_coords([-132.2, -157.8, 23.3, 171.98, -0.05, 153.68], 80, 0)




#testing servo 1 angles
'''
print("\nServo 1: -60")
mycobot.send_angles([-60,0,0,0,0,0], 50)
time.sleep(3)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\nServo 1: -120")
mycobot.send_angles([-120,0,0,0,0,0], 50)
time.sleep(3)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\nServo 1: min angle")
mycobot.send_angles([s1_min_angle,0,0,0,0,0], 20)
time.sleep(5)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\ndefault position")
mycobot.send_angles([0,0,0,0,0,0], 50)
time.sleep(5)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\nServo 1: 60")
mycobot.send_angles([60,0,0,0,0,0], 50)
time.sleep(3)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\nServo 1: 120")
mycobot.send_angles([120,0,0,0,0,0], 50)
time.sleep(3)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)

print("\nServo 1: max angle")
mycobot.send_angles([s1_max_angle,0,0,0,0,0], 50)
time.sleep(3)
angles = mycobot.get_angles()
print(angles)
coords = mycobot.get_coords()
print(coords)
'''
