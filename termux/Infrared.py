"""Termux-API Infrared

    Methods
    ------------
    getfrequency - Returns the infrared transmitter's supported carrier frequencies
    transmit     - transmit infrared signals
"""

from .android import execute

def getfrequency():
    """
    Returns the infrared transmitter's supported carrier frequencies\n
    Note: This API can be used only on devices that have infrared transmitter
    """
    return execute["termux-infrared-frequencies"]

def transmit(frequency: int, pattern: str):
    """
    Transmit infrared signals

    Parameters
    ----------
    frequency : int - frequency of the infrared transmitter in Hertz\n
    pattern : str - pattern of the infrared signal, the pattern is specified in comma-separated on/off intervals, such as '20,50,20,30'
    """
    return execute(["termux-infrared-transmit", "-f", frequency, pattern])