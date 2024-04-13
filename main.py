import datetime
import time

print( "_" * 59)
print("I_" * 10, "ServerHelper V1.1", "_I" * 10)
print( "_" * 59)
print("*" * 10, "for a list of commands enter - Help", "*" * 10)
while True:
    s = input ("User: ")



    if s == 'Help': print("_"  * 17)
    if s == 'Help': print("|Help Menu V1.0|")
    if s == 'Help': print("_"  * 17)
    if s == 'Help': print("|Command: Exit - exiting the program|")
    if s == 'Help': print("|Command: Time - Shows time|")
    if s == 'Help': print("|Command: Gude - The guides themselves|")



    if s == 'Time': print("Time: ", datetime.datetime.now())
    if s == 'Exit': break
    if s == 'Gude': print("." * 10, "Gude", "." * 10)