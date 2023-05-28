''' Termux-API Wakelock

    Methods
    ------------
    lock - Trigger a wakelock which causes Android not to go into deep sleep.
    unlock - Release wakelock.
'''

from .android import execute

def lock():
    '''
    Trigger a wakelock which causes Android not to go into deep sleep.
    '''
    return execute(["termux-wake-lock"])

def unlock():
    '''
    Release wakelock.
    '''
    return execute(["termux-wake-unlock"])
