'''Termux-API Clipboard methods

    getclipboard - get current clipboard text
    setclipboard - set clipboard text
'''

from . import scrip as t

def getclipboard():
   '''
   Returns value stored in the clipboard.
   '''
   return t.compute("termux-clipboard-get")["output"]

def setclipboard(newClip: str =" "):
    '''
    Set new value to clipboard

    Parameters
    ----------
    newClip: (optional) - new clipboard text (default is empty string)
    '''
    return t.compute(f"termux-clipboard-set {newClip}")["output"]