import sys
import os
import encoder
import decoder

def main():
    path = './.kintai_info'
    if os.path.exists(path):
        decoder.decodeInfo(path) 
    else:
        encoder.createInfo()

if __name__ == '__main__':
    main()
