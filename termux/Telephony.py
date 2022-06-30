''' Telephony API methods from termux-api

Avaliable methods are:
    call       - make a phone call to number (str)
    cellinfo   - retrieve cell information (json)
    deviceinfo -
'''

from .android import execute

def __dir__():
    return ['call', 'cellinfo', 'deviceinfo']

def call(phone_number: str):
    '''
    Makes a phone call to number passed as an argument
    '''
    return execute(["termux-telephony-call", phone_number])

def cellinfo():
    '''
    Get information about all observed cell information
    from all radios on the device including the primary
    and neighboring cells. (JSON format)
    '''
    return execute(["termux-telephony-cellinfo"])

def deviceinfo():
    '''
    Get information about the telephony device. 
    '''
    return execute(["termux-telephony-displayinfo"])
