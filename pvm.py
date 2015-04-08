import re
from subprocess import check_output

def byteToString (b): return b.decode('utf-8')

pyFileRegex = re.compile('python[0-9]\.?[0-9]?').search
files = map(byteToString, check_output(["ls", "-al", "/usr/bin"]).splitlines())
fFiles = filter(pyFileRegex, files)
for a in fFiles:
    print(a)
