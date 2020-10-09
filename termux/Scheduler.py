'''Termux-API Job Scheduler methods

    cancel    - Cancel job with given id
    cancelAll - Cancel all jobs
    listAll   - list pending jobs
    schedule  - schedule new job
'''
from . import scrip as t

def _makeopt(str): 
    res = [str[0].lower()] 
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res.append('-') 
            res.append(c.lower()) 
        else: 
            res.append(c) 
    return ''.join(res) 

def cancel(id: int):
    '''
    Cancel job with the given id
    '''
    return t.compute(f"termux-job-scheduler --cancel {id}")["output"]

def cancelAll():
    '''
    Cancel all jobs
    '''
    return t.compute("termux-job-scheduler --cancel-all")["output"]

def listAll():
    '''
    List pending jobs
    '''
    return t.compute("termux-job-scheduler -p")["output"]

def schedule(script: str, id: int, **kwargs):
    '''
    Schedule a script to run at specified intervals. 

    Parameters
    ----------
    script :str         path of script to be called
    id :int             overwrites previous job if same id
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
    kargs = ""
    
    if len(kwargs) > 0:
        for k,v in kwargs.items():
            if type(v) is bool:
                kargs += f"--{_makeopt(k)} " + f'{str(v).lower()} '
            elif type(v) is int:
                kargs += f"--{_makeopt(k)} " + f'{v} '
            else:
                kargs += f"--{_makeopt(k)} " + f'"{v}" '

    return f'termux-job-scheduler -s "{script}" --job-id {str(id)} {kargs}'

