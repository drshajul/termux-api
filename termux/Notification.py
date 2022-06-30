'''Termux-API Notification methods

    notify - Create the notification
    remove - Remove notificaiton with the given id
'''
from .android import execute

def remove(nid: int):
    '''
    Remove notificaiton with the given id
    '''
    return execute(["termux-notification-remove", nid])


def notify(title: str, content: str, nid: int = 1, args: tuple = (), kwargs: dict = {}):
    '''
    Create a notification

    Parameters
    ----------
    title: Title of notification
    content: Content of notification
    nid: (optional) The id for the notification,
        required to remove notification
    args: (optional) A tuple of arguments, eg ("ongoing", "sound")
    kwargs: (optional) A dict of args, eg {"led-color": "ff00ff"}
    
    For more info visit
        [termux wiki](https://wiki.termux.com/wiki/Termux-notification)
    '''
    cargs = kargs = []
    if len(args) > 0:
        for v in args:
            cargs.append(f"-{v}" if (len(v) == 1) else f"--{v}")
    
    if len(kwargs) > 0:
        for k,v in kwargs.items():
            kargs += [(f"-{k}" if (len(k) == 1) else f"--{k}"), str(v)]

    opts = cargs + kargs

    return execute(["termux-notification", "-t", title, "-c", content, "-i", nid] + opts)
