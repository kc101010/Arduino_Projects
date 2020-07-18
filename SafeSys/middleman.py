# SAFESYS 0 - Serial Management Module
# Program used to read serial data and run camera program 
# Written by Kyle Christie xx/7/2020

# Library Calls
import serial   # serial used to read from arduino board
import os       # os used to manage camera
import time     # time used for time.sleep

#Set serial port to read from Arduino Board
a_board = serial.Serial('COM5', baudrate = 9600, timeout=1)


#Perform constantly - read the serial data and perform actions where necessary
while(True):
    #reset all data to prevent false alarms
    a_board.flushInput()
    a_board.flushOutput()
    board_data = "" 
    
    #sleep for 2 seconds to ensure data is accurate
    time.sleep(2)
    
    #take serial data from arduino and print it to terminal 
    print("Scanning... ")
    board_data = a_board.readline()
    time.sleep(2)
    print(board_data)
    
    #assign the bare serial data to a new variable and decode it to produce a string, print this to terminal
    board_cmp = board_data.decode('utf-8')
    print(board_cmp)
  
    #look for the below message in the serial data, if its found then run the camera module
    #not sure why this section has to be inverted but it works :)
    if not board_cmp.find("INTRUDER")  :
        os.system("camera.py")
        
        
        
        
    