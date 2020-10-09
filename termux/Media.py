'''Termux-API media player and scanner methods

play - play specified file
control - control playback (play, pause, stop)
info - playback information
scan - scan file(s) & add to media content provider

'''
from . import scrip as t

def play(file):
    '''Play specified file

    Parameters
    ----------
    file    file to play
    '''
    return t.compute(f'termux-media-player play "{file}"')["output"]

def control(dothis):
    '''Control playback

    Parameters
    ----------
    dothis  =  play / pause / stop (str)
    '''
    return t.compute(f"termux-media-player {dothis}")["output"]

def info():
    '''Playback information
    '''
    return t.compute(f"termux-media-player info")["output"]

def scan(file_s, recursive :bool = False, verbose: bool = False):
    '''Scan the specified file(s) and add to the media content provider. 

    file_s - Single file (str) or a tuple of files (tuple)
    recursive - Recursive scan directories (default: False)
    verbose - Get more information (default: False)
    '''
    if type(file_s) is tuple:
      f = "'" + "' '".join(file_s) + "'"
    elif type(file_s) is str:
      f = "'" + file_s + "'"
    else:
      return "file_s type invalid"
    opt = ""
    if recursive:
      opt += "-r "
    if verbose:
      opt += "-v"
    return t.compute(f"termux-media-scan {opt} {f}")["output"]
    