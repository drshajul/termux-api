'''Termux-API Camera methods

    info      - Returns camera info in JSON format
    takephoto - Take photo with specified camera
'''

from .android import execute
from datetime import datetime

def info():
    '''
    Returns camera info in JSON format
    '''
    return execute(["termux-camera-info"])

def takephoto(cid=0, saveas=None):
    '''
    Take a picture

    Parameters
    ----------
    cid: camera id (int), default is 0
    saveas: output file name (str), default is <timestamp>.jpg
    '''
    if saveas is None:
        saveas = datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    return execute(["termux-camera-photo", "-c", cid, saveas])