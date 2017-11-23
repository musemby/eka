#!/usr/bin/python


import os
import sys
import dominus
#import progressbar
import tqdm
import time
from time import sleep
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
        print'                             Decompression:\n'
        print bcolors.BOLD+'Use: [No instruction yet]'+ bcolors.ENDC
    else:
        if len(sys.argv) != 3:
            interactive = 1
            fromdir = raw_input(colored('[+]', 'green')+bcolors.WARNING+' Compressed   File dir > '+ bcolors.ENDC)
            tofile  = raw_input(colored('[+]', 'green')+bcolors.WARNING+' Decompressed File dir > '+ bcolors.ENDC)
        else:
            interactive = 0
        print colored(fromdir, 'red') # Print user input for the compressed directory
        print colored('Your file will be created in this directory:\n'+tofile, 'blue') # print directory where new decompressed file will be created
        print colored('\nDecompressing file....', "yellow") # Print the process in terminal
        #
        # Print the percentage of the process
        for n in tqdm.tqdm(range(1000)):
            time.sleep(0.01)
            infile = dominus.readbytes(fromdir)
            uncompressed = dominus.decompress(infile)
            file2 = open(tofile,'w')
            for bt in uncompressed:
                file2.write(bt)

        if interactive: raw_input('Press Enter key') # pause if clicked

