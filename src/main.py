import sys
import os
import encoder
import decoder
import embossing


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
    path = '../.kintai_info'
    if os.path.exists(path):
        info = decoder.decodeInfo(path)
        if embossing.applyEmbossing(info):
            print("Embossing is Successfully!🍻")
    else:
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
    if command == 'apply':
        apply()
    elif command == 'show':
        show()
    elif command == 'init':
        initialize()
