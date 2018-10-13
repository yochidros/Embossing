import sys
import os
from Coder import decoder, encoder
from Embossing import embossing
from Helper import helper
import subprocess
import shutil

def __initialize():
    print('Start common Initialize ...')
    if not encoder.createCommonIdInfo():
        print('Error: couldn\'t common initialize')
        sys.exit(1)
    else:
        print('Do you want to apply embossing? as CommonID (y/n)')
        answer = input()
        if answer is 'y' or answer is 'yes':
            __apply()
        else:
            print('Initialize is Done!! 🐶')


def __getInfo():
    path = '/home/yochidrop/yochio/Embossing/.kintai_common_info'
    if os.path.exists(path):
        info = decoder.decodeCommonInfo(path)
        return info
    else:
        print("Error: couldn't find " + path)
        sys.exit(0)


def __apply():
    info = __getInfo()
    if embossing.applyEmbossing(info):
        print("Embossing is Successfully!🍻")


def __show():
    info = __getInfo()
    if embossing.capture_Attendance(info):
        if os.path.exists('./attendance.png'):
            shutil.copy2("./attendance.png", "../images/attendance.png")
            os.remove('attendance.png')

        # open screenshot
        subprocess.run(['xdg-open', '../images/attendance.png'])
        sys.exit(0)
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
