import subprocess, json
from sys import stdout

def liveSave(func, logfile = 'sensors.log'):
    """Display live data to the screen and
       saving the computed data to sensor.log file.
    """
    with open(logfile, 'wb') as f:
        p = subprocess.Popen(func, stdout=subprocess.PIPE,shell=True)
        for c in iter(lambda: p.stdout.read(1), b''):
            a=c.decode("utf-8") #to write to stdout needs to be decoded
            stdout.write(a)
            f.write(c)    #needs to write in byte like format


def execute(func):
    '''Interface to shell

    Returns:
        tuple: returnCode = 0 for success, > 0 error, -N for signal N
        output = string, JSON string or None
        err = error message or None
    '''
    fSplit = func.split() #secure call
    p = subprocess.Popen(
            fSplit,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
            text=True)
    output, err = p.communicate()
    try:
        output = json.loads(output)
    except json.JSONDecodeError:
        pass
    return p.returncode, output, err
