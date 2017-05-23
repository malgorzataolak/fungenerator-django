import sys

#import RPi.GPIO as GPIO

import time


rotation_speed = 0.5

def sing():
	print("spinning")

def spin():
        print("starting to spin")

        GPIO.setmode(GPIO.BOARD)

        pin_number = 11
        GPIO.setup(pin_number, GPIO.OUT)  
        frequency_hertz = 50
        pwm = GPIO.PWM(pin_number, frequency_hertz)
        left_position = 0.40
        right_position = 2.5
        middle_position = (right_position - left_position) / 2 + left_position
        positionList = [left_position, middle_position, right_position, middle_position]
        ms_per_cycle = 1000 / frequency_hertz

        for i in range(4):
                # This sequence contains positions from left to right
                # and then back again.  Move the motor to each position in order.
                for position in positionList:
                        duty_cycle_percentage = position * 100 / ms_per_cycle
                        print("Position: " + str(position))
                        print("Duty Cycle: " + str(duty_cycle_percentage))
                        print("")
                        pwm.start(duty_cycle_percentage)
                        time.sleep(rotation_speed)
                
        pwm.stop()

        GPIO.cleanup()

def quick_rotation():
        global rotation_speed
        rotation_speed = 0.2
        print("quick rotation set")

def normal_rotation():
        global rotation_speed
        rotation_speed = 0.5
        print("normal rotation set")

def slow_rotation():
        global rotation_speed
        rotation_speed = 0.8
        print("slow rotation set")
