''' Telephony Microphone methods from termux-api

Avaliable methods are:
    record - record microphone
    info   - retrieve recording info
    stop   - stop recording
'''

from . import scrip as t

def __dir__():
    return ['record', 'info', 'stop']

def record(file: str, limit: int = 0, **kwargs):
    '''
    Record to specified file, limit in seconds. 
    If no other parameters, uses default settings

    Parameters
    ----------
    file    file to record to
    limit   record w/ limit (seconds, 0 = unlimited)
    encoder record w/ encoder (aac, amr_wb, amr_nb)
    bitrate record w/ bitrate (in kbps)
    rate    record w/ sampling rate (in Hz)
    count   record w/ channel count (1, 2, ...)
    '''
    params = {
      "encoder": "-e",
      "bitrate": "-b",
      "rate": "-r",
      "count": "-c"   
    }; opt = ""
    if len(kwargs) == 0:
      opt = "-d"
    else: 
      for k,v in kwargs.items():
        opt += f"{params[k]} {v} "
    return t.compute(f"termux-microphone-record -f {file} -l {limit} {opt}")["output"]

def info():
    '''
    Get recording information
    '''
    return t.compute("termux-microphone-record -i")["output"]

def stop():
    '''
    Quits recording 
    '''
    return t.compute("termux-microphone-record -q")["output"]
