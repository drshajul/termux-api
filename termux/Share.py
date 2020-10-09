'''Termux-API Share methods

    text - Share specified text
    file - Share specified file
'''
from .android import execute

def text(text: str, action = "send", defaultReciever = False):
  '''
  Share text

  Parameters
  ----------
  action = edit/send/view (default: send)
  defaultReciever  = default receiver instead of showing a chooser
  '''
  opt = f"-a {action}"
  if defaultReciever:
    opt += " -d"
  
  return execute(f'echo "{text}" | termux-share {opt}')

def file(filepath: str, action = "send", defaultReciever = False, contentType = None, title = None):
  '''
  Share text

  Parameters
  ----------
  action = edit/send/view (default: send)
  defaultReciever  = default receiver instead of showing a chooser
  contentType = eg, "text/plain" (default: guessed from file extension)
  title = title to share (default: None)
  '''
  opt = f"-a {action}"
  if defaultReciever:
    opt += " -d"
  if contentType is not None:
    opt += " -c {contentType}"
  if title is not None:
    opt += " -t {title}"
  
  return execute(f'termux-share {opt} "{filepath}"')
