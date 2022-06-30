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
    return execute(["termux-media-player", "play", file])

def control(opt):
    '''Control playback

    Parameters
    ----------
    opt  =  play / pause / stop (str)
    '''
    return execute(["termux-media-player", opt])

def info():
    '''Playback information
    '''
    return execute(["termux-media-player", "info"])

def scan(file_s, recursive :bool = False, verbose: bool = False):
    '''Scan the specified file(s) and add to the media content provider

    Parameters
    ----------
    file_s : Single file (str) or a tuple of files (tuple|list)\n
    recursive : Recursive scan directories, by default False\n
    verbose : Verbose mode, by default False
        
    '''    
    if isinstance(file_s, str):
        file_s = [file_s]
    file_s = list(file_s)
    opt = []
    if recursive:
      opt += ["-r"]
    if verbose:
      opt += ["-v"]
    return execute(["termux-media-scan"] + opt + file_s)
    