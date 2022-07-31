'''Termux-API Dialog and Toast methods

    confirm - Show confirmation dialog
    checkbox - Select multiple values using checkboxes
    counter - Pick a number in specified range
    date - Pick a date
    time - Pick a time value
    radio - Pick a single value from radio buttons
    sheet - Pick a value from sliding bottom sheet
    spinner - Pick a single value from a dropdown spinner
    speech - Obtain speech using device microphone
    text - Input text
    toast - Show text as toast (transient popup) 
'''
from .android import execute

def __radiolike(func: str, opts: list | tuple, title: str):
  v = ["-v"]
  v.append(','.join([str(i) for i in opts]))
  if title is not None:
    v += ["-t", title]
  return execute(["termux-dialog", func] + v)

def __hintlike(func: str, hint: str, title: str):
  opts = []
  if hint is not None:
    opts += ["-i", hint]
  if title is not None:
    opts += ["-t", title]
  return execute(["termux-dialog", func] + opts)
   


def confirm(hint: str = None, title: str = None):
  '''Show confirmation dialog

    hint - text hint (optional)
    title - set title of dialog (optional)
  '''
  return __hintlike("confirm", hint, title)

def speech(hint :str = None, title :str = None):
  '''Obtain speech using device microphone

    hint - text hint (optional)
    title - set title of dialog (optional)
  '''
  return __hintlike("speech", hint, title)


def counter(rangeTuple :tuple = None, title :str = None):
  '''Pick a number in specified range

    rangeTuple - tuple of 3 numbers (min, max, start) (optional)
    title - set title of dialog (optional)
  '''
  r = ["-r", ','.join([str(i) for i in rangeTuple])]
  if title is not None:
    r += ["-t", title]
  return execute(["termux-dialog", "counter"] + r)

def date(format: str = None, title: str = None):
  '''Pick a date

    format - SimpleDateFormat (optional) eg "dd-MM-yyyy"
    title - set title of dialog (optional)
  '''
  opts = []
  if format is not None:
    opts += ["-d", format]
  if title is not None:
    opts += ["-t", title]
  return execute(["termux-dialog", "date"] + opts)

def time(title: str = None):
  '''Pick a time value
  
    title - set title of dialog (optional)
  '''
  return __hintlike("time", hint = None, title = title)


def checkbox(opts: tuple, title: str = None):
  '''Select multiple values using checkboxes

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('checkbox', opts, title)

def radio(opts: tuple, title: str = None):
  '''Pick a single value from radio buttons

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('radio', opts, title)

def sheet(opts: tuple, title: str = None):
  '''Pick a value from sliding bottom sheet

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('sheet', opts, title)

def spinner(opts: tuple, title: str = None):
  '''Pick a single value from a dropdown spinner

    opts - tuple of options to use (required)
    title - set title of dialog (optional)
  '''
  return __radiolike('spinner', opts, title)

def text(hint: str = None, multiline: bool = None, number: bool = None, password: bool = None, title: str = None):
  '''Text input

    hint - text hint (optional)
    multiline - multiline input (optional)*
    number - number input (optional)*
    password - password input (optional)
    title - set title of dialog (optional)

    * cannot use together 
  '''
  if (multiline is not None) and (number is not None):
    raise ValueError("Cannot use multiline and number together.")
  opts = []
  if multiline is not None: 
    opts.append("-m")
  if number is not None:
    opts.append("-n")
  if password is not None:
    opts.append("-p")
  if hint is not None:
    opts += ["-i", hint]
  if title is not None:
    opts += ["-t", title]
  return execute("termux-dialog", "text", opts)

def toast(text: str, short: bool = False, **kwargs):
    '''Show a toast message

    text = Text to show toast
    short = only show the toast for a short while (default: false)
    bgcolor = background color (default: gray)
    color = text color (default: white)
    position = [top, middle, or bottom] (default: middle)
    '''
    params = {
      "bgcolor": "b",
      "color": "c",
      "position": "g"
    }
    opts = []
    for k,v in kwargs.items():
        opts += ['-'+params[k], v]
    if short:
        opts.append("-s")
    return execute(["termux-toast"] + opts + [text])
