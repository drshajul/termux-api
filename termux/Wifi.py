'''Termux-API WiFi methods

    on       - Enable Wifi
    off      - Disable Wifi
    info     - Connection information (JSON)
    scaninfo - Last scan info (JSON)
'''
from . import scrip as t

def on():
    '''
    Enable WiFi
    '''
    return t.compute("termux-wifi-enable true")["output"]

def off():
    '''
    Disable WiFi
    '''
    return t.compute("termux-wifi-enable false")["output"]
    


def info():
    '''
    Return wifi connection info (json format)
    '''
    return t.compute(f"termux-wifi-connectioninfo")["output"]

def scaninfo():
    '''
    Return last wifi scan info (json format)
    '''
    return t.compute(f"termux-wifi-scaninfo")["output"]
