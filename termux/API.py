''' Misc API methods from termux-api'''

from .android import execute

def __dir__():
    return ['generic', 'battery', 'brightness', 'contactlist', 'download', 'fingerprint', 'getfile', 'location', 'torch', 'vibrate', 'volume']

def generic(func: list):
    '''
    Any function can be called, which will be passed directly
        to subprocess.Popen, and result returned. Call this if you
        know what you are doing.
    eg. termux.API.generic(["termux-toast", "-g", "middle", "-s", "Hello"])
    for more info visit [termux API](https://wiki.termux.com/wiki/Termux:API)
    '''
    return execute(func)

def battery():
    '''
    Returns battery status info.
    '''
    return execute(["termux-battery-status"])

def brightness(Brightness: int = 100):
    '''
    Set the brightness of your device.

    Parameters
    ----------
    Brightness : int, optional
        int value from 0 - 100 (default is 100)
    '''
    return execute(["termux-brightness", Brightness])

def vibrate(duration: int = 1000, force: bool = False):
    '''
    vibrates your phone.

    Parameters
    ----------
    duration : int, optional
    force: bool
        Force vibrate even in silent mode, default = False

    '''
    return execute(["termux-vibrate", "-d", duration])


def contactlist():
    '''
    Dumps all contact avalable on the phone.
    '''
    return execute(["termux-contact-list"])

def fingerprint():
    '''
    Use fingerprint sensor on device to check for authentication.
    '''
    return execute(["termux-fingerprint"])


def torch(switch: bool =True):
    '''
    Toggles the torch on/off

    Parameter
    ----------
    switch: bool
        True for on, False for off (Default is True)
    '''
    status = "on" if switch else "off"
    return execute(["termux-torch", status])


def download(url, description: str = "From termux",title: str = "Download"):
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
    return execute(["termux-download", "-t", title, url])

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
    cmd = "termux-volume"
    if(len(kwargs) > 0):
        stream = "ring"; volume = "5"
        stream = kwargs.get('stream', 'ring')
        volume = kwargs.get('volume', "5")
        cmd += [stream, volume]
    return execute(cmd)

def location(provider: str = None, request: str = None):
    '''
    Location of device.

    Parameters
    ----------
    provider  [gps/network/passive] (default: gps)
    request   [once/last/updates] (default: once)

    '''
    opt =["termux-location"]
    if provider:
        opt += ["-p", provider]
    if request:
        opt += ["-r", request]
    return execute(opt)

def getfile(saveas: str):
    '''
    Request a file from the system and write it to the specified file.
    '''
    return execute(["termux-storage-get", saveas])
