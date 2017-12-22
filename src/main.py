import sys
import os
import encoder
import decoder

def initialize():
    print('Start Initialize ...')
    if not encoder.createInfo():
        print('Error: couldn\'t initialize.')
        sys.exit(1)
    else:
        print('Do you want to apply? (y/n)')
        answer = input()
        if answer is 'y' or answer is 'yes':
            apply()
        else:
            print('Initialize is Done!! :\)')

def apply():
    print("Sorry. not implement..")
    sys.exit(0)

def show():
    print("Sorry. not implement..")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Not fill command...")
        print("USAGE: python main.py [apply, show, init]")
        sys.exit(1)

    command = sys.argv[1]
    print(command)
    if command == 'apply':
        apply()
    elif command == 'show':
        show()
    elif command == 'init':
        initialize()
    else:
        print("Error: invalid command")

