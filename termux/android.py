import subprocess, json
from sys import stdout

def liveSave(func: str, logfile: str = 'sensors.log'):
    """Display live data to the screen and
       saving the computed data to sensor.log file.
    """
    with open(logfile, 'wb') as f:
        p = subprocess.Popen(func, stdout=subprocess.PIPE)
        for c in iter(lambda: p.stdout.read(1), b''):
            a = c.decode("utf-8") #to write to stdout needs to be decoded
            stdout.write(a)
            f.write(c)    #needs to write in byte like format


def execute(func: list, stdin: str = ""):
    '''Interface to shell

    Returns:
        tuple: returnCode = 0 for success, > 0 error, -N for signal N
        output = string, JSON string or None
        err = error message or None
    '''
    func = [str(i) if type(i) in (int, float) else i for i in func]
    p = subprocess.Popen(
            func,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
            text=True)
    output, err = p.communicate(stdin)
    try:
        output = json.loads(output)
    except json.JSONDecodeError:
        pass
    return p.returncode, output, err
