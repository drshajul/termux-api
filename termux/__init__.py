'''
Termux API python wrapper

Available modules are:
  termux.API - Misc API methods, including generic call
  termux.Camera
  termux.Clipboard
  termux.Media - Playback and media scanner
  termux.Microphone
  termux.Notification
  termux.Scheduler - Job Scheduler
  termux.Sensors
  termux.Share
  termux.SMS
  termux.Telephony - make call, info of device and network
  termux.TTS - Text to speech
  termux.UI - Dialog Widgets and Toast
  termux.Wifi
  termux.Wake

For information about available methods, use
  help(termux.<modulename>)
'''

from . import API, Camera, Clipboard, Sensors, TTS, Wifi, Notification, Media, Microphone, Scheduler, Share, Telephony, UI, Wake, SMS


__all__ = sorted(["API", "Sensors", "Camera", "Clipboard", "TTS", "Wifi", "Notification",
                  "Media", "Microphone", "Scheduler", "Share", "Telephony", "UI", "Wake", "SMS"])