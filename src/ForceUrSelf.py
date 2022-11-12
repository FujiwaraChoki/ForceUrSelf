import requests
import os
import methods
import argparse
from platform import platform
from termcolor import colored

__author__ = "Sami Hindi"
__version__ = "1.0.0"

# Set OS Variable to user operating system
OS = "windows" if "windows" in platform().lower() else "linux"

# Set the username of the currently logged in user
USER = os.getlogin()

def main(args: argparse.Namespace) -> None:
    '''
    Tool: ForceUrSelf
    Author: Sami Hindi
    Usage:
    Bruteforce & Account cracking
    License: GNU General Public Licesne V3.0
    OS: Windows & Linux
    '''
    
    
    
if __name__ == '__main__':
    # Print logo
    methods.print_logo()
    
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='ForceUrSelf - Bruteforce & Account cracking')
    
    # Get mode from arguments
    parser.add_argument('-m', '--mode', help='Mode to run ForceUrSelf in', required=True)
    
    # Take required username argument
    parser.add_argument('-u', '--username', type=str,
                        help='Username to bruteforce')
    
    parser.add_argument('-pl', '--password-list', type=str,
                        help='Passwordlist to use for provided username')
    
    # Add proxy argument
    parser.add_argument('-p', '--proxy', type=str,
                        help='Proxy to use for requests')
    
    # Add verbosity argument
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Use verbose mode')
    
    # Parse the arguments
    args = parser.parse_args()
    parsed_args = methods.parse_args(args)
    
    # Handle arguments in main function
    main(parsed_args)