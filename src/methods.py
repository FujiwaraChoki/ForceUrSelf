'''
Methods file for ForceUrSelf
'''
import random
import requests
from termcolor import colored

OUT_FILE: str = '../output.txt'

def print_logo() -> None:
    # Method to print the logo
    with open('../assets/logo.txt', 'r') as logo:
        print(colored(logo.read(), 'blue'))

def parse_args(args) -> list[str]:
    # Method to parse arguments
    RETURN_LIST: list[str] = []
    if args.verbose:
        print('\nParameters: ')
        print(colored(f'Verbose mode enabled. Suppressing output.', 'green'))
        RETURN_LIST.append('verbose')
        
    if args.mode:
        print(colored(f'Running ForceUrSelf in bruteforce mode', 'green')) if args.verbose else None
        RETURN_LIST.append(f'mode:::{args.mode}')
        
        if args.username and args.password_list:
            print(colored(f'Username: {args.username}\nPassword list: {args.password_list}', 'green')) if args.verbose else None
            RETURN_LIST.append(f'username:::{args.username}')
            RETURN_LIST.append(f'password_list:::{args.password_list}')
    
    if args.proxy:
        print(colored(f'Using proxies', 'green')) if args.verbose else None
        RETURN_LIST.append('proxy')
        
    if args.url:
        print(colored(f'Using URL: {args.url}', 'green')) if args.verbose else None
        RETURN_LIST.append(f'url:::{args.url}')
        
    if args.out_file:
        print(colored(f'Output file: {args.out_file}', 'green')) if args.verbose else None
        RETURN_LIST.append(f'out_file:::{args.out_file}')

    return RETURN_LIST

def get_tor_path(OS) -> str:
    # Method to get the tor path
    if OS == 'linux':
        TOR_PATH = '../assets/Tor/tor/tor'
    elif OS == 'windows':
        TOR_PATH = '..\\assets\\Tor\\tor\\tor.exe'
    return TOR_PATH

def get_random_user_agent() -> str:
    # Method to get a random user agent
    USER_AGENTS: list[str] = open('../assets/user_agents.txt', 'r').readlines()
    return random.choice(USER_AGENTS).strip()
    
def get_random_port() -> int:
    # Method to get a random port
    return random.randint(10000, 65535)

def get_ip() -> str:
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location() -> dict:
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def log_output(output) -> None:
    with open(OUT_FILE, 'a') as file:
        file.write(f'{output}\n')
    
def clear_output() -> None:
    with open(OUT_FILE, 'w') as file:
        file.truncate(0)
        
def set_output_file(out_file) -> None:
    global OUT_FILE
    OUT_FILE = out_file
    
def print_goodbye() -> None:
    print(colored('ForceUrSelf has finished running!.', 'red'))
    print(colored('Thanks for using ForceUrSelf!', 'yellow'))
    print(colored('Made with <3 by @FujiwaraChoki!', 'green'))
    print(colored('GitHub: https://github.com/FujiwaraChoki/', 'blue'))
    