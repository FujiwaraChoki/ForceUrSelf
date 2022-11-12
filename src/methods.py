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
        print(colored(f'Using proxy: {args.proxy}', 'green'))
        RETURN_LIST.append(f'proxy:::{args.proxy}')
        
    if args.url:
        print(colored(f'Using URL: {args.url}', 'green'))
        RETURN_LIST.append(f'url:::{args.url}')

    return RETURN_LIST
