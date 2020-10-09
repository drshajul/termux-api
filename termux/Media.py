'''Termux-API media player and scanner methods

play - play specified file
control - control playback (play, pause, stop)
info - playback information
scan - scan file(s) & add to media content provider

'''
from .android import execute

def play(file):
    '''Play specified file

    Parameters
    ----------
    file    file to play
    '''
    return execute(f'termux-media-player play "{file}"')

def control(dothis):
    '''Control playback

    Parameters
    ----------
    dothis  =  play / pause / stop (str)
    '''
    return execute(f"termux-media-player {dothis}")

def info():
    '''Playback information
    '''
    return execute(f"termux-media-player info")

def scan(file_s, recursive :bool = False, verbose: bool = False):
    '''Scan the specified file(s) and add to the media content provider

    Parameters
    ----------
    file_s : Single file (str) or a tuple of files (tuple)\n
    recursive : Recursive scan directories, by default False\n
    verbose : Verbose mode, by default False
        
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
    return execute(f"termux-media-scan {opt} {f}")
    