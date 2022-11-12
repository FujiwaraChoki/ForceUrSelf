'''
Methods file for ForceUrSelf
'''
from termcolor import colored

def print_logo() -> None:
    # Method to print the logo
    with open('../assets/logo.txt', 'r') as logo:
        print(colored(logo.read(), 'blue'))

def parse_args(args) -> list[str]:
    # Method to parse arguments
    print('Parameters: ')
    if args.verbose:
        print(colored(f'Verbose mode enabled', 'green'))
        
    if args.mode == 'bruteforce':
        print(colored(f'Running ForceUrSelf in bruteforce mode', 'green'))
        
        if args.username and args.password_list:
            print(colored(f'Username: {args.username}\nPassword list: {args.pl}', 'green'))
    
    if args.proxy:
        print(colored(f'Using proxy: {args.proxy}', 'green'))