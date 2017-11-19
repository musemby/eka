#!/usr/bin/python


import os
import sys
import dominus
from termcolor import colored
#from termcolor import colored

#print colored('hello', 'red'), colored('world', 'green')
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
        print 'Use: de_encode_interface.py [When prompted, put the directory for compressed file]'
    else:
        if len(sys.argv) != 3:
            interactive = 1
            fromdir = raw_input(colored('[+][+]', 'green')+bcolors.WARNING+' Directory containing file to Compress > '+ bcolors.ENDC)
            tofile  = raw_input(colored('[+][+]', 'green')+bcolors.WARNING+' To Directory NOTE: Not in Use!        > '+ bcolors.ENDC)
        else:
            interactive = 0
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        infile = dominus.readbytes(fromdir)
        compressed = dominus.compress(infile)
        dominus.writebytes(tofile, compressed)

        print 'Compression', absfrom, 'to make', absto

        try:
            print'Compressing file....'
            join(fromdir, tofile)
        except:
            print 'Error Compressing files:'
            print sys.exc_type, sys.exc_value
        else:
           print 'Compression Complete: see', absto
        if interactive: raw_input('Press Enter key') # pause if clicked



