import sys
import os
import encoder
import decoder


def main():
    path = './.kintai_info'
    if os.path.exists(path):
        decoder.decodeInfo(path) 
        # do decoder from path
    else:
        # do create info
        #encoder.createInfo()

if __name__ == "__name__":
    main()
