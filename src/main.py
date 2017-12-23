import sys
import os
from Coder import decoder, encoder
from Embossing import embossing
from Helper import helper
from threading import Thread


def __initialize():
    print('Start Initialize ...')
    if not encoder.createInfo():
        print('Error: couldn\'t initialize.')
        sys.exit(1)
    else:
        print('Do you want to apply embossing? (y/n)')
        answer = input()
        if answer is 'y' or answer is 'yes':
            __apply()
        else:
            print('Initialize is Done!! 🐶')


def __getInfo():
    path = '../.kintai_info'
    if os.path.exists(path):
        info = decoder.decodeInfo(path)
        return info
    else:
        print("Error: couldn't find " + path)
        sys.exit(0)


def __apply(info):
    if embossing.applyEmbossing(info):
        print("Embossing is Successfully!🍻")


def __show():
    info = __getInfo()
    if embossing.capture_Attendance(info): 
        print("hello")
    else:
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Not fill command...")
        print("USAGE: python main.py [apply, show, init]")
        sys.exit(1)

    command = sys.argv[1]
    if command == 'apply':
        helper.printBanner()
        __apply()
    elif command == 'show':
        helper.printBanner()
        __show()
    elif command == 'init':
        helper.printBanner()
        __initialize()
    elif command == '-h' or command == 'help':
        helper.printHelp()
