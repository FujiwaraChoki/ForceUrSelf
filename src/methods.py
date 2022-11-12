'''
Methods file for ForceUrSelf
'''
def print_logo() -> None:
    # Method to print the logo
    with open('../assets/logo.txt', 'r') as logo:
        print(logo.read())
        