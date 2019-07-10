from os import system, name
from time import sleep

def clear():
    # Clears the console of all text.
    if name == "nt": # If the OS is Windows, executes this
        _ = system("cls")
    else: # If OSX or Unix-based/Unix-like systems, executes this
        _ = system("clear")