'''Termux-API SMS methods

    list_messages - List messages
    send - Send messages 
'''
from .android import execute

def listsms(limit: int = None, offset: int = None, msg_type: str = None, show_dates=False, show_phones=False):
  '''List sms messages

    limit - limit of messages to show (optional)"
    offset - starting index (optional)
    msg_type - all|inbox|sent|draft|outbox (default: inbox)
    show_dates - show dates (default: False)
    show_phones - show phone numbers (default: False)    
  '''
  opts = []
  if limit is not None:
    opts += ["-l", limit]
  if offset is not None:
    opts += ["-o", offset]
  if msg_type is not None:
    opts += ["-t", msg_type]
  if show_dates:
    opts += "-d"
  if show_phones:
    opts += "-n"
  return execute(["termux-sms-list"] + opts)

def send(text, number, sim: int = None):
  '''Pick a date

    text - text to send
    number - string / list of numbers
    sim - numeric sim number (optional)
  '''
  opts = []
  if sim is not None:
    opts += ['-s', sim]
  if type(number) is list:
    opts += ["-n", ",".join(number)]
  elif type(number) is str:
    opts += ["-n", number]
  opts.append(text)
  return execute(["termux-sms-send"] + opts)