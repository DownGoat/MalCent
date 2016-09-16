import os
from subprocess import Popen, PIPE

SSDEEP_LOCATION = "C:\\Users\\sis13\\Documents\\apps\\ssdeep\\ssdeep.exe"

def ssdeep(filename):
    process = Popen([SSDEEP_LOCATION, filename], stdout=PIPE)
    output = process.communicate()[0]

    return output.split("\n")[1].split(",")[0]

if __name__ == "__main__":
    ssdeep("C:\\Users\sis13\\Documents\\apps\\kitty.exe")