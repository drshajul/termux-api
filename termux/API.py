''' Misc API methods from termux-api'''

from . import scrip as t

def __dir__():
    return ['generic', 'battery', 'brightness', 'contactlist', 'download', 'fingerprint', 'getfile', 'location', 'torch', 'vibrate', 'volume']

def generic(funcName: str):
    '''
    Any function can be called, which will be passed directly 
        to subprocess.Popen, and result returned. Call this if you
        know what you are doing.
    eg. termux._generic('termux-toast -g middle -s "Hello"')
    for more info visit [termux API](https://wiki.termux.com/wiki/Termux:API)
    '''
    return t.compute(funcName)["output"]

def battery():
    '''
    Returns battery status info.
    '''
    return t.compute("termux-battery-status")["output"]  

def brightness(Brightness: int =100):
    '''
    Set the brightness of your device.

    Parameters
    ----------
    Brightness : int, optional
        int value from 0 - 100 (default is 100)
    '''
    return t.compute(f"termux-brightness {Brightness}")["output"]

def vibrate(duration: int =1000, force: bool = False):
    '''
    vibrates your phone.

    Parameters
    ----------
    duration : int, optional
    force: bool 
        Force vibrate even in silent mode, default = False
        
    '''
    extra = "-f" if (force) else ""
    return t.compute(f"termux-vibrate -d {duration} {extra}")["output"]


def contactlist():
    '''
    Dumps all contact avalable on the phone.
    '''
    return t.compute("termux-contact-list")["output"]

def fingerprint():
    '''
    Use fingerprint sensor on device to check for authentication.
    '''
    return t.compute("termux-fingerprint")["output"]


def torch(switch: bool =True):
    '''
    Toggles the torch on/off
    
    Parameter
    ----------
    switch: bool 
        True for on, False for off (Default is True)
    '''
    cmd = "termux-torch on" if (switch) else "termux-torch off"
    return t.compute(cmd)["output"]


def download(url, description: str ="From termux",title: str ="Download"):
    '''
    This is the method for downloading anything from the internet.

    Parameters
    ----------
    url
        the url to download
    description (optional)
        description for the download request notification
    title (optional)
        title for the download request notification
    '''
    return t.compute(f"termux-download -t {title} {url}")["output"]

def volume(**kwargs):
    '''
    Change volume of specified audio stream.
    Called without arguments, returns all volume info as json.

    Parameters
    ----------
    stream: str (optional)
      Valid audio streams are: alarm, music, notification, ring, system, call.
    volume: str (optional)
    '''
    if(len(kwargs) == 0): 
      cmd = "termux-volume" 
    else:
      stream = "ring"; volume = "5"
      if 'stream' in kwargs:
        stream = kwargs['stream']
      if 'volume' in kwargs:
        volume = kwargs['volume']
      cmd = f"termux-volume {stream} {volume}" 
    return t.compute(f"termux-volume")["output"]

def location(provider: str = None, request: str = None):
    '''
    Location of device.

    Parameters
    ----------
    provider  [gps/network/passive] (default: gps)
    request   [once/last/updates] (default: once)
        
    '''
    opt = f"-p {provider} " if provider is not None else ""
    opt += f"-r {request}" if request is not None else ""
    return t.compute(f"termux-location {opt}")["output"]

def getfile(saveas: str):
    '''
    Request a file from the system and write it to the specified file. 
    '''
    return t.compute(f"termux-storage-get {saveas}")["output"]