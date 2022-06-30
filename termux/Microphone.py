''' Telephony Microphone methods from termux-api

Avaliable methods are:
    record - record microphone
    info   - retrieve recording info
    stop   - stop recording
'''

from .android import execute

def __dir__():
    return ['record', 'info', 'stop']

def record(file: str, limit: int = 0, **kwargs):
    '''
    Record to specified file, limit in seconds. 
    If no other parameters, uses default settings

    Parameters
    ----------
      file:    file to record to\n
      limit:   record w/ limit (seconds, 0 = unlimited)\n
      encoder: record w/ encoder (aac, amr_wb, amr_nb)\n
      bitrate: record w/ bitrate (in kbps)\n
      rate:    record w/ sampling rate (in Hz)\n
      count:   record w/ channel count (1, 2, ...)
    '''   

    params = {
      "encoder": "-e",
      "bitrate": "-b",
      "rate": "-r",
      "count": "-c"   
    }
    opt = []
    if len(kwargs) == 0:
      opt += ["-d"]
    else: 
      for k,v in kwargs.items():
        opt += [params[k], v]
    return execute(["termux-microphone-record", "-f", file, "-l", limit] + opt)

def info():
    '''
    Get recording information
    '''
    return execute(["termux-microphone-record", "-i"])

def stop():
    '''
    Quits recording 
    '''
    return execute(["termux-microphone-record", "-q"])
