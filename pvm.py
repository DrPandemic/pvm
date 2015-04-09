import re
from subprocess import check_output
import sys

acceptedCommands = [('help', 0),('ls', 0), ('use', 1), ('use', 0)]

def byteToString (b): return b.decode('utf-8')
def listVersions ():
    pyFileRegex = re.compile('^python[0-9]\.?[0-9]?$').search
    files = map(byteToString, check_output(['ls', '/usr/bin']).splitlines())
    return filter(pyFileRegex, files)
def printVersions ():
    for count, version in enumerate(listVersions()):
        print('(' + str(count) + ') ' + version)

def checkArgv ():
    args = sys.argv
    if len(args) == 1:
        showHelp()
        exit(0)

    #Checks if the args are ok
    isOk = False
    for arg in acceptedCommands:
        if arg[0] == args[1] and len(args) == arg[1] + 2:
            isOk = True;

    #Manage different args
    if args[1] == 'help':
        showHelp()
        exit(0)
    elif args[1] == 'ls':
        print('\nYou currently have those Pythons installed (some may only be symlinks):\n')
        printVersions()

def showHelp ():
    print('Python Version Manager\n')
    print('Usage:')
    print(' pvm help                Show this message')
    print(' pvm list                List installed versions')
    print(' pvm use                 Show installed versions and let you choose which one to set as default')
    print(' pvm use version         Let you choose which version to use as default')

checkArgv()