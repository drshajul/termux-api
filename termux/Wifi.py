'''Termux-API WiFi methods

    on       - Enable Wifi
    off      - Disable Wifi
    info     - Connection information (JSON)
    scaninfo - Last scan info (JSON)
'''
from .android import execute

def on():
    '''
    Enable WiFi
    '''
    return execute(["termux-wifi-enable", "true"])

def off():
    '''
    Disable WiFi
    '''
    return execute(["termux-wifi-enable", "false"])

def info():
    '''
    Return wifi connection info (json format)
    '''
    return execute(["termux-wifi-connectioninfo"])

def scaninfo():
    '''
    Return last wifi scan info (json format)
    '''
    return execute(["termux-wifi-scaninfo"])
