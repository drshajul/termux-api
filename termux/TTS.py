''' Termux-API Text-to-Speech

    tts_info   - Get tts-engines info (JSON)
    tts_speak  - Text to speech
'''
from .android import execute

def tts_info():
    '''
    Get tts-engines info (JSON format).
    '''
    return execute(["termux-tts-engines"])


def tts_speak(text, **kwargs):
    '''
    Text to speech.  

    Parameters
    ----------
    text: text to speak
    engine: (optional) TTS engine to use. see ttsinfo()
    language: (optional) language
    pitch: (optional) pitch
    rate: (optional) rate
    stream: (optional) audio stream to use
    region: (optional) language region
    variant: (optional) language variant 
    for more info visit [termux wiki](https://wiki.termux.com/wiki/Termux-tts-speak)

    TODO: Implement os.mkfifo() and os.pipe() 
    '''
    opts = []
    params = {
        "engine" : "e",
        "language" : "l",
        "region" : "n",
        "variant" : "v",
        "pitch" : "p",
        "rate" : "r",
        "stream" : "s"}
    
    for k,v in kwargs.items():
        opts += ['-'+params[k], v]
    
    return execute(["termux-tts-speak"] + opts +[text])