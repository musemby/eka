#!/usr/bin/python


import os
import sys
import dominus
import tqdm
import time
from termcolor import colored



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.BOLD + "\n                    DOMINUS TECH\n" + bcolors.ENDC



if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print'                             Compression:\n'
        print bcolors.BOLD+'Use: de_encode_interface.py [When prompted, put the directory for compressed file]'+bcolors.ENDC
    else:
        if len(sys.argv) != 3:
            interactive = 1
            fromdir = raw_input(colored('[+][+]', 'green')+bcolors.WARNING+' File to compress dir > '+ bcolors.ENDC)
            tofile  = raw_input(colored('[+][+]', 'green')+bcolors.WARNING+' Compressed file dir  > '+ bcolors.ENDC)
        else:
            interactive = 0
        print colored(fromdir, 'blue') # Print user input for the compressed directory
        print colored('Your file will be created in this directory:\n'+tofile, 'blue') # print directory where new decompressed file will be created
        print colored('\nCompressing file....', "yellow") # Print the process in terminal
        #
        # Print the percentage
        for n in tqdm.tqdm(range(1000)):
            #time.sleep(0.01)
            infile = dominus.readbytes(fromdir)
            compressed = dominus.compress(infile)
            dominus.writebytes(tofile, compressed)
        print colored('\nCompression complete!', 'green')

        if interactive: raw_input('Press Enter key') # pause if clicked



