import subprocess
from sys import stdout


def liveSave(func, logfile = 'sensors.log'):
    '''
    liveSave is the function taking a function as an argument
    which need to compute sensor data displaying live
    data to the screen and saving the computed data
    to sensor.log file when on interrupt.
    '''
    with open(logfile, 'wb') as f:
        process = subprocess.Popen(func, stdout=subprocess.PIPE,shell=True)
        for c in iter(lambda: process.stdout.read(1), b''):
            a=c.decode("utf-8") #to write to stdout needs to be decoded
            stdout.write(a)
            f.write(c)    #needs to write in byte like format


def compute(func):
    '''
    compute is the function takinga function as an argument
    which need to generate final computed data 
    as an output. It only saves data to return variable
    not for only the time the program runs.
    '''
    outvalue_tuple = subprocess.Popen(
            func,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,shell=True)
    output,err=outvalue_tuple.communicate()
    output=output.decode("utf-8").replace("\n","")
    err=err.decode("utf-8")
    if err !="":
        return {"output":err}
    elif output=="":
        return {"output":"OK"} 
    else:
        return {"output":output} 


