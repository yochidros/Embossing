import textwrap


def printBanner():
    string = textwrap.dedent('''
     _____           _                   _
    | ____|_ __ ___ | |__   ___  ___ ___(_)_ __   __ _
    |  _| | '_ ` _ \| '_ \ / _ \/ __/ __| | '_ \ / _` |
    | |___| | | | | | |_) | (_) \__ \__ \ | | | | (_| |
    |_____|_| |_| |_|_.__/ \___/|___/___/_|_| |_|\__, |
                                                 |___/
    ''')
    print(string)


def printHelp():
    printBanner()
    print("USAGE: python main.py [apply, show, init]")
    string = textwrap.dedent('''
    How:
        embossing by using jobcan(https://ssl.jobcan.jp/login/pc-employee/)

    Command:
        show    show screenshot Attendance record.
        apply   do embossing
        init    initialize user data.
        
        commonInit initialize user data for common Id page.
        applyCommon do embossing common id page.
    ''')
    print(string)
