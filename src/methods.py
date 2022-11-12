'''
Methods file for ForceUrSelf
'''
import random
from termcolor import colored

def print_logo() -> None:
    # Method to print the logo
    with open('../assets/logo.txt', 'r') as logo:
        print(colored(logo.read(), 'blue'))

def parse_args(args) -> list[str]:
    # Method to parse arguments
    RETURN_LIST: list[str] = []
    print('Parameters: ')
    if args.verbose:
        print(colored(f'Verbose mode enabled', 'green'))
        RETURN_LIST.append('verbose')
        
    if args.mode:
        print(colored(f'Running ForceUrSelf in bruteforce mode', 'green'))
        RETURN_LIST.append(f'mode:::{args.mode}')
        
        if args.username and args.password_list:
            print(colored(f'Username: {args.username}\nPassword list: {args.password_list}', 'green'))
            RETURN_LIST.append(f'username:::{args.username}')
            RETURN_LIST.append(f'password_list:::{args.password_list}')
    
    if args.proxy:
        print(colored(f'Using proxyies', 'green'))
        RETURN_LIST.append(f'proxy')
        
    if args.url:
        print(colored(f'Using URL: {args.url}', 'green'))
        RETURN_LIST.append(f'url:::{args.url}')

    return RETURN_LIST

def get_tor_path(OS) -> str:
    # Method to get the tor path
    if OS == 'linux':
        TOR_PATH = '../assets/tor/tor'
    elif OS == 'windows':
        TOR_PATH = '..\\assets\\Tor\\tor\\tor.exe'
    return TOR_PATH

def get_random_user_agent() -> str:
    # Method to get a random user agent
    USER_AGENTS: list[str] = open('../assets/user_agents.txt', 'r').readlines()
    return random.choice(USER_AGENTS)
    