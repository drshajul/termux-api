'''Termux-API Clipboard methods

    getclipboard - get current clipboard text
    setclipboard - set clipboard text
'''

from .android import execute

def getclipboard():
   '''
   Returns value stored in the clipboard.
   '''
   return execute(["termux-clipboard-get"])

def setclipboard(newClip: str = " "):
    '''
    Set new value to clipboard

    Parameters
    ----------
    newClip: (optional) - new clipboard text (default is empty string)
    '''
    return execute(["termux-clipboard-set"], stdin=newClip)
