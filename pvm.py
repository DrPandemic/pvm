import re
from subprocess import check_output
import sys
import os

#TODO : say how to add the source

acceptedCommands = [('help', 0),('ls', 0), ('use', 1), ('use', 0), ('set', 1), ('set', 0)]
cachedVersions = None

configFolder = os.getenv('PVM')
configBin = configFolder+'/python'

def getVersions ():
    global cachedVersions
    if cachedVersions is not None:
        return cachedVersions
    pyFileRegex = re.compile('^python[0-9]\.?[0-9]?$').search
    versions = filter(pyFileRegex, os.listdir('/usr/bin'))
    cachedVersions = versions
    return versions

def printVersions ():
    print('\nYou currently have those versions installed (some may be symlinks):')
    for count, version in enumerate(getVersions()):
        print('(' + str(count) + ') ' + version)

def useVersion (path):
    if os.path.exists(configBin):
        os.remove(configBin)
    os.symlink(path, configBin)
def setVersion (path):
    return

def getVersionPath (version):
    if 'python' + version not in getVersions():
        return None
    return '/usr/bin/python' + version

def checkVersionByPosition (value):
    return isinstance(value, int) and value >= 0 and value < len(getVersions())
def useVersionByPosition (versionNumber, isSet):
    if not checkVersionByPosition(versionNumber):
        return False
    #get the version
    #if isSet
    #return setVersion
    #else
    #return useVersion(completeVersion)
    return True

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
        printVersions()
        exit(0)
    elif args[1] == 'use' and len(args) == 2:
        printVersions()
        exit(useVersionByPosition(input('Which version do you want to use? '), False) if 0 else 1)
    elif args[1] == 'use' and len(args) == 3:
        path = getVersionPath(args[2])
        if path is None:
            print('This version is not present on the system')
            exit(1)
        useVersion(path)
        exit(0)
    elif args[1] == 'set' and len(args) == 2:
        printVersions()
        exit(useVersionByPosition(input('Which version do you want to set as default? '), True) if 0 else 1)
    elif args[1] == 'set' and len(args) == 3:
        exit(setVersion(args[2]))


def showHelp ():
    print('Python Version Manager\n')
    print('Usage:')
    print(' pvm help                Show this message')
    print(' pvm list                List installed versions')
    print(' pvm use                 Show installed versions and let you choose which one to use')
    print(' pvm use version         Let you choose which version to use')
    print(' pvm set                 Show installed versions and let you choose which one to set as default')
    print(' pvm set version         Let you choose which version to set as default')

checkArgv()