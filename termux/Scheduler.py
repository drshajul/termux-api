'''Termux-API Job Scheduler methods

    cancel    - Cancel job with given id
    cancelAll - Cancel all jobs
    listAll   - list pending jobs
    schedule  - schedule new job
'''
from .android import execute

def _makeopt(str):
    '''
    Convert var like "batteryNotLow" to argument like "battery-not-low".
    '''
    res = [str[0].lower()] 
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res.append('-') 
            res.append(c.lower()) 
        else: 
            res.append(c) 
    return ''.join(res) 

def cancel(jid: int):
    '''
    Cancel job with the given id
    '''
    return execute(["termux-job-scheduler", "--cancel", jid])

def cancelAll():
    '''
    Cancel all jobs
    '''
    return execute(["termux-job-scheduler", "--cancel-all"])

def listAll():
    '''
    List pending jobs
    '''
    return execute(["termux-job-scheduler", "-p"])

def schedule(script: str, jid: int, **kwargs):
    '''
    Schedule a script to run at specified intervals. 

    Parameters
    ----------
    script :str         path of script to be called
    jid :int            overwrites previous job if same id
    periodMs :int       milliseconds (default 0 means once).
                          Since Android N, the minimum period
                          is 900,000ms (15 minutes).
    network :str        run only when network type available 
                          (default any)
                          any|unmetered|cellular|not_roaming|none
    batteryNotLow :bool run only when battery is not low
                          default true (>= Android O)
    storageNotLow :bool run only when storage is not low
                          default false (>= Android O)
    charging :bool      run only when charging, default false
    persisted :bool     survive reboots, default false
    triggerContentUri  :str  (>= Android N)
    triggerContentFlag :int  default 1, (>= Android N)
    '''
    kargs = []
    
    if len(kwargs) > 0:
        for k,v in kwargs.items():
            kargs.append("--" + _makeopt(k))
            if type(v) is bool:
                kargs.append(str(v).lower())
            else:
                kargs.append(v)

    return execute(["termux-job-scheduler", "-s", script, "--job-id", jid] + kargs)

