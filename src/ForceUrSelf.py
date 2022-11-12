import requests
import os
import methods
from platform import platform
from termcolor import colored

__author__ = "Sami Hindi"
__version__ = "1.0.0"

# Set OS Variable to user operating system
OS = "windows" if "windows" in platform().lower() else "linux"

# Set the username of the currently logged in user
USER = os.getlogin()

def main():
    '''
    Tool: ForceUrSelf
    Author: Sami Hindi
    Usage:
    Bruteforce & Account cracking
    License: GNU General Public Licesne V3.0
    OS: Windows & Linux
    '''
    methods.print_logo()
    
if __name__ == '__main__':
    main()