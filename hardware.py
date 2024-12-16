# -*- coding: utf-8 -*-
"""
1P13 Design Studio
Dr. Cam Churchill
Created on Mon Dec  2 13:34:41 2024
@authors: Vedant, Liam, Majuraa, Hanna
"""

def rotary():
    bot.activate_stepper_motor() 
    time.sleep(1)
    bot.rotate_stepper_ccw(7) 
    time.sleep(1) 
    
def platform(): 
    arm.rotate_base(-90) 
    time.sleep(1) 
    arm.rotate_elbow(15) 
    time.sleep(1) 
    arm.rotate_shoulder(20) 
    time.sleep(1) 
    arm.rotate_shoulder(20) 
    time.sleep(1) 
    arm.control_gripper(45) 
    time.sleep(1) 
    arm.rotate_elbow(-43) 
    time.sleep(1) 
    arm.rotate_base(75) 
    time.sleep(1) 
    arm.rotate_shoulder(8) 
    time.sleep(1) 
    arm.rotate_elbow(-5) 
    time.sleep(1) 
    
    arm.rotate_elbow(10) 
    time.sleep(1)
    arm.control_gripper(-45)
    time.sleep(1) 
    return arm.effector_position() 

def reject(): 
    arm.rotate_base(-90) 
    time.sleep(1) 
    arm.rotate_elbow(15) 
    time.sleep(1) 
    arm.rotate_shoulder(20) 
    time.sleep(1) 
    arm.control_gripper(45) 
    time.sleep(1) 
    arm.rotate_elbow(-43) 
    time.sleep(1) 
    arm.rotate_base(75)
    time.sleep(1) 
    arm.rotate_base(100)
    time.sleep(1)
    
    arm.rotate_shoulder(-10) 
    time.sleep(1) 
    arm.rotate_elbow(50) 
    time.sleep(1) 
    
    arm.rotate_elbow(10) 
    time.sleep(1) 
    arm.control_gripper(-45)
    time.sleep(1) 
    return arm.effector_position()

rotary() 

for _ in range(4): 
    status = scanner.barcode_check() 
    if status == "Platform": 
        platform() 
    elif status == "Rejection Bin": 
        reject() 
        
    table.rotate_table_angle(45) 
    time.sleep(1) 
    table.rotate_table_angle(45) 
    time.sleep(1)
    
    arm.home() 