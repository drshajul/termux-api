''' Termux-API sensors live data

    Methods
    ------------
    sensors - Lists available sensors on the device
    cleanup - Performs cleanup releasing sensor resources.
    sensorsData - Output specific sensor(s) data. (limit = 1)
    allSensorsData - Output all sensors data (limit = 1)
    liveSaveLog - Live sensor data to stdout and to log file.    
'''

from .android import execute,liveSave

def sensors():
    '''
    Lists available sensors on the device.
    '''
    return execute("termux-sensor -l")

def cleanup():
    '''
    Performs cleanup releasing sensor resources.
    '''
    return execute("termux-sensor -c")

def sensorsData(*args):
    '''
    Output specific sensor(s) data. (JSON)
    You can pass multiple sensor names as arguments.
    As live data is not useful when calling from 
    python, only one reading is retrieved by this method.
    If you need continous data, you can create a 
    loop in python
    '''
    sname=tuple(args)
    if not sname:
        return "At least one sensor name required. \nFor finding sensor name call sensors() method"
    else:
        sensornames=""
        for v in sname:
            sensornames += v + ","      
        return execute(f"termux-sensor -n 1 -s {sensornames[0:-1]}")


def allSensorsData():
    '''
    Method to print sensor data all at once.
    As live data is not useful when calling from 
    python, only one reading is retrieved by this method.
    If you need continous data, you can create a 
    loop in python
    '''
    return execute("termux-sensor -n 1 -a")


def liveSaveLog(sensors, logfile = 'sensors.log', delay = 1000, limit = 60):
    '''
    Live sensor data to stdout and to log file.

    Parameters
    ----------
    sensors = tuple of sensors to query data for (or string sensor)
    logfile = file to log to (default is 'sensors.log')
    delay = delay between querying sensor (default 1000 ms)
    limit = number of time to query (default 60, 0 for no limit)

    Example:
    > > > sensors = 'gravity', 'Orientation'
    > > > liveSaveLog( sensors , limit = 10 )
    '''
    if type(sensors) is tuple:
        sensornames=""
        for v in sensors:
            sensornames += v + ","      
        liveSave(f"termux-sensor -d {delay} -n {limit} -s {sensornames[0:-1]}", logfile)
    elif type(sensors) is str:
        liveSave(f"termux-sensor -d {delay} -n {limit} -s {sensors}", logfile)
    else:
        return 'Invalid sensors argument'
